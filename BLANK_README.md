<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->
<a id="readme-top"></a>
<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Don't forget to give the project a star!
*** Thanks again! Now go create something AMAZING! :D
-->



<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
 
[![Issues][issues-shield]][[issues-url](https://github.com/Nikhil-9981/AI_Agent_for_CSV_files/issues)]
[![LinkedIn][linkedin-shield]][[linkedin-url](https://www.linkedin.com/in/nikhil9981/)]



<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/Nikhil-9981/AI_Agent_for_CSV_files">
    <img src="images/logo.png" alt="Logo" width="80" height="80">
  </a>

<h3 align="center">project_title</h3>

  <p align="center">
    project_description
    <br />
    <a href="https://github.com/github_username/repo_name"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/github_username/repo_name">View Demo</a>
    ·
    <a href="https://github.com/Nikhil-9981/AI_Agent_for_CSV_files/issues/new?labels=bug&template=bug-report---.md">Report Bug</a>
    ·
    <a href="https://github.com/Nikhil-9981/AI_Agent_for_CSV_files/issues/new?labels=enhancement&template=feature-request---.md">Request Feature</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#About-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

[![Product Name Screen Shot][product-screenshot]](https://github.com/Nikhil-9981/AI_Agent_for_CSV_files/blob/main/images/Product_screenshot.png)

This project automates the extraction of meaningful information from structured datasets (CSV or Google Sheets). Users can upload data, select target columns, and define custom prompts to retrieve specific details. The AI agent performs web searches for each entity, parses the results using a language model (LLM), and organizes the information into a structured format.

Key Features:

   • Upload CSVs or connect to Google Sheets
   • Define custom queries (e.g., "Find the contact email for {company}")
   • Perform automated web searches using SerpAPI
   • Parse results with GPT or Groq API
   • Display and download extracted data in CSV format
 

<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Built With

* [![LangChain][LangChain]][LangChain-url]
* [![Streamlit][Streamlit]][Streamlit-url]
* [![Hugging Face][HuggingFace]][HuggingFace-url]
* [![Llama][Llama]][Llama-url]
* [![Google Gemini][GoogleGemini]][GoogleGemini-url]
* [![FAISS][FAISS]][FAISS-url]
* [![Python][Python]][Python-url]
* [![Google Sheets Connection][GoogleSheets]][GoogleSheets-url]
* [![Render][Render]][Render-url]
* [![Docker][Docker]][Docker-url]
* [![Pandas][Pandas]][Pandas-url]
* [![Groq API][GroqAPI]][GroqAPI-url]
* [![Google Search Engine API][GoogleSearchAPI]][GoogleSearchAPI-url]


<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

Follow these instructions to set up the project and start using the AI Agent for Structured Data Retrieval.
### Prerequisites

1. Python (version 3.7 or higher) :
The project is developed in Python, so you will need to install Python 3.7 or later. You can download Python from the official website:
 [Python Donwloads](https://www.python.org/downloads/)



2. Docker (Optional for containerization)
If you prefer using Docker to run the project in a containerized environment, ensure that Docker is installed.
 [Docker Download](https://www.docker.com/get-started)

3. External API Keys 
    • GEMINI_API_KEY : [![YouTube][YouTube]][YouTube-url] [![GEMINI_API_KEY][GEMINI_API_KEY]][YouTube-url] 
    • GROQ_API_KEY : [![YouTube][YouTube]][YouTube-url]  [![GROQ_API_KEY][GROQ_API_KEY]][YouTube-url] 
    • GOOGLE_CSE_ID : [![YouTube][YouTube]][YouTube-url]  [![GOOGLE_CSE_ID][GOOGLE_CSE_ID]][YouTube-url] 
    • GOOGLE_SEARCH_API_KEY : [![YouTube][YouTube]][YouTube-url]  [![GOOGLE_SEARCH_API_KEY][GOOGLE_SEARCH_API_KEY]][YouTube-url] 

4. Text Editor or IDE
 Use any code editor or IDE for Python development. Recommended options include:

  • Visual Studio Code:  **[Download Visual Studio Code (VS Code)](https://code.visualstudio.com/Download)**
  • PyCharm: - **[Download PyCharm](https://www.jetbrains.com/pycharm/download/)**





### Installation

1. Get a free API Key as above given 
2. Clone the repo
   ```sh
   git clone https://github.com/Nikhil-9981/AI_Agent_for_CSV_files.git
   ```
3. Create a virtual environment:
                                    python -m venv <your env name> 
  Here we are considering myenv : -
  ```sh
  python -m venv myenv

  ```
  •  Activate env :
  ```sh 
  myenv/Scripts/activate
  ```

4. Install requirements : 
   ```sh
   pip install -r requirements.txt
   ```
5. Run command to setup .env file or 
   ```sh
  python app_file/config.py
   ```

   you will get opitons to add your env files one by one :
   c:\Users\NIKHIL SINGH\AppData\Local\Packages\MicrosoftWindows.Client.CBS_cw5n1h2txyewy\TempState\ScreenClip\{3D3E85A4-580D-4DF3-AAEB-CD066FF9059C}.png

6. 
  




Commnads :

 
 

-------- Set Envrionmental varialbles-------
GEMINI_API_KEY= 
GROQ_API_KEY= 
GOOGLE_CSE_ID= 
GOOGLE_SEARCH_API_KEY= 

5. streamlit run app_file/main.py


for creating docker image 


6. docker images
7. dokcer build -t  <your_docker_iamge_name> .
8. docker images
9. docker run --env-file .env -p 8501:8501 <agent_name>:latest


<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- USAGE EXAMPLES -->
## Usage

Use this space to show useful examples of how a project can be used. Additional screenshots, code examples and demos work well in this space. You may also link to more resources.

_For more examples, please refer to the [Documentation](https://example.com)_

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ROADMAP -->
## Roadmap

- [ ] Feature 1
- [ ] Feature 2
- [ ] Feature 3
    - [ ] Nested Feature

See the [open issues](https://github.com/github_username/repo_name/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#readme-top">back to top</a>)</p>



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

<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Top contributors:

<a href="https://github.com/github_username/repo_name/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=github_username/repo_name" alt="contrib.rocks image" />
</a>



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Your Name - [@twitter_handle](https://twitter.com/twitter_handle) - email@email_client.com

Project Link: [https://github.com/github_username/repo_name](https://github.com/github_username/repo_name)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

* []()
* []()
* []()

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/github_username/repo_name.svg?style=for-the-badge
[contributors-url]: https://github.com/github_username/repo_name/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/github_username/repo_name.svg?style=for-the-badge
[forks-url]: https://github.com/github_username/repo_name/network/members
[stars-shield]: https://img.shields.io/github/stars/github_username/repo_name.svg?style=for-the-badge
[stars-url]: https://github.com/github_username/repo_name/stargazers
[issues-shield]: https://img.shields.io/github/issues/github_username/repo_name.svg?style=for-the-badge
[issues-url]: https://github.com/github_username/repo_name/issues
[license-shield]: https://img.shields.io/github/license/github_username/repo_name.svg?style=for-the-badge
[license-url]: https://github.com/github_username/repo_name/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/linkedin_username
[product-screenshot]: images/screenshot.png
[Next.js]: https://img.shields.io/badge/next.js-000000?style=for-the-badge&logo=nextdotjs&logoColor=white
[Next-url]: https://nextjs.org/
[React.js]: https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB
[React-url]: https://reactjs.org/
[Vue.js]: https://img.shields.io/badge/Vue.js-35495E?style=for-the-badge&logo=vuedotjs&logoColor=4FC08D
[Vue-url]: https://vuejs.org/
[Angular.io]: https://img.shields.io/badge/Angular-DD0031?style=for-the-badge&logo=angular&logoColor=white
[Angular-url]: https://angular.io/
[Svelte.dev]: https://img.shields.io/badge/Svelte-4A4A55?style=for-the-badge&logo=svelte&logoColor=FF3E00
[Svelte-url]: https://svelte.dev/
[Laravel.com]: https://img.shields.io/badge/Laravel-FF2D20?style=for-the-badge&logo=laravel&logoColor=white
[Laravel-url]: https://laravel.com
[Bootstrap.com]: https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white
[Bootstrap-url]: https://getbootstrap.com
[JQuery.com]: https://img.shields.io/badge/jQuery-0769AD?style=for-the-badge&logo=jquery&logoColor=white
[JQuery-url]: https://jquery.com 
