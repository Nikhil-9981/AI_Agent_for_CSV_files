import time
import streamlit as st
import logging

# Set up a logger to capture warnings and errors
logger = logging.getLogger(__name__)

def make_request_with_rate_limit_handling(request_func, *args, max_retries=2, base_delay=1, max_delay=40, **kwargs):
    """
    Handles requests with automatic retry logic in case of rate limiting errors.
    
    Parameters:
    - request_func (callable): The function to be called for the request.
    - *args: Positional arguments for the request function.
    - max_retries (int): The maximum number of retry attempts on failure (default is 2).
    - base_delay (int): Initial delay time in seconds before retrying (default is 1 second).
    - max_delay (int): Maximum delay between retries, in seconds (default is 40 seconds).
    - **kwargs: Keyword arguments for the request function.
    
    Returns:
    - response: The response from the request function if successful.
    - None: If all retries fail or if a non-rate-limit error occurs.
    """
    attempt = 0  # Track the current attempt number
    delay = base_delay  # Set the initial delay for rate limit handling
    temp_message = st.empty()  # Create a temporary Streamlit message for UI feedback

    # Initial status message
    temp_message.info("Attempting request ...")

    # Loop through retry attempts up to max_retries
    while attempt < max_retries:
        try:
            # Call the request function with provided arguments
            response = request_func(*args, **kwargs)
            
            # If a response is received successfully, show a success message
            if response is not None:
                temp_message.success("Request completed successfully.")
                time.sleep(2)  # Small pause before clearing the message
                temp_message.empty()  # Clear message
                return response  # Return the successful response

        except Exception as e:
            # Handle any exceptions that occur during the request
            x = str(e)  # Store exception message for later display
            logger.warning(f"Attempt {attempt + 1} failed:\n\n {e}")  # Log warning
            temp_message.warning(f"Attempt {attempt + 1} failed:\n\n {e}")  # Display warning in UI
            time.sleep(2)  # Small pause before clearing the message
            temp_message.empty()  # Clear message

            # Check if the exception message indicates a rate limit issue
            if "rate limit" in str(e).lower():
                # Handle rate limit by increasing delay with exponential backoff
                temp_message.warning(f"Rate limit reached. Retrying in {delay} seconds...")
                time.sleep(delay)  # Wait before retrying
                delay = min(max_delay, delay * 2)  # Increase delay, up to max_delay
                temp_message.empty()  # Clear message after delay
            else:
                # For non-rate-limit errors, log and stop retries
                logger.error("Non-rate-limit error. Exiting retries.")
                st.error("Non-rate-limit error encountered. Exiting retries.")
                st.stop()  # Stop further execution
                break  # Exit retry loop

        # Increment the attempt counter after each try
        attempt += 1

    # If all retries fail, log and display an error
    st.error(f"All {max_retries} attempts failed due to rate limits or other errors: \n\n\n{x}")
    logger.error(f"All {max_retries} attempts failed due to rate limits or other errors.")
    st.stop()  # Stop further execution
    return None  # Return None if no successful response is obtained
