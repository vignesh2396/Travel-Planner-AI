# config.py

import os

class Config:
    PROVIDER = os.environ.get("PROVIDER", "gemini").lower()

    GEMINI_API_KEY = "AIzaSyB5ER3FZDpfZ0CDaDbyifTHCF70IM0C-Js"
    GEMINI_MODEL = "gemini-2.5-flash"

    # OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY", "")
    # OPENAI_MODEL = "gpt-4o-mini"

    DEFAULT_CURRENCY = "INR"
    MAX_DAYS = 14
    MIN_DAYS = 1