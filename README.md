## gemini_api_chatbot
# Amazon Customer Support Bot

## Overview
This project implements an AI-powered customer support bot for Amazon using Streamlit, Google Generative AI, Gemini API, and Langchain embeddings. The bot interacts with users, answers queries based on stored FAQ documents, and provides personalized responses.

## Features
- **PDF Processing:** Extracts and splits text from PDF documents containing FAQs.
- **Natural Language Processing:** Uses AI models to understand user queries and generate appropriate responses.
- **Fallback Mechanism:** Provides a default response if no relevant information is found in the FAQs.
- **Interactive Interface:** Built using Streamlit for easy user interaction.

## Prerequisites
Ensure you have the following installed and configured before running the application:
1. **Python 3.7+**
2. **Dependencies:** Install required Python packages using:
   ```bash
   pip install -r requirements.txt
