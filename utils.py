import requests
from bs4 import BeautifulSoup
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from gtts import gTTS
from deep_translator import GoogleTranslator
import nltk
from nltk.tokenize import sent_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import re
import os

# Download NLTK resources
nltk.download('punkt')  # For sentence splitting
nltk.download('stopwords')  # For common words to skip
nltk.download('wordnet')  # For word simplification

# Initialize tools
analyzer = SentimentIntensityAnalyzer()  # For sentiment analysis
lemmatizer = WordNetLemmatizer()  # For simplifying words
stop_words = set(stopwords.words('english'))  # List of words to ignore
translator = GoogleTranslator(source='en', target='hi')  # For English-to-Hindi translation

def fetch_article_urls(company_name):
    # Gets news article links for a company from Google News
    # Input: company_name (string) - Company name
    # Output: List of up to 10 URLs, or empty list if failed
    query = f"{company_name} news"  # Search term
    url = f"https://www.google.com/search?q={query}&tbm=nws"  # Google News URL
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }  # Browser simulation headers
    try:
        response = requests.get(url, headers=headers, timeout=10)  # Sends request with 10-second timeout
        response.raise_for_status()  # Checks for errors
        soup = BeautifulSoup(response.text, 'html.parser')  # Parses HTML
        urls = []  # Stores URLs
        for item in soup.select('div.SoaBEf')[:10]:  # Takes first 10 news items
            link = item.select_one('a')['href']  # Extracts link
            urls.append(link)  # Adds to list
        return urls  # Returns URLs
    except Exception as e:
        print(f"Error getting URLs: {e}")  # Logs error
        return []  # Returns empty list on failure

def extract_article_content(url):
    # Extracts title and text from an article URL
    # Input: url (string) - Article URL
    # Output: Dictionary with title and text, or None if failed
    try:
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"}  # Browser headers
        response = requests.get(url, headers=headers, timeout=5)  # Sends request with 5-second timeout
        response.raise_for_status()  # Checks for errors
        soup = BeautifulSoup(response.text, 'html.parser')  # Parses HTML
        title = soup.find('title').text if soup.find('title') else "No title available"  # Gets title or default
        paragraphs = soup.find_all('p')  # Finds paragraphs
        content = ' '.join([p.text for p in paragraphs]) if paragraphs else "No content available"  # Combines text or default
        return {"title": title, "content": content}  # Returns title and text
    except Exception as e:
        print(f"Error fetching {url}: {e}")  # Logs error
        return None  # Returns None on failure

def summarize_text(text):
    # Shortens text to first 3 sentences
    # Input: text (string) - Text to shorten
    # Output: Shortened text with "..." if longer than 3 sentences
    sentences = sent_tokenize(text)  # Splits into sentences
    if len(sentences) > 3:  # Takes first 3 if more than 3
        return ' '.join(sentences[:3]) + "..."
    return text  # Returns full text if 3 or less

def analyze_sentiment(text):
    # Analyzes text sentiment with VADER
    # Input: text (string) - Text to check
    # Output: "Happy", "Sad", or "Normal"
    score = analyzer.polarity_scores(text)  # Gets sentiment scores
    compound = score['compound']  # Uses compound score
    print(f"Sentiment - Text: {text[:100]}... | Compound: {compound} | Neg: {score['neg']} | Neu: {score['neu']} | Pos: {score['pos']}")  # Logs scores
    if compound > 0.1:  # Happy if above 0.1
        sentiment = "Happy"
    elif compound < -0.1:  # Sad if below -0.1
        sentiment = "Sad"
    else:  # Normal if between
        sentiment = "Normal"
    print(f"Result: {sentiment}")  # Logs result
    return sentiment  # Returns sentiment

def extract_topics(text):
    # Finds 3 key words from text
    # Input: text (string) - Text to analyze
    # Output: List of 3 unique words
    words = re.findall(r'\w+', text.lower())  # Extracts words, converts to lowercase
    cleaned_words = [lemmatizer.lemmatize(word) for word in words if word not in stop_words and len(word) > 3]  # Simplifies, skips short or common words
    return list(set(cleaned_words[:3]))  # Returns 3 unique words

def comparative_analysis(articles):
    # Compares articles by sentiment, coverage, and topics
    # Input: articles (list) - List of article data
    # Output: Dictionary with sentiment counts, differences, and topics
    sentiment_dist = {"Happy": 0, "Sad": 0, "Normal": 0}  # Counts sentiments
    coverage_diff = []  # Stores coverage notes
    topics_overview = {"common": set(), "unique": {}}  # Tracks common and unique topics
    if not articles:  # Returns empty result if no articles
        return {
            "sentiment_distribution": sentiment_dist,
            "coverage_difference": [{"comparison": "No articles available", "impact": "N/A"}],
            "topics_overview": topics_overview
        }
    for i, article in enumerate(articles):  # Loops through articles
        sentiment_dist[article['sentiment']] += 1  # Updates sentiment count
        topics = set(article['topics'])  # Converts topics to set
        if i == 0:  # Sets common topics from first article
            topics_overview['common'] = topics
        else:  # Updates common topics with overlap
            topics_overview['common'] &= topics
        topics_overview['unique'][f"Article {i+1}"] = list(topics - topics_overview['common'])  # Stores unique topics
    if len(articles) >= 2:  # Compares topics if 2 or more articles
        coverage_diff.append({
            "comparison": f"Article 1 highlights {articles[0]['topics']}, Article 2 focuses on {articles[1]['topics']}",
            "impact": "Different focus shows varied views."
        })
    elif len(articles) == 1:  # Notes limited data if 1 article
        coverage_diff.append({
            "comparison": f"One article focuses on {articles[0]['topics']}",
            "impact": "Not enough to compare."
        })
    else:  # Notes no data if no articles
        coverage_diff.append({
            "comparison": "No articles to compare",
            "impact": "N/A"
        })
    return {
        "sentiment_distribution": sentiment_dist,
        "coverage_difference": coverage_diff,
        "topics_overview": topics_overview
    }  # Returns analysis

def generate_hindi_tts(summary_text, filename="output.mp3"):
    # Creates Hindi audio from text
    # Input: summary_text (string) - Text to convert, filename (string) - File name (default: "output.mp3")
    # Output: File name of saved audio
    translated_text = translator.translate(summary_text)  # Translates to Hindi
    print(f"Hindi text: {translated_text[:100]}... | File: {filename}")  # Logs translation
    tts = gTTS(text=translated_text, lang='hi', slow=False)  # Generates audio
    tts.save(filename)  # Saves file
    return filename  # Returns file name