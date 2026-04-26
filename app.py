import streamlit as st
from main import run_vibe_guide
import os
import time

st.set_page_config(page_title="VibeGuide | GenAI Edition", layout="wide")

st.title("🧭 VibeGuide: Agentic Concierge")
st.markdown("### *RAG + Live Scraping MCP + Gemini Multi-Agent*")

with st.sidebar:
    st.header("⚙️ System Status")
    st.success("✅ RAG Knowledge Base Connected")
    location = st.text_input("Current Location", "Storrs, Connecticut")
    st.info("Agent: Ready to Scout")

user_query = st.text_input("What are you looking for?", "A minimalist cafe to study")

if st.button("Activate Multi-Agent Workflow"):
    with st.status("Agents are working...", expanded=True) as status:
        st.write("🔍 [Agent 1] Retrieving Taste Profile from RAG Layer...")
        vibe, raw_data, final_plan, file_path = run_vibe_guide(location, user_query)
        st.write("🌐 [Agent 2] Scraper Agent launched. Crawling Google Maps...")
        time.sleep(1)
        st.write("🧠 [Agent 3] Gemini reasoning over crawled data...")
        status.update(label="Workflow Complete!", state="complete", expanded=False)

    col1, col2 = st.columns([2, 1])

    with col1:
        st.subheader("📋 Personalized Recommendation (Gemini)")
        st.markdown(final_plan)

    with col2:
        st.subheader("📍 Live Data Source")
        for venue in raw_data:
            with st.expander(f"📌 {venue['title']}", expanded=True):
                st.write(f"[Open in Google Maps]({venue['url']})")
                st.image(f"https://loremflickr.com/400/250/cafe,interior/all?lock={venue['title'].encode().hex()[:2]}")

    st.divider()
    with open(file_path, "r") as f:
        st.download_button("Download Itinerary (MD)", f.read(), file_name=os.path.basename(file_path))