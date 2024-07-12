## gemini_api_chatbot
# Amazon Customer Support Bot

## Overview
This project implements an AI-powered customer support bot for Amazon using Streamlit, Google Generative AI, Gemini API, and Langchain embeddings. The bot interacts with users, answers queries based on stored FAQ documents and the customer database, and provides personalized responses.

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

3. Include dependencies such as Streamlit, PyPDF2, Langchain, Google Generative AI, etc.

## API Keys: Obtain API keys for Google Generative AI and store them in a .env file:
```bash
GOOGLE_API_KEY=your_api_key_here
```
# Installation
## Clone the repository:
```bash
git clone https://github.com/your_username/amazon-support-bot.git
cd amazon-support-bot
```
## Install dependencies:
```bash
pip install -r requirements.txt
```
## Usage
### Run the application:
```bash
streamlit run app.py
```
## Open your web browser: Navigate to http://localhost:8501 to interact with the bot.

1. Input Queries: Enter questions related to Amazon services or products in the text input field.

2. View Responses: The bot will generate responses based on the queries, leveraging AI models and stored FAQ information.

# About
- This Amazon Customer Support Bot aims to enhance customer interaction by providing efficient and accurate responses to common queries regarding Amazon's products and services. It utilizes advanced AI technologies for natural language processing and response generation.


![WhatsApp Image 2024-07-11 at 12 08 17_cd7fff76](https://github.com/Hermes-25/gemini_api_chatbot/assets/152592240/f36fc2f0-cbcf-497c-992a-ef55107d1607)
![image](https://github.com/user-attachments/assets/46a81adf-d2da-4e90-bbc8-19a5eb059af2)

