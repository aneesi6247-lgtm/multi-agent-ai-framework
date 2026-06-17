import streamlit as st
from Youtube_video_analyzer import youtube_agent

st.set_page_config(
    page_title="YouTube Video Analyzer",
    layout="centered",
)

st.title("YouTube Video Analyzer")

@st.cache_resource # Cache the agent to avoid reinitialization on every run
def get_agent():
    return youtube_agent()

agent = get_agent()

# input box
video = st.text_input("Enter YouTube video URL") # return the stril 
button = st.button("Analyze") # return true or false

if button and video:
    with st.spinner("Analyzing video..."):
        response = agent.run(f"Analyze this video: {video}")
        st.markdown(response.content)
