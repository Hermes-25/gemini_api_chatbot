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
