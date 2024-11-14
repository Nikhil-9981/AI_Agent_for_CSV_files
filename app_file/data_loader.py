# Import logging functionality from logging.py
from logger_config import log_info, log_warning, log_exception

import pandas as pd
import streamlit as st
from streamlit_gsheets import GSheetsConnection

def load_data():
    """
    Loads data from either a CSV file uploaded by the user or a Google Sheets URL.
    The user is prompted to choose the data source, and the corresponding data is loaded accordingly.
    
    Returns:
        pd.DataFrame: DataFrame containing the loaded data, or None if no data is loaded.
    """
    data_source = st.radio("Choose data source", ["Upload CSV", "Connect to Google Sheet"])
     
    uploaded_file = None
    sheet_url = None
    df = None

    if data_source == "Upload CSV":
        uploaded_file = st.file_uploader("🔽 Upload a CSV file", type="csv", label_visibility="collapsed")
        if uploaded_file:
            try:
                df = pd.read_csv(uploaded_file)
                log_info("CSV file loaded successfully.")
            except Exception as e:
                st.error("Failed to load CSV file.")
                log_exception(e)
    elif data_source == "Connect to Google Sheet":
        sheet_url = st.text_input("Enter Google Sheet URL")
        if sheet_url:
            try:
                conn = st.connection("gsheets", type=GSheetsConnection)
                df = conn.read(spreadsheet=sheet_url)
                log_info("Google Sheet loaded successfully.")
            except Exception as e:
                st.error(f"An error occurred while loading the Google Sheet. There could be two reasons: \n1. The link URL is incorrect. \n2. The URL points to a private sheet. \n\nError details: \n\nPlease reload the page and paste the link again.")


                log_exception(e)
    else:
        log_warning("No data source selected.")

    return df

# Display the uploaded or connected data
def display_data_preview(df):
    """
    Displays a preview of the loaded data, showing available and selected columns for further processing.
    Users can choose columns from the data for further operations.
    
    Args:
        df (pd.DataFrame): The DataFrame containing the uploaded or connected data.
    
    Returns:
        str: A string representation of the selected columns of the DataFrame for further processing.
    """
    if df is not None:
         
        
        st.markdown("<h3 style='color: #4CAF50;'>Data Preview</h3>", unsafe_allow_html=True)
        row_count = len(df)
        height = min(row_count * 30, 210)  # Dynamic height calculation for the dataframe
        st.dataframe(df, height=height)
        
        available_col, selected_col = st.columns([1, 3])
        with available_col:
            st.markdown("<h4 style='color: #4CAF50;'>Available Columns</h4>", unsafe_allow_html=True)
            columns = ["All Columns"] + list(df.columns)
            chosen_columns = st.multiselect("Drag columns to the right to select", columns)
            
            if "All Columns" in chosen_columns:
                chosen_columns = list(df.columns)
                log_info("All columns selected for operation.")
            else:
                log_info(f"Selected columns: {chosen_columns}")

        with selected_col:
            st.markdown("<h4 style='color: #4CAF50;'>Selected Columns</h4>", unsafe_allow_html=True)
            selected_columns = st.multiselect("Selected columns to operate on", chosen_columns, default=chosen_columns)
             
        return selected_columns
    
     
    return None
