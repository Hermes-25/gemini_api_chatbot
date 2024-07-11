import streamlit as st
from PyPDF2 import PdfReader
from langchain.text_splitter import RecursiveCharacterTextSplitter
import os

from langchain_google_genai import GoogleGenerativeAIEmbeddings
import google.generativeai as genai

from langchain.vectorstores import FAISS
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains.question_answering import load_qa_chain
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Define PDF file paths
PDF_FILES = [
    "AMAZON_FAQs_v1.pdf",
    
]

# Function to extract text from PDFs
def get_pdf_text(pdf_docs):
    text = ""
    for pdf in pdf_docs:
        pdf_reader = PdfReader(pdf)
        for page in pdf_reader.pages:
            text += page.extract_text()
    return text

def get_text_chunks(text):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
    chunks = text_splitter.split_text(text)
    return chunks

def get_vector_store(text_chunks):
    embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
    vector_store = FAISS.from_texts(text_chunks, embedding=embeddings)
    vector_store.save_local("faiss_index")

def get_conversational_chain():
    prompt_template = """
    Search through the provided FAQ document to find a relevant answer.
    
    If you find a relevant answer, respond with a clear and friendly message based on the information from the FAQs.

    If the question has some personal questions reply in a friendly manner like for the question, "i want to surprise my girlfriend on her bday by sending a gift to her address , can you guide me with the steps?",
    answer can be like,"Wow thats so sweet of you! Here are the steps to change the shipping address and gift wrap the order", and then provide details on chaging addres and gift wrapping from the PDF document.
    
    Also after every reply you give, in the end leave a line and say, "I hope that solves your query, if not please contact our customer care at, https://www.amazon.in/gp/help/customer/contact-us"  
    If the question is asking you to do some task like placing orders,returns,exchanges,making calls etc. , like,"Can you place an order for me?", reply in a friendly manner like,"Sorry, I am an AI Model and I can't do that for you, but i can definitely give you steps to do it by yourself", then give the steps to place an order.

    If you don't find a relevant answer, respond with the following fallback message:
    "Sorry, I couldn't find the information you're looking for in our FAQ document. Please feel free to contact our customer support team for further assistance."\n\n
    Context:\n {context}?\n
    Question: \n{question}\n
    
    Answer:
    """
    model = ChatGoogleGenerativeAI(model="gemini-pro", temperature=0.3)
    prompt = PromptTemplate(template=prompt_template, input_variables=["context", "question"])
    chain = load_qa_chain(model, chain_type="stuff", prompt=prompt)
    return chain

def user_input(user_question):
    embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
    new_db = FAISS.load_local("faiss_index", embeddings, allow_dangerous_deserialization=True)
    docs = new_db.similarity_search(user_question)
    chain = get_conversational_chain()
    response = chain({"input_documents": docs, "question": user_question}, return_only_outputs=True)
    
    if response and "output_text" in response:
        return response["output_text"]
    else:
        return "Sorry, I couldn't find the information you're looking for in our FAQ document. Please feel free to contact our customer support team for further assistance."



def main():
    st.set_page_config("Amazon ChatBot")
    
    # Add Amazon logo beside the header
    logo_path = "Amazon-Logo-31.png"  # Update with your actual file path
    st.image(logo_path, caption='', width=150)
    st.write("# Amazon Customer Support Bot")
    
    # Process PDF documents defined in PDF_FILES
    raw_text = get_pdf_text(PDF_FILES)
    text_chunks = get_text_chunks(raw_text)
    get_vector_store(text_chunks)
    
    # User input handling
    user_question = st.text_input("Feel free to ask any query to our chat bot :)")
    
    if user_question:
        with st.spinner('Generating...'):
            response_text = user_input(user_question)
            st.write("Reply:\n", response_text)
    
    # Add an "About" section or sidebar
    st.sidebar.title("About Amazon Customer Support Bot")
    st.sidebar.markdown("""
    This Amazon Customer Support Bot is built using Streamlit and AI-powered conversational models. Here's how it works:
    
    1. **PDF Processing:** 
       - The bot reads information from a PDF document containing FAQs and product details.
       - It splits the text into manageable chunks and stores them for quick retrieval.
    
    2. **User Interaction:**
       - Users can input questions related to Amazon services or products.
       - The bot uses AI models (such as Google Generative AI, Gemini API, and Langchain embeddings) to generate responses based on the input and stored information.
    
    3. **Response Generation:**
       - After processing the user query, the bot displays a response with relevant information or a fallback message if necessary.
    
    **Technologies Used:**
    - Streamlit for building the web application interface.
    - Python for backend processing and integrating AI models.
    - AI models (such as Google Generative AI, Gemini API, and Langchain embeddings) for natural language understanding and response generation.
    
    **Purpose:**
    - The bot aims to provide quick and accurate answers to common customer queries related to Amazon services and products.
    
    For any feedback or issues, please feel free to reach out to the developer.
    """)

if __name__ == "__main__":
    main()
