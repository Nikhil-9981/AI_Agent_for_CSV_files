import streamlit as st
import pandas as pd
from dotenv import load_dotenv
import os
from langchain_core.prompts import PromptTemplate
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chains import RetrievalQA
from langchain_community.utilities import GoogleSearchAPIWrapper
from langchain_google_genai import ChatGoogleGenerativeAI,GoogleGenerativeAIEmbeddings
from langchain_groq import ChatGroq
from langchain.agents import Tool, initialize_agent
import io
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from Prompts import get_qa_chain_prompt, get_search_results_prompt
from logger_config import log_info, log_error, log_exception, log_warning
from rate_limit_handling import make_request_with_rate_limit_handling


def setup_ai_agent():
    """
    Sets up the AI agent using Groq's model and Google Search API.

    Logs the setup process and any exceptions. Stops execution if there is a critical error.

    Returns:
        agent (Agent): The initialized AI agent with real-time search capabilities.
    """
    log_info("Setting up the AI agent with Groq's model and Google Search API.")
    try:
        # Initialize ChatGroq with model specifications and API key
        ai_agent = ChatGroq(
            model="llama-3.1-70b-versatile",
            temperature=0.3,
            max_tokens=None,
            timeout=60,
            max_retries=2,
            api_key=os.getenv("GROQ_API_KEY")
        )
        
        # Initialize Google Search API
        search = GoogleSearchAPIWrapper(
            google_api_key=os.getenv("GOOGLE_SEARCH_API_KEY"),
            search_engine="google",
            google_cse_id=os.getenv("GOOGLE_CSE_ID")
        )
        
        # Set up tool for search functionality
        tools = [
            Tool(
                name="Google",
                func=search.run,
                description="Useful for answering questions with real-time information."
            )
        ]

        # Initialize the AI agent with tools
        agent = initialize_agent(
            llm=ai_agent,
            tools=tools,
            verbose=True,
            agent="zero-shot-react-description",
            handle_parsing_errors=True
        )

        log_info("AI agent successfully set up.")
        return agent

    except Exception as e:
        log_exception(f"Critical error setting up AI agent: {e}")
        st.error(f"Error setting up AI agent:\n\n{e}")
        st.stop()  # Stop further execution if setup fails


def initialize_qa_chain(context):
    """
    Initializes the QA chain by setting up embeddings, chunking context text, and configuring the retrieval chain.

    Args:
        context (str): The text to be split and used as the context for retrieval.

    Returns:
        qa_chain (RetrievalQA): A retrieval QA chain configured with embeddings and a FAISS index.
    """
    try:
        log_info("Initializing the language model...")
        
        # Initialize GoogleGenerativeAI with Gemini model
        model = ChatGoogleGenerativeAI(
            model="gemini-1.5-pro",
            google_api_key=os.getenv("GEMINI_API_KEY"),
            temperature=0.4,
            convert_system_message_to_human=True
        )

        log_info("Splitting the context text into manageable chunks...")
        
        # Split the context into chunks for efficient processing
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=10000, chunk_overlap=1000)
        texts = text_splitter.split_text(context)
        
        if not texts:
            log_warning("No text chunks generated from context. Check if context is empty.")

        log_info("Setting up embeddings...")
        
        # Set up embeddings model for vector storage
        embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001", google_api_key=os.getenv("GEMINI_API_KEY"))

        log_info("Building FAISS index...")
        
        # Build a FAISS index to store and retrieve text chunks
        vector_index = FAISS.from_texts(texts, embeddings).as_retriever(search_kwargs={"k": 5})
        
        # Get the QA chain prompt template
        QA_CHAIN_PROMPT = PromptTemplate.from_template(get_qa_chain_prompt())

        log_info("Initializing the QA chain...")
        
        # Set up the QA chain with the vector index
        qa_chain = RetrievalQA.from_chain_type(
            model,
            retriever=vector_index,
            return_source_documents=True,
            chain_type_kwargs={"prompt": QA_CHAIN_PROMPT},
        )
        
        log_info("QA chain initialized successfully.")
        return qa_chain
    
    except Exception as e:
        log_exception(f"Critical error in initializing QA chain: {e}")
        st.error(f"Error initializing QA chain:\n\n{e}")
        st.stop()  # Stop further execution if initialization fails


def generate_search_results(response_text, agent):
    """
    Generates search results from the response text using the AI agent.

    Args:
        response_text (str): The text to generate search results for.
        agent (Agent): The initialized AI agent with real-time search capabilities.

    Returns:
        csv_data (pd.DataFrame): Dataframe containing the search results in CSV format.
    """
    log_info("Generating search results from the response text.")
    
    # Load the search results prompt template
    template = get_search_results_prompt()

    # Fetch search results with rate limit handling
    search_result_csv = make_request_with_rate_limit_handling(agent.run, f"{response_text}, {template}")

    if search_result_csv:
        try:
            # Parse CSV data
            csv_data = pd.read_csv(io.StringIO(search_result_csv))
            log_info("Search results successfully processed into CSV format.")
            return csv_data
        except Exception as e:
            log_error(f"Failed to process response into CSV: {e}")
            st.error(f"Error processing response into CSV format: \n\n{e}")
            st.stop()  # Stop further execution if CSV parsing fails
    else:
        log_error("Rate limit exceeded or another error occurred. Could not fetch search results.")
        st.error("Rate limit exceeded. Could not fetch search results.")
        st.stop()  # Stop further execution if rate limit is hit or other error occurs
