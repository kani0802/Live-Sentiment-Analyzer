import streamlit as st
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import nltk

import os
import ssl

nltk_data_path = os.path.join(os.getcwd(), 'nltk_data')
if not os.path.exists(nltk_data_path):
    os.makedirs(nltk_data_path)
nltk.data.path.append(nltk_data_path)


try:
  
    nltk.data.find('sentiment/vader_lexicon.zip')
except LookupError:
 
    try:
      
        _create_unverified_https_context = ssl._create_unverified_context
    except AttributeError:
        
        pass
    else:
       
        ssl._create_default_https_context = _create_unverified_https_context
        
    nltk.download('vader_lexicon')

analyzer = SentimentIntensityAnalyzer()


def categorize_sentiment(score):
    if score >= 0.7:
        return 'VERY HAPPY 😀'
    elif score > 0.1:
        return 'Happy 🙂'
    elif score <= -0.7:
        return 'VERY SAD 😡'
    elif score < -0.1:
        return 'Sad 🙁'
    else:
        return 'Okay 😐'


st.title('💬 Simple Live Sentiment Analyzer')
st.write('Paste any English text below to instantly analyze the emotion (polarity).')
st.markdown("---")


user_input = st.text_area("Paste your text here:", 
                          "This project is easy to understand, and I fixed all the errors!", 
                          height=150)

if st.button('Analyze Sentiment'):
    if user_input:
       
        score = analyzer.polarity_scores(user_input)['compound']
        sentiment_category = categorize_sentiment(score)

   
        st.markdown("### Analysis Result:")
        st.write(f"**Overall Sentiment:** **{sentiment_category}**")
        st.write(f"**VADER Compound Score:** `{score:.4f}` (Range: -1.0 to +1.0)")

       
        st.markdown("#### Detailed Scores (Positive/Neutral/Negative):")
        scores = analyzer.polarity_scores(user_input)
        
    
        st.write(f"Positive: {scores['pos']:.3f}")
        st.progress(scores['pos'])
        
        st.write(f"Neutral: {scores['neu']:.3f}")
        st.progress(scores['neu'])
        
        st.write(f"Negative: {scores['neg']:.3f}")
        st.progress(scores['neg'])

    else:

        st.warning("Please paste some text to analyze!")


