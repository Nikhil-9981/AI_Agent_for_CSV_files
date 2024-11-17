 
<a id="readme-top"></a>

<!-- Badges Section -->
<div align="center">
  <a href="https://github.com/Nikhil-9981/AI_Agent_for_CSV_files">
    <img src="images/logo.png" alt="Logo" width="100" height="100">
  </a>
  <h1>AI Agent for CSV Files</h1>
 
  
  <!-- Shields -->
  <p>
    <a href="https://github.com/Nikhil-9981/AI_Agent_for_CSV_files/network/members">
      <img src="https://img.shields.io/github/forks/Nikhil-9981/AI_Agent_for_CSV_files?style=for-the-badge" alt="Forks">
    </a>
    <a href="https://github.com/Nikhil-9981/AI_Agent_for_CSV_files/stargazers">
      <img src="https://img.shields.io/github/stars/Nikhil-9981/AI_Agent_for_CSV_files?style=for-the-badge" alt="Stars">
    </a>
    <a href="https://github.com/Nikhil-9981/AI_Agent_for_CSV_files/issues">
      <img src="https://img.shields.io/github/issues/Nikhil-9981/AI_Agent_for_CSV_files?style=for-the-badge" alt="Issues">
    </a>
  </p>
  
  <!-- Description -->
  <p>
    This agent automates the extraction of meaningful insights from  CSV files and Google Sheets. With a simple upload process, users can select specific columns, define custom queries, and retrieve structured information through an AI-driven web search and result parsing system.
  </p>
  
  <!-- Action Links -->
  <p>
    <a href="https://github.com/Nikhil-9981/AI_Agent_for_CSV_files" style="text-decoration:none;">
      <strong>Explore Documentation »</strong>
    </a>
    <br />
    <a href="https://github.com/Nikhil-9981/AI_Agent_for_CSV_files">View Demo</a> · 
    <a href="https://github.com/Nikhil-9981/AI_Agent_for_CSV_files/issues/new?labels=bug&template=bug-report---.md">Report Bug</a> · 
    <a href="https://github.com/Nikhil-9981/AI_Agent_for_CSV_files/issues/new?labels=enhancement&template=feature-request---.md">Request Feature</a>
  </p>
</div>

<!-- Social Media Section -->
<div align="center">
  <a href="https://www.linkedin.com/in/nikhil9981/" target="_blank">
    <img src="https://img.shields.io/badge/LinkedIn-Nikhil%20Kumar%20Singh-blue?style=for-the-badge&logo=linkedin" alt="LinkedIn">
  </a>
 

 <hr />


</div>

 



<!-- TABLE OF CONTENTS -->
<details>
  <summary><h3>Table of Contents </summary>
  <ol>
    <li><a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li><a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
        <li><a href="#user-guide">User Guide</a></li>
        <li><a href="#Optional features">Optional Features </a></li>
      </ul>
    </li> 
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#contact">Contact</a></li>
    
  </ol>
</details>


<!-- ABOUT THE PROJECT -->
## About The Project

<div style="text-align: center;">
  <img src="https://raw.githubusercontent.com/Nikhil-9981/AI_Agent_for_CSV_files/main/images/Product_screenshot.png" alt="Product Name Screen Shot" width="900" />
</div>

This Project enables users to upload CSV files or connect Google Sheets, define search queries, and retrieve specific information for entities in a selected column. It uses web scraping APIs to gather data, processes it with an LLM, and displays the results in a structured format for download or Google Sheets updates.

 ### 🚀 Key Features:
- **Seamless Data Upload**: Upload CSVs or connect directly to Google Sheets for easy integration.
- **Custom Queries**: Define personalized queries, such as *"Find the contact email for {company}"*, to fetch precise data.
- **Automated Web Searches**: Perform web searches for each entity using the powerful **Google Search API**.
- **Advanced Data Parsing**: Results are parsed using cutting-edge **Groq API** for accurate information extraction.
- **Downloadable Results**: The extracted data is organized and available for download in **CSV format** for further analysis or use.

With this project, you can automate  the process of gathering and structuring data, enabling smarter and more efficient decision-making.

<p align="right">(<a href="#readme-top"><strong>Back to top</strong></a>)</p>




## Built With

### Technologies and Tools Used
 
