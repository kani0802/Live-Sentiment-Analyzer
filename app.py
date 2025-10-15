import streamlit as st
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import nltk

# NLTK download step for the cloud environment
# This ensures VADER is available even if deployed to a new machine
try:
    # Try to find it first, if not found, download it.
    nltk.data.find('sentiment/vader_lexicon.zip')
except AttributeError:
    nltk.download('vader_lexicon')

# Initialize VADER
analyzer = SentimentIntensityAnalyzer()

# --- Analysis Logic (Identical to your successful analyzer code) ---
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

# --- Streamlit Interface (What users see) ---
st.title('💬 Simple Live Sentiment Analyzer')
st.write('Paste any English text below to instantly analyze the emotion (polarity).')
st.markdown("---")

# Text input box for the user
user_input = st.text_area("Paste your text here:", 
                          "This project is easy to understand, and I fixed all the errors!", 
                          height=150)

if st.button('Analyze Sentiment'):
    if user_input:
        # Get the compound VADER score
        score = analyzer.polarity_scores(user_input)['compound']
        sentiment_category = categorize_sentiment(score)

        # Display results
        st.markdown("### Analysis Result:")
        st.write(f"**Overall Sentiment:** **{sentiment_category}**")
        st.write(f"**VADER Compound Score:** `{score:.4f}` (Range: -1.0 to +1.0)")

        # Display detailed scores
        st.markdown("#### Detailed Scores (Positive/Neutral/Negative):")
        scores = analyzer.polarity_scores(user_input)
        
        # Streamlit provides a simple progress bar for visualization
        st.write(f"Positive: {scores['pos']:.3f}")
        st.progress(scores['pos'])
        
        st.write(f"Neutral: {scores['neu']:.3f}")
        st.progress(scores['neu'])
        
        st.write(f"Negative: {scores['neg']:.3f}")
        st.progress(scores['neg'])

    else:

        st.warning("Please paste some text to analyze!")
