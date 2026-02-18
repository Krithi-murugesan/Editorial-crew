import os
from dotenv import load_dotenv
from config import Config
from logger import logger
from crew import ContentCrew

def run():
    try:
        # Validate API Keys
        Config.validate()
        
        logger.info("🚀 Starting Content Creation Crew...")
        
        topic = input("Enter a topic for the blog post: ")
        
        content_crew = ContentCrew(topic)
        result = content_crew.run()
        
        logger.info("✅ Crew workflow completed successfully.")
        
        print("\n" + "="*30)
        print("FINAL OUTPUT")
        print("="*30 + "\n")
        print(result)

    except Exception as e:
        logger.error(f"An error occurred during execution: {e}")

if __name__ == "__main__":
    run()
