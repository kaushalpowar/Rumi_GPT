import streamlit as st
from streamlit.components.v1 import html
import openai
import os
from langchain.prompts import PromptTemplate
from langchain.llms import OpenAI
from langchain_openai import ChatOpenAI

from langchain.chains import LLMChain

# Use environment variable for API key
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

# Set page config
st.set_page_config(page_title="Rumi's Wisdom", page_icon="🕯️", layout="wide")

# Custom CSS for a modern, dark theme design
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Poppins', sans-serif;
        color: #e0e0e0;
    }
    
    .main {
        background-color: #121212;
    }
    
    .stTextInput > div > div > input {
        background-color: #1e1e1e;
        color: #e0e0e0;
        border: 1px solid #333333;
        border-radius: 8px;
        padding: 15px;
        font-size: 16px;
    }
    
    .stButton > button {
        background-color: #bb86fc;
        color: #121212;
        font-weight: 600;
        border-radius: 8px;
        padding: 0.6rem 2rem;
        font-size: 1rem;
        transition: all 0.3s;
        border: none;
        box-shadow: 0 4px 6px rgba(187, 134, 252, 0.2);
    }
    
    .stButton > button:hover {
        background-color: #a66efa;
        box-shadow: 0 6px 8px rgba(187, 134, 252, 0.3);
        transform: translateY(-2px);
    }
    
    .quote-box {
        background-color: #1e1e1e;
        padding: 2rem;
        border-radius: 12px;
        box-shadow: 0 8px 16px rgba(0, 0, 0, 0.3);
        margin-top: 2rem;
        transition: all 0.3s;
    }
    
    .quote-box:hover {
        box-shadow: 0 12px 24px rgba(0, 0, 0, 0.4);
        transform: translateY(-5px);
    }
    
    .sidebar .sidebar-content {
        background-color: #1e1e1e;
    }
</style>
""", unsafe_allow_html=True)

code_template = PromptTemplate(
    input_variables=["user_input"],
    template='You are a chatbot with the personality of Rumi (Persian poet). Based on the following feelings of the user, suggest a relevant Rumi quote with a brief explanation that will uplift them: {user_input}'
)

def get_rumi_quote(user_input):
    open_ai_llm = ChatOpenAI(model="gpt-3.5-turbo",temperature=0.7, max_tokens=1000)
    code_chain = LLMChain(llm=open_ai_llm, prompt=code_template, verbose=True)
    message = code_chain.run(user_input)
    return message

def main():
    col1, col2, col3 = st.columns([1,2,1])
    
    with col2:
        st.image("Header_image.png", use_column_width=True)
        st.markdown("<h1 style='text-align: center; color: #bb86fc; font-weight: 600;'>Rumi's Wisdom</h1>", unsafe_allow_html=True)
        st.markdown("<p style='text-align: center; color: #b0b0b0; font-size: 18px;'>Let the words of Rumi illuminate your soul 🕯️</p>", unsafe_allow_html=True)
        
        user_input = st.text_area("How are you feeling today?", height=100, max_chars=200, key="user_input")
        
        
        if st.button("Seek Wisdom", use_container_width=True):
            if user_input:
                with st.spinner("Channeling Rumi's spirit..."):
                    quote = get_rumi_quote(user_input)
                    st.markdown(f"<p style='font-style: italic; color: #bb86fc; font-size: 18px;'>{quote}</p>", unsafe_allow_html=True)
                    st.markdown("</div>", unsafe_allow_html=True)
            else:
                st.warning("Please share your feelings before seeking Rumi's wisdom.")
    
    with st.sidebar:
        st.markdown("<h3 style='color: #bb86fc; font-weight: 600;'>About</h3>", unsafe_allow_html=True)
        st.markdown("Welcome to Rumi's Wisdom, a chatbot that provides insightful Rumi quotes to inspire and uplift your spirit. 🌟")
        
        st.markdown("<h3 style='color: #bb86fc; font-weight: 600;'>How it works</h3>", unsafe_allow_html=True)
        st.markdown("1. Share your current feelings or state of mind in the text area.")
        st.markdown("2. Click 'Seek Wisdom' to receive a relevant Rumi quote.")
        st.markdown("3. Reflect on the wisdom shared and let it guide you.")
        
        st.markdown("<h3 style='color: #bb86fc; font-weight: 600;'>Creator</h3>", unsafe_allow_html=True)
        st.markdown("Crafted with ❤️ by [Kaushal](https://x.com/holy_kau)")
        
        st.markdown("<br>", unsafe_allow_html=True)
        html("""
        <script type="text/javascript" src="https://cdnjs.buymeacoffee.com/1.0.0/button.prod.min.js" data-name="bmc-button" data-slug="kaushal.ai" data-color="#bb86fc" data-emoji=""  data-font="Cookie" data-text="Support my work" data-outline-color="#000000" data-font-color="#121212" data-coffee-color="#FFDD00" ></script>
        """, height=70, width=220)

if __name__ == "__main__":
    main()

