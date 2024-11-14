import streamlit as st
import pandas as pd
from agent import setup_ai_agent, initialize_qa_chain, generate_search_results
from data_loader import load_data, display_data_preview
from config import load_dotenv
import warnings
from logger_config import log_exception

# Suppress any warning messages for a cleaner output
warnings.filterwarnings("ignore")

# Load environment variables from a .env file
load_dotenv()


def setup_streamlit_page():
    """
    Configures the Streamlit page layout and style, setting the page title, icon, and other stylistic elements.
    
    If an error occurs, logs the exception and stops execution to prevent further issues.
    """
    try:
        # Setting up page configuration
        st.set_page_config(
            page_title="AI Agent for CSV files",
            page_icon="📊",
            layout="centered",
        )
        
        # Adding a header with a green color and centered alignment
        st.markdown("<h1 style='text-align: center; color: #4CAF50;'>📊 AI Agent for CSV files</h1>", unsafe_allow_html=True)
        
        # Adding a horizontal line for visual separation
        st.markdown("<hr style='border-top: 3px solid #4CAF50;'>", unsafe_allow_html=True)
    
    except Exception as e:
        # Log and display error if page setup fails
        log_exception(f"Error setting up Streamlit page: {e}")
        st.error("An error occurred while setting up the page.")
        st.stop()  # Stop further execution if setup fails


def main():
    """
    Main function to orchestrate the Streamlit app's flow.
    
    The function:
    - Sets up the page layout.
    - Loads and previews data.
    - Allows users to select columns and ask questions.
    - Processes the question using an AI agent and displays search results.
    
    Only critical errors and key events are logged.
    """
    # Setup the page layout and styling
    setup_streamlit_page()

    try:
        # Load data from a CSV file or Google Sheets (handled in load_data function)
        df = load_data()
        
        # Check if data is loaded successfully
        if df is not None:
            # Display a data preview and allow column selection
            selected_columns = display_data_preview(df)
            
            if selected_columns:
                # Convert selected columns to a context string for AI processing
                context = df[selected_columns].to_string(index=False)
                
                # Initialize the AI agent and QA chain with the context
                agent = setup_ai_agent()
                qa_chain = initialize_qa_chain(context)

                # UI for user to ask a question
                st.markdown("<h3 style='color: #4CAF50;'>Ask a Question</h3>", unsafe_allow_html=True)
                question = st.text_input("Ask a question related to the data:")

                # Button to trigger answer generation
                if st.button("Get Answer"):
                    # Run the QA chain on the user’s question
                    result = qa_chain({"query": question})
                    response_text = result["result"]

                    # Display the answer obtained
                    st.markdown("<h3 style='color: #4CAF50;'>Answer:</h3>", unsafe_allow_html=True)
                    
                    # Generate search results based on the answer
                    csv_data = generate_search_results(response_text, agent)
                    
                    if csv_data is not None:
                        # Display search results in a table format
                        st.write("Web Search Results:")
                        st.dataframe(csv_data)

                        # Option to download the search results as a CSV file
                        csv_download = csv_data.to_csv(index=False).encode('utf-8')
                        st.download_button(
                            label="Download Results as CSV",
                            data=csv_download,
                            file_name="search_results.csv",
                            mime="text/csv"
                        )
            else:
                # Display a warning if no columns are selected
                st.warning("Please select columns to proceed.")
        else:
            # Display a warning if data is not loaded
            st.warning("Please upload a CSV file or provide a Google Sheets URL to load the data.")
    
    except Exception as e:
        # Log critical error and display it to the user
        log_exception(f"Critical error in main function: {e}")
        st.error(f"An unexpected error occurred: \n\n {e}")
        st.stop()  # Stop execution on encountering a critical error


# Entry point of the Streamlit app
if __name__ == "__main__":
    main()
