# NEWS_PULSE:News Summarizer and Text-to-Speech Model

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

# Deployed Here :https://huggingface.co/spaces/SayyedAli/NEW-Summarizer_AND_TTS_MODEL?logs=container




