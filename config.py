import os
import streamlit as st

class Config:
    PROVIDER = os.environ.get("PROVIDER", "gemini").lower()

    # Gemini not used
    GEMINI_API_KEY = os.getenv("GEMINI_API_KEY") or st.secrets.get("GEMINI_API_KEY")
    GEMINI_MODEL = "models/gemini-2.5-pro-preview-03-25"

    # OpenAI
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY") or st.secrets.get("OPENAI_API_KEY")
    OPENAI_MODEL = "gpt-4o-mini"  # you can also use "gpt-4o" if needed

    DEFAULT_CURRENCY = "INR"
    MAX_DAYS = 14
    MIN_DAYS = 1
