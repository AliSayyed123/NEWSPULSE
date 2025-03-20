# News-Summarizer-and-Talk-to-Speech-model
# News Summarizer and Talk-to-Speech Model

This project fetches news articles about a company, summarizes them, checks their sentiment, finds key topics, and turns the summaries into Hindi audio. It has two versions: a web app using Streamlit and an API server using FastAPI.

## Features
- Gets news articles from Google News.
- Shortens articles to 3 sentences.
- Checks if summaries are Happy, Sad, or Normal.
- Picks 3 main topics from each summary.
- Makes Hindi audio for summaries and an overall summary.
- Offers a web interface (Streamlit) or an API (FastAPI).

## Files
- **`app.py`**: A standalone Streamlit app that does everything in one file.
- **`api.py`**: A FastAPI server that works with `utils.py` for an API.
- **`utils.py`**: Helper functions for the FastAPI version (fetching, summarizing, etc.).
- **`requirements.txt`**: List of libraries needed.
- **`README.md`**: This file!

## Tech Stack
### Languages
- **Python**: Used for all code (version 3.7+ works best).

### Libraries
- **Streamlit**: Builds the web app in `app.py`.
- **FastAPI**: Creates the API server in `api.py`.
- **Pydantic**: Sets up data format for API requests.
- **Requests**: Gets web pages from Google News and articles.
- **BeautifulSoup4**: Reads HTML to find news links and text.
- **VaderSentiment**: Checks text sentiment.
- **gTTS (Google Text-to-Speech)**: Makes Hindi audio from text.
- **Deep-Translator**: Translates English to Hindi using Google Translate.
- **NLTK**: Splits text into sentences and skips common words.
- **Uvicorn**: Runs the FastAPI server.

### APIs Used
- **Google News (Unofficial)**: Scraped with `requests` and `BeautifulSoup4` to get article URLs. No API key needed, but depends on Google’s HTML layout.
- **Google Translate (via Deep-Translator)**: Turns English summaries into Hindi. Uses an unofficial API through `deep-translator`.
- **Google Text-to-Speech (via gTTS)**: Creates Hindi audio files. No API key required, but needs internet.

## How to Run
### Prerequisites
- **Python**: Install Python 3.7 or higher from [python.org](https://www.python.org/).
- **Git**: Get Git from [git-scm.com](https://git-scm.com/) to clone the repo.
- **Internet**: Required for news fetching, translation, and audio.

### Steps
1. **Clone the Repository**
   ```bash
   git clone https://github.com/AliSayyed123/News-Summarizer-and-Talk-to-Speech-model.git
   cd News-Summarizer-and-Talk-to-Speech-model
   Running the Project
# Project Name

## You can run the project in two ways:

### Run the Streamlit Web App  
This provides a web-based UI to interact with the model.  

```bash
streamlit run app.py
   ```
###To run the API
**This starts the FastAPI server using Uvicorn.**

```bash
Copy code
uvicorn api:app

