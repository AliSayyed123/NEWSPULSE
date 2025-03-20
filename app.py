import streamlit as st
import requests

# Sets the page title
st.title("News Summarization and TTS Application")

# Adds a text box for company name, defaults to "Tesla"
company_name = st.text_input("Enter Company Name", "Tesla")

# Runs when the "Analyze" button is clicked
if st.button("Analyze"):
    # Sends company name to the API
    response = requests.post("http://localhost:8000/analyze", json={"company_name": company_name})
    
    # Checks if API call worked
    if response.status_code == 200:
        data = response.json()  # Gets data from API response
        
        # Shows a heading with the company name
        st.subheader(f"Analysis for {data['company']}")
        
        # Loops through each article in the data
        for article in data['articles']:
            st.write(f"**Title**: {article['title']}")  # Displays article title
            st.write(f"**Summary**: {article['summary']}")  # Displays article summary
            st.audio(article['audio'], format="audio/mp3")  # Plays article audio
            st.write(f"**Sentiment**: {article['sentiment']}")  # Shows article sentiment
            st.write(f"**Topics**: {', '.join(article['topics'])}")  # Lists article topics
            st.write("---")  # Adds a line break between articles
        
        # Shows a heading for comparison
        st.subheader("Comparative Analysis")
        st.write(data['comparative_analysis'])  # Displays comparison data
        
        # Shows a heading for the final audio
        st.subheader("Hindi Audio Summary (Overall)")
        st.audio(data['final_audio'], format="audio/mp3")  # Plays the final Hindi audio
    
    # Shows an error if API call fails
    else:
        st.error(f"Error fetching data from API: {response.status_code}")