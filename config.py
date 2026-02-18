import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    # Model Configuration
    MODEL_NAME = os.getenv("MODEL_NAME", "gpt-4o-mini")
    TEMPERATURE = 0.7
    
    # Crew Settings
    VERBOSE = True
    ALLOW_DELEGATION = False
    
    # API Keys
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

    @staticmethod
    def validate():
        if not Config.OPENAI_API_KEY:
            raise ValueError("❌ OPENAI_API_KEY not found. Please check your .env file.")
