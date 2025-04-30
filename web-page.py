import streamlit as st
import asyncio
from scrape import scrape_website


import nest_asyncio
nest_asyncio.apply()

# Streamlit app title
st.title("Async Website Scraper")

# Text input for website URL
website = st.text_input("Enter a website URL", "https://www.google.com")

# When the "Scrape" button is pressed
if st.button("Scrape"):
    with st.spinner("Scraping..."):
        try:
            # Create a new event loop for the scraping operationj
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)
            
            # Call the scrape_website function asynchronously
            html_content = loop.run_until_complete(scrape_website(website))
            
            # Display the result
            if html_content:
                st.success("Scraping complete!")
                # Display the HTML content in a scrollable text area
                st.text_area("Scraped Content", html_content, height=400)
            else:
                st.warning("No content scraped or an error occurred.")
            
            # Close the loop
            loop.close()
        
        except Exception as e:
            # Handle any errors that might occur during scraping
            st.error(f"Something went wrong: {e}")
