# Use the official Python image as a base
FROM python:3.11-slim

# Set environment variables
ENV STREAMLIT_APP=app.py
ENV STREAMLIT_PORT=8501
ENV STREAMLIT_DEBUG=False
ENV GEMINI_API_KEY="Your GEMINI_API_KEY"
ENV GROQ_API_KEY="Your GROQ_API_KEY"
ENV GOOGLE_CSE_ID="Your GOOGLE_CSE_ID"
ENV GOOGLE_SEARCH_API_KEY="Your GOOGLE_SEARCH_API_KEY"

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file to the container
COPY requirements.txt .

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the Streamlit application files to the container
COPY . .

# Expose the Streamlit port
EXPOSE ${STREAMLIT_PORT}

# Run the Streamlit app
CMD ["streamlit", "run", "app_file/main.py"]
