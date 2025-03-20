from fastapi import FastAPI
from pydantic import BaseModel
from utils import fetch_article_urls, extract_article_content, summarize_text, analyze_sentiment, extract_topics, comparative_analysis, generate_hindi_tts
import os

# Creates a FastAPI app
app = FastAPI()

# Defines a data structure for the request
class CompanyRequest(BaseModel):
    company_name: str  # Holds the company name as a string

# Sets up the "/analyze" endpoint to handle POST requests
@app.post("/analyze")
def analyze_company(request: CompanyRequest):
    # Gets article URLs for the company
    urls = fetch_article_urls(request.company_name)
    processed_articles = []  # List to store article details
    
    # Loops through each URL
    for i, url in enumerate(urls):
        # Extracts title and content from the article
        article_data = extract_article_content(url)
        # Checks if article data is valid and has content
        if article_data and article_data['content'] != "No content available":
            # Shortens the article content
            summary = summarize_text(article_data['content'])
            # Logs the URL and summary for tracking
            print(f"Processing fetched article - URL: {url} | Summary: {summary}")
            # Finds the sentiment of the summary
            sentiment = analyze_sentiment(summary)
            # Picks out key topics from the summary
            topics = extract_topics(summary)
            # Names an audio file for this article
            audio_file = f"audio_{i}.mp3"
            # Creates a Hindi audio file from the summary
            generate_hindi_tts(summary, audio_file)
            # Adds article details to the list
            processed_articles.append({
                "title": article_data['title'],
                "summary": summary,
                "sentiment": sentiment,
                "topics": topics,
                "audio": audio_file
            })
    
    # Compares all processed articles
    comparative_result = comparative_analysis(processed_articles)
    # Makes a final summary based on the most common sentiment
    final_summary = f"Media coverage for {request.company_name} is mostly {max(comparative_result['sentiment_distribution'], key=comparative_result['sentiment_distribution'].get)}." if processed_articles else "No valid articles found."
    # Names the final audio file
    final_audio_file = "final_audio.mp3"
    # Creates a Hindi audio file for the final summary
    generate_hindi_tts(final_summary, final_audio_file)
    
    # Returns all the results in a dictionary
    return {
        "company": request.company_name,
        "articles": processed_articles,
        "comparative_analysis": comparative_result,
        "final_audio": final_audio_file
    }