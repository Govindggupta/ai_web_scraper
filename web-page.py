import streamlit as st

st.title("Web Scraper")
url = st.text_input("Enter the URL of the website you want to scrape")

if st.button("Scrape Site"):
    st.write("Scraping...")