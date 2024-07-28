import streamlit as st
import requests

API_BASE_URL = "https://text-fixer-lilac.vercel.app"

def make_post_request(endpoint, payload):
    response = requests.post(f"{API_BASE_URL}{endpoint}", json=payload)
    return response.json()

st.set_page_config(page_title="Text Manipulation Toolkit", page_icon="🛠️", layout="wide")
st.title('Text Manipulation Toolkit')
st.markdown("""
Welcome to the **Text Manipulation Toolkit**! This app provides various text manipulation utilities powered by an API. 
Navigate through the sidebar to access different features.
""")

st.sidebar.title("Navigation")
pages = ["Home", "Remove Tags", "Extract Emails and URLs", "Word Count", "Remove Line Breaks", "Character Counter", "HTML Link Extractor", "Password Generator", "Random Quote", "Detect Language", "Acronym Generator"]
page = st.sidebar.radio("Go to", pages)


if page == "Home":
    st.header('Welcome to Text Manipulation Toolkit')
    st.markdown("""
    This toolkit offers a range of features to manipulate and analyze text. Choose a tool from the sidebar to get started:
    - **Remove Tags:** Remove HTML tags from your text.
    - **Extract Emails and URLs:** Extract all emails and URLs from your text.
    - **Word Count:** Count the number of words in your text.
    - **Remove Line Breaks:** Remove line breaks from your text.
    - **Character Counter:** Count the number of characters in your text.
    - **HTML Link Extractor:** Extract links from HTML content.
    - **Password Generator:** Generate a random secure password.
    - **Random Quote:** Get a random quote.
    - **Detect Language:** Detect the language of your text.
    - **Acronym Generator:** Generate an acronym from a phrase.
    """)

elif page == "Remove Tags":
    st.header('Remove HTML Tags')
    html_input = st.text_area("Enter HTML content:")
    if st.button("Remove Tags"):
        payload = {"html": html_input}
        result = make_post_request("/text-manipulation/remove-tags/json", payload)
        st.write("Cleaned Text:")
        st.write(result.get("cleaned_text", "Error processing request"))

elif page == "Extract Emails and URLs":
    st.header('Extract Emails and URLs')
    text_input = st.text_area("Enter text:")
    if st.button("Extract"):
        payload = {"text": text_input}
        result = make_post_request("/text-manipulation/extract-emails-urls", payload)
        st.write("Extracted Emails and URLs:")
        st.write(result)

elif page == "Word Count":
    st.header('Word Count')
    text_input = st.text_area("Enter text:")
    if st.button("Count Words"):
        payload = {"text": text_input}
        result = make_post_request("/text-manipulation/word-count", payload)
        st.write("Word Count:")
        st.write(result.get("word_count", "Error processing request"))

elif page == "Remove Line Breaks":
    st.header('Remove Line Breaks')
    text_input = st.text_area("Enter text:")
    if st.button("Remove Line Breaks"):
        payload = {"text": text_input}
        result = make_post_request("/text-manipulation/remove-line-breaks", payload)
        st.write("Text without Line Breaks:")
        st.write(result.get("cleaned_text", "Error processing request"))

# Page: Character Counter
elif page == "Character Counter":
    st.header('Character Counter')
    text_input = st.text_area("Enter text:")
    if st.button("Count Characters"):
        payload = {"text": text_input}
        result = make_post_request("/text-manipulation/character-counter", payload)
        st.write("Character Count:")
        st.write(result.get("character_count", "Error processing request"))

# Page: HTML Link Extractor
elif page == "HTML Link Extractor":
    st.header('HTML Link Extractor')
    html_input = st.text_area("Enter HTML content:")
    if st.button("Extract Links"):
        payload = {"html": html_input}
        result = make_post_request("/html-manipulation/html-link-extractor", payload)
        st.write("Extracted Links:")
        st.write(result)

# Page: Password Generator
elif page == "Password Generator":
    st.header('Password Generator')
    if st.button("Generate Password"):
        result = requests.get(f"{API_BASE_URL}/random-password-generator").json()
        st.write("Generated Password:")
        st.write(result.get("password", "Error generating password"))

# Page: Random Quote
elif page == "Random Quote":
    st.header('Random Quote')
    if st.button("Get Quote"):
        result = requests.get(f"{API_BASE_URL}/random-quote").json()
        st.write("Random Quote:")
        st.write(result.get("quote", "Error fetching quote"))

# Page: Detect Language
elif page == "Detect Language":
    st.header('Detect Language')
    text_input = st.text_area("Enter text:")
    if st.button("Detect Language"):
        payload = {"text": text_input}
        result = make_post_request("/text-manipulation/detect-language", payload)
        st.write("Detected Language:")
        st.write(result.get("language", "Error detecting language"))

# Page: Acronym Generator
elif page == "Acronym Generator":
    st.header('Acronym Generator')
    phrase_input = st.text_input("Enter phrase:")
    if st.button("Generate Acronym"):
        payload = {"phrase": phrase_input}
        result = make_post_request("/acronym-generator", payload)
        st.write("Generated Acronym:")
        st.write(result.get("acronym", "Error generating acronym"))

