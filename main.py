import os
from dotenv import load_dotenv
from crewai_project.crew import ContentCrew

# Load environment variables from .env file
load_dotenv()

def run():
    print("## Welcome to the Content Lifecycle Manager Crew")
    print("---------------------------------------")
    topic = input("Enter a topic for the blog post: ")
    
    content_crew = ContentCrew(topic)
    result = content_crew.run()
    
    print("\n\n########################")
    print("## FINAL OUTPUT ##")
    print("########################\n")
    print(result)

if __name__ == "__main__":
    run()
