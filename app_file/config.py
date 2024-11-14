import os
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

# Function to set environment variables in the .env file
def set_env_variable(key, value):
    with open('.env', 'a') as f:
        f.write(f"{key}={value}\n")

# Fetch API keys from environment variables
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
GOOGLE_CSE_ID = os.getenv("GOOGLE_CSE_ID")
GOOGLE_SEARCH_API_KEY = os.getenv("GOOGLE_SEARCH_API_KEY")

# Check if any API key is not set and ask the user to input them
if not GEMINI_API_KEY:
    GEMINI_API_KEY = input("Enter your GEMINI_API_KEY: ")
    set_env_variable("GEMINI_API_KEY", GEMINI_API_KEY)

if not GROQ_API_KEY:
    GROQ_API_KEY = input("Enter your GROQ_API_KEY: ")
    set_env_variable("GROQ_API_KEY", GROQ_API_KEY)

if not GOOGLE_CSE_ID:
    GOOGLE_CSE_ID = input("Enter your GOOGLE_CSE_ID: ")
    set_env_variable("GOOGLE_CSE_ID", GOOGLE_CSE_ID)

if not GOOGLE_SEARCH_API_KEY:
    GOOGLE_SEARCH_API_KEY = input("Enter your GOOGLE_SEARCH_API_KEY: ")
    set_env_variable("GOOGLE_SEARCH_API_KEY", GOOGLE_SEARCH_API_KEY)


# Check if each API key is set, and raise an error for each missing key
if not GEMINI_API_KEY:
    raise ValueError("The GEMINI_API_KEY environment variable is missing.")

if not GROQ_API_KEY:
    raise ValueError("The GROQ_API_KEY environment variable is missing.")

if not GOOGLE_CSE_ID:
    raise ValueError("The GOOGLE_CSE_ID environment variable is missing.")

if not GOOGLE_SEARCH_API_KEY:
    raise ValueError("The GOOGLE_SEARCH_API_KEY environment variable is missing.")
else:
    print("API keys have been set successfully.")