* [![LangChain](https://img.shields.io/badge/LangChain-blue)](https://www.langchain.com/)  
* [![Streamlit](https://img.shields.io/badge/Streamlit-red)](https://streamlit.io/)  
* [![Hugging Face](https://img.shields.io/badge/Hugging%20Face-orange)](https://huggingface.co/)  
* [![Llama](https://img.shields.io/badge/Llama-purple)](https://github.com/facebookresearch/llama)  
* [![Google Gemini](https://img.shields.io/badge/Google%20Gemini-green)](https://cloud.google.com/ai/)  
* [![FAISS](https://img.shields.io/badge/FAISS-lightblue)](https://github.com/facebookresearch/faiss)  
* [![Python](https://img.shields.io/badge/Python-yellow)](https://www.python.org/)  
* [![Google Sheets Connection](https://img.shields.io/badge/Google%20Sheets-blue)](https://developers.google.com/sheets/api)  
* [![Render](https://img.shields.io/badge/Render-lightgreen)](https://render.com/)  
* [![Docker](https://img.shields.io/badge/Docker-lightblue)](https://www.docker.com/)  
* [![Pandas](https://img.shields.io/badge/Pandas-darkblue)](https://pandas.pydata.org/)  
* [![Groq API](https://img.shields.io/badge/Groq%20API-teal)](https://groq.com/)  
* [![Google Search Engine API](https://img.shields.io/badge/Google%20Search%20API-gray)](https://developers.google.com/custom-search/v1/introduction)  
 
 



<p align="right">(<a href="#readme-top"><strong>Back to top</strong></a>)</p>


<!-- GETTING STARTED -->
## Getting Started

Follow the instructions below to set up the project and begin using the **AI Agent for CSV files**.

### 🔧 Prerequisites

   Before you begin, ensure that the following are installed:

1. **Python (version 3.7 or higher)**  
   The project is developed in Python, so you will need to have Python 3.7 or later installed.  
   You can download Python from the official website:  
   ➡️ [Python Downloads](https://www.python.org/downloads/)

2. **Docker (Optional)**  
   If you prefer running the project in a containerized environment, you will need Docker installed:  
   ➡️ [Docker Download](https://www.docker.com/get-started)

3. **External API Keys**  
   You will need API keys for various external services. Please follow the links below to obtain the necessary keys:
   
   - **[GEMINI_API_KEY documentation](https://ai.google.dev/gemini-api/docs?gad_source=1&gclid=CjwKCAiAxea5BhBeEiwAh4t5K6pTGySth9ueQ9Mof3EGIP4-JX3QfMl27w4VBkcDFn0vHP5cEOctshoCfukQAvD_BwE)**  
     🎥 [Youtube Guide](https://youtu.be/OVnnVnLZPEo?si=Y1ZKLIoUNC3rS82P)
   
   - **[GROQ_API_KEY documentation](https://console.groq.com/keys)**  
     🎥 [Youtube Guide](https://youtu.be/TTG7Uo8lS1M?si=VCl3OvpCwMTnzsoY)
   
   - **[GOOGLE_CSE_ID documentation](https://programmablesearchengine.google.com/controlpanel/all)**  
     🎥 [Youtube Guide](https://www.youtube.com/watch?v=vP_inGfKG5E)
   
   - **[GOOGLE_SEARCH_API_KEY documentation](https://developers.google.com/custom-search/v1/introduction)**  
     🎥 [Youtube Guide](https://www.youtube.com/watch?v=bMV_6tmQYDw)

 
| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `GEMINI_API_KEY` | `string` | **Required**. Your GEMINI API key |
| `GROQ_API_KEY` | `string` | **Required**. Your GROQ API key |
| `GOOGLE_CSE_ID` | `string` | **Required**. Your Google Custom Search Engine ID |
| `GOOGLE_SEARCH_API_KEY` | `string` | **Required**. Your Google Search API key |

4. **Text Editor or IDE**  
   You will need a text editor or integrated development environment (IDE) for Python development. Recommended options include:

   - **[Visual Studio Code (VS Code)](https://code.visualstudio.com/Download)**  
   - **[PyCharm](https://www.jetbrains.com/pycharm/download/)**

---

 
### Installation

1. **Clone the Repository**:  <br>
   Run the following command to clone the repository to your local machine:
   ```bash
   git clone https://github.com/Nikhil-9981/AI_Agent_for_CSV_files.git 
   ```

2. **Create a virtual environment**: <br>
    Create a new virtual environment by running:
      ```bash
      python -m venv myenv
      ```
      
      (You can replace myenv with your preferred environment name)


      •  To activate the environment:
      ```bash
      myenv/Scripts/activate
      ```
3. **Install requirements** : <br>
Once the virtual environment is activated, install the required dependencies by running:

   ```bash
   pip install -r requirements.txt
   ```
4. **Obtain API Keys**:  <br>
   Follow the instructions in the [External API Keys](#-prerequisites)(3rd point on Prerequisites) section to get the necessary API keys.
  


5. **Set Up .env File**:  <br>
Run command to setup .env file or :
   ```bash
   python app_file/config.py

   ```

    You will be prompted to add your environment variables one by one, and the application will display a confirmation message once the API key has been successfully added:




 <div style="text-align: center;">
  <img src="https://github.com/Nikhil-9981/AI_Agent_for_CSV_files/blob/main/images/config_show.png?raw=true" alt="Show config" />
</div>







 

   

6. **Run app locally by streamlit**  : <br>
To start the app using Streamlit, run:

    ```bash
    streamlit run app_file/main.py
    ```

 

  **Optional** : <br>
  1. **Check docker is installed  or not** :
  ```bash
    docker images
  ```
  2. **Build docker image using this command**  : <br>
     To build the Docker image, use the following command:
  ```bash
    docker build -t  aiagent .
  ```
  (You can replace aiagent with your preferred environment name.)

  3. **Run docker image locally**  : <br>
    Run the following command to start the Docker image:

  ```bash
   docker run --env-file .env -p 8501:8501 <aiagent>:latest
  ```

4. If you want to deploy docker image on Render follow this link : 
- **[Deployment on Render documentation](https://docs.render.com/)**  
     🎥 [Youtube Guide](https://youtu.be/Qb7tNtIEpcA?si=77bQeRZLVesm_AZJ)




 


<p align="right">(<a href="#readme-top"><strong>Back to top</strong></a>)</p>


 


# User Guide
 

1. **Click on the link to access the website : **  
[AI Agent for CSV File](https://agent-for-csv-dev.onrender.com)
 
Upon clicking the link, you will be redirected to a webpage that appears as shown below:

<div style="text-align: center;">
  <img src="https://raw.githubusercontent.com/Nikhil-9981/AI_Agent_for_CSV_files/main/images/website_display.jpeg" alt="Website display" width="600" />
</div>


2. **Upload a CSV file from your device or provide the public URL of a Google Sheet:**  
   After uploading the file or entering the URL, the interface will update to display your data:  
    
  <div style="text-align: center;">
  <img src="https://raw.githubusercontent.com/Nikhil-9981/AI_Agent_for_CSV_files/main/images/upload_csv.jpeg" alt="Upload CSV" width="600" />
</div>

3. **Select the columns :**  
   Choose the relevant columns in order to perform the desired operations .  
   
   

4. **Submit a query related to the CSV file to retrieve additional data from the web :**  
   You may ask questions such as: *"What are the capitals of the first five countries?"*  
   The system will process your query and extract the relevant information.

5. **View the results and download the extracted data :**  
   Once the query is processed, the results will be displayed. You can then download the extracted data as a CSV file:  
  <div style="text-align: center; display: block; margin: auto;">
  <img src="https://raw.githubusercontent.com/Nikhil-9981/AI_Agent_for_CSV_files/main/images/Result.jpeg" alt="Results" width="600" />
</div>



 
 
## Optional Features 
1. **Multi-Selection Column Functionality**: You can now perform search operations on multiple columns simultaneously, making it more efficient to retrieve relevant information from structured datasets.<br>
***Limitations:***<br>
- Google API Free Tier: There is a limit of 1000 searches per day.<br>
- Groq API Free Tier: You are restricted to using up to 200,000 tokens per day when using Llama 3.<br>
- Google Generative Embeddings: Quota limits depend on the model used, with higher usage requiring requests for increased limits via Google Cloud Console.<br>

2. **Query Refinement using RAG (Retrieval-Augmented Generation)** : RAG enhances query responses by combining document retrieval and generative methods, ensuring more accurate and contextually relevant answers. This approach allows for better refinement of complex queries, improving response quality.

3. **Advanced Error Handling**: Implemented error-handling mechanisms to catch exceptions during API calls or LLM queries, ensuring smooth operation even in the event of failures. Users are notified with clear, actionable messages, and automatic retries with exponential backoff are employed for transient errors.




<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top"><strong>Back to top</strong></a>)</p>

 
 #
<div style="text-align: center; font-size: 36px; font-weight: bold; color: #4CAF50; text-transform: uppercase; letter-spacing: 3px; animation: slideIn 2s ease-in-out;">
    Get in Touch
</div>

<div style="text-align: center; font-size: 20px; font-style: italic; color: #333; margin-top: 10px; animation: fadeIn 2s ease-in-out;">
    I’d love to hear from you!
</div>

<div style="text-align: center; font-size: 18px; color: #FF6347; margin-top: 20px;">
    Nikhil Kumar Singh<br>
    <a href="https://www.linkedin.com/in/nikhil9981/" style="color: #4CAF50; text-decoration: none; font-weight: bold;">@nikhil9981</a><br>
    <a href="mailto:rathaurnikhil14@gmail.com" style="color: #4CAF50; text-decoration: none; font-weight: bold;">rathaurnikhil14@gmail.com</a><br><br>
    Project Link: 
    <a href="https://github.com/Nikhil-9981/AI_Agent_for_CSV_files" style="color: #FF6347; font-weight: bold; text-decoration: none;">AI Agent for CSV Files</a>
</div>

<p align="right" style="font-size: 18px; color: #4CAF50;">
    (<a href="#readme-top" style="color: #FF6347; font-weight: bold;">Back to top</a>)
</p>

 

<div style="text-align: center; font-size: 60px; font-weight: bold; color: #FF6347; text-transform: uppercase; letter-spacing: 5px; animation: bounce 1.5s ease-in-out infinite;">
    THANK YOU!
</div>

<div style="text-align: center; font-size: 24px; font-style: italic; color: #555; animation: fadeIn 2s ease-in-out;">
    Your time and attention mean the world! ✨
</div>

<style>
    @keyframes bounce {
        0%, 100% { transform: translateY(0); }
        50% { transform: translateY(-10px); }
    }

    @keyframes fadeIn {
        0% { opacity: 0; }
        100% { opacity: 1; }
    }

    @keyframes slideIn {
        0% { transform: translateX(-100%); }
        100% { transform: translateX(0); }
    }
</style>
