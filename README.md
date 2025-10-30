# NEWS_PULSE; AI NEWS SUMMARIZER

This project fetches news articles about a company, summarizes them, performs sentiment analysis, extracts key topics, and converts the summaries into Hindi audio. It has two versions: a web application using Streamlit and an API server using FastAPI.

## Project Structure
- **`app.py`** - Streamlit application for an interactive UI.
- **`api.py`** - FastAPI server for API-based access.
- **`utils.py`** - Helper functions for fetching, summarizing, sentiment analysis, etc.
- **`requirements.txt`** - List of required dependencies.
- **`README.md`** - Documentation.
## Project demo
![np1](images/np1.png)
![np2](images/np2.png)
![np3](images/np3.png)
![np4](images/np4.png)


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



# Deployed Here** :
https://huggingface.co/spaces/SayyedAli/NEW-Summarizer_AND_TTS_MODEL?logs=container





