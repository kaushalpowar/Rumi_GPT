import streamlit as st
import openai

openai.api_key = st.secrets["api_secret"]


def get_rumi_quote(user_input):
    prompt = f"Give me a Rumi quote for : {user_input} and explain that quote. \n"
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        temperature=0.5,
        max_tokens=1024,
        n=1,
        stop=None,
        timeout=30,
    )
    message = response.choices[0].text
    return message


def main():
    import streamlit as st
    st.image("/Users/kaushal/Documents/Projects/poems_like_rumi/Header_image.png")

    html_temp = """
                    <div style="background-color:{};padding:1px">

                    </div>
                    """
    with st.sidebar:
        st.markdown("""
        # About 
        Hi!👋 I'm a chatbot that provides Rumi quotes to help motivate and inspire you 😇        """)
        st.markdown(html_temp.format("rgba(55, 53, 47, 0.16)"), unsafe_allow_html=True)
        st.markdown("""
        # How does it work
        Simply enter how you are feeling right now.
        """)
        st.markdown(html_temp.format("rgba(55, 53, 47, 0.16)"), unsafe_allow_html=True)
        st.markdown("""
        Made by [@Obelisk_1531](https://twitter.com/Obelisk_1531)
        """,
                    unsafe_allow_html=True,
                    )

    st.markdown("<h4 style='text-align: center;'>Let Rumi guide you with our chatbot🤖❤️ ️</h4>",
                unsafe_allow_html=True)

    user_input = st.text_input("\nTell me how you feel?\n")
    st.write("\n")

    st.markdown(
        """
        <style>

        .stButton button {
            background-color: #752400;
            color: white;
            border-radius: 4px;
            padding: 0.5rem 1rem;
            font-size: 1.25rem;
            margin: 0 auto;
            display: block;

        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    st.button("Generate")

    if user_input:
        with st.spinner("I'm searching the best Rumi quote for you..."):
            quote = get_rumi_quote(user_input)
            st.write(f"\nHere's a Rumi quote for you: \n{quote}")


if __name__ == "__main__":
    main()

