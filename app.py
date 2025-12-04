import streamlit as st
import requests

# 1. App Title
st.title("🗣️ Brian Multilingual (Json2Video API)")

# 2. API Key Setup (Secure)
# Tries to get from secrets first, otherwise asks user
api_key = st.secrets.get("JSON2VIDEO_API_KEY")
if not api_key:
    api_key = st.text_input("Enter Json2Video API Key", type="password")

# 3. User Inputs
# We default to the voice you requested: Brian Multilingual
voice_id = "en-US-BrianMultilingualNeural"
text_input = st.text_area("Text to speak (English, Spanish, French, etc.)", "Hello! I am Brian. ¡Hola! Soy Brian.")

# 4. The Generation Logic
if st.button("Generate Audio"):
    if not api_key:
        st.error("Please enter your API Key.")
    else:
        with st.spinner("Requesting audio from Json2Video..."):
            try:
                # API Configuration
                url = "https://api.json2video.com/v2/voice"
                
                payload = {
                    "text": text_input,
                    "voice": voice_id
                }
                
                headers = {
                    "x-api-key": api_key,
                    "Content-Type": "application/json"
                }

                # Make the request
                response = requests.post(url, json=payload, headers=headers)

                # Handle Response
                if response.status_code == 200:
                    # Success: Play and Download
                    st.success("Success!")
                    
                    # Display Audio Player
                    st.audio(response.content, format="audio/mp3")
                    
                    # Download Button
                    st.download_button(
                        label="Download MP3",
                        data=response.content,
                        file_name="brian_multilingual.mp3",
                        mime="audio/mp3"
                    )
                else:
                    # Error from API
                    st.error(f"Error {response.status_code}: {response.text}")
                    
            except Exception as e:
                st.error(f"Connection Error: {e}")
