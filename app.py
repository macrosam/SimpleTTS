import streamlit as st
import edge_tts
import asyncio

st.title("🗣️ Brian Multilingual (Free Edge Version)")

# 1. User Input
text_input = st.text_area("Text to speak", "Hello! I am Brian. ¡Hola! Soy Brian.")

# 2. Async Function to Generate Audio
async def generate_speech(text, output_file):
    voice = "en-US-BrianMultilingualNeural"
    communicate = edge_tts.Communicate(text, voice)
    await communicate.save(output_file)

# 3. The Button
if st.button("Generate Audio"):
    if not text_input:
        st.error("Please enter some text.")
    else:
        output_file = "brian_edge.mp3"
        
        with st.spinner("Generating..."):
            # Run the async function
            try:
                asyncio.run(generate_speech(text_input, output_file))
                
                # Success!
                st.success("Generated successfully!")
                
                # Play Audio
                st.audio(output_file, format="audio/mp3")
                
                # Download Button
                with open(output_file, "rb") as f:
                    st.download_button(
                        label="Download MP3",
                        data=f,
                        file_name="brian_voice.mp3",
                        mime="audio/mp3"
                    )
            except Exception as e:
                st.error(f"Error: {e}")
