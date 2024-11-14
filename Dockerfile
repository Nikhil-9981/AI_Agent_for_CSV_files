# Use the official Python image as a base
FROM python:3.11-slim

# Set environment variables
ENV STREAMLIT_APP=app.py
ENV STREAMLIT_PORT=8501
ENV STREAMLIT_DEBUG=False
ENV GEMINI_API_KEY="AIzaSyAGGrU9FTYnQ6AutDvj7m_OuGD_ZJY6STo"
ENV GROQ_API_KEY="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"
ENV GOOGLE_CSE_ID="33b55e189a0e043e0"
ENV GOOGLE_SEARCH_API_KEY="AIzaSyDo4_JJG6-LWOxwvsfngV97mYV5Ncl-L_I"

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
