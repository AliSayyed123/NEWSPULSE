# News Summarizer and Talk-to-Speech Model

This project fetches news articles about a company, summarizes them, performs sentiment analysis, extracts key topics, and converts the summaries into Hindi audio. It has two versions: a web application using Streamlit and an API server using FastAPI.

## Features
- Fetches news articles from Google News.
- Summarizes articles into three sentences.
- Performs sentiment analysis (Happy, Sad, or Neutral).
- Extracts three main topics from each summary.
- Converts summaries and overall analysis to Hindi audio.
- Provides a web interface (Streamlit) or an API (FastAPI).

## Project Structure
- **`app.py`** - Streamlit application for an interactive UI.
- **`api.py`** - FastAPI server for API-based access.
- **`utils.py`** - Helper functions for fetching, summarizing, sentiment analysis, etc.
- **`requirements.txt`** - List of required dependencies.
- **`README.md`** - Documentation.

## Tech Stack
### Languages
- **Python** (Version 3.7+ recommended)

### Libraries
- **Streamlit** - For building the web application.
- **FastAPI** - For API-based access.
- **Pydantic** - For API request validation.
- **Requests** - To fetch web pages and articles.
- **BeautifulSoup4** - To parse HTML and extract news content.
- **VaderSentiment** - For sentiment analysis.
- **gTTS (Google Text-to-Speech)** - To generate Hindi audio.
- **Deep-Translator** - To translate English summaries to Hindi.
- **NLTK** - For text processing and topic extraction.
- **Uvicorn** - To run the FastAPI server.

### APIs Used
- **Google News (Unofficial)** - Scraped using `requests` and `BeautifulSoup4` to fetch article URLs. No API key required, but dependent on Google’s HTML structure.
- **Google Translate (via Deep-Translator)** - Converts English text to Hindi.
- **Google Text-to-Speech (via gTTS)** - Converts text summaries to Hindi audio.

## Installation and Setup
### Prerequisites
- **Python 3.7+** - Download from [python.org](https://www.python.org/)
- **Git** - Install from [git-scm.com](https://git-scm.com/)
- **Internet** - Required for news fetching, translation, and text-to-speech conversion.

### Steps to Set Up
1. **Clone the Repository**
   ```bash
   git clone https://github.com/AliSayyed123/News-Summarizer-and-Talk-to-Speech-model.git
   cd News-Summarizer-and-Talk-to-Speech-model
   ```
2. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

## Running the Project
### Option 1: Run the Streamlit Web App  
Provides a web-based UI to interact with the model.  
```bash
streamlit run app.py
```

### Option 2: Run the API Server  
Starts the FastAPI server using Uvicorn.
```bash
uvicorn api:app --reload
```

## Usage
- Use the **Streamlit Web App** for an interactive experience.
- Use the **FastAPI server** to integrate the service into other applications.

## Contributing
Feel free to contribute by forking the repository and submitting pull requests.



---

For any issues or improvements, open a GitHub issue or reach out to the maintainers.

