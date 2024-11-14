import logging
import os

# Define default values for log file and log level
LOG_FILE = 'logging_file/logging_file.log'  # You can change this to any file path you want
LOG_LEVEL = logging.INFO  # You can set this to logging.DEBUG, logging.WARNING, etc.

# Set up logging configuration
log_dir = os.path.dirname(LOG_FILE)
if log_dir and not os.path.exists(log_dir):
    os.makedirs(log_dir)

# Initialize logger
def initialize_logger(name=__name__, log_file=LOG_FILE, log_level=LOG_LEVEL):
    """
    Initializes and configures a logger with both file and console handlers.
    
    Args:
        name (str): Name of the logger.
        log_file (str): File path for logging output.
        log_level (int): Logging level (e.g., logging.INFO, logging.DEBUG).
    
    Returns:
        logging.Logger: Configured logger object.
    """
    logger = logging.getLogger(name)
    logger.setLevel(log_level)

    # Set up file handler
    file_handler = logging.FileHandler(log_file)
    file_handler.setLevel(log_level)

    # Set up console handler
    console_handler = logging.StreamHandler()
    console_handler.setLevel(log_level)

    # Define formatter for consistent log messages
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)

    # Add handlers if not already added to avoid duplication
    if not logger.handlers:
        logger.addHandler(file_handler)
        logger.addHandler(console_handler)
    
    return logger

# Initialize the logger for this module
logger = initialize_logger()

# Logging functions for various log levels
def log_info(message):
    """Log an informational message."""
    logger.info(message)

def log_warning(message):
    """Log a warning message."""
    logger.warning(message)

def log_error(message):
    """Log an error message."""
    logger.error(message)

def log_exception(exception):
    """Log an exception with traceback."""
    logger.exception(f"An error occurred: {exception}")

def log_debug(message):
    """Log a debug message for detailed insights."""
    logger.debug(message)

 