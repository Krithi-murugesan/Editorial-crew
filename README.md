### AI Content Lifecycle Manager ✍️🤖
An autonomous multi-agent editorial pipeline built with CrewAI. This system transforms a single topic into a structured, SEO-optimized, and editorially vetted blog post using specialized AI agents.

# 🌟 Overview
Unlike simple LLM prompts, this Content Lifecycle Manager uses a "Relay" architecture. Each agent is a specialist that focuses on one part of the editorial process, passing its output as context to the next stage. This ensures higher quality, better structure, and professional-grade content.

# 👥 The Crew
The system consists of three specialized agents:

Content Planner: Researches latest trends, identifies target audience pain points, and creates a strategic SEO outline.

Content Writer: Translates the plan into a compelling Markdown draft, distinguishing between objective facts and expert opinion.

Editor: Conducts the final audit for journalistic integrity, brand voice alignment, and grammatical precision.

# 🛠️ Technical Pillars
This project implements several core concepts of Agentic AI:

Role-Playing: Distinct backstories and goals for each agent.

Sequential Process: A strict "Plan -> Write -> Edit" workflow.

Context Management: Passing results from one task as the "fuel" for the next.

# Focus: allow_delegation=False to keep agents dedicated to their specific expertise.

🚀 Getting Started
Prerequisites
Python 3.10+
An OpenAI API Key
