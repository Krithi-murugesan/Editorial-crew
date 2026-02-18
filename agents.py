from crewai import Agent

class ContentAgents:
    def planner(self):
        return Agent(
            role="Content Planner",
            goal="Plan engaging and factually accurate content on {topic}",
            backstory="You are planning a blog article about {topic}. You collect information that helps the audience learn and make informed decisions.",
            llm="gpt-4o-mini",
            allow_delegation=False,
            verbose=True
        )

    def writer(self):
        return Agent(
            role="Content Writer",
            goal="Write an insightful and factually accurate opinion piece on {topic}",
            backstory="You are writing a new opinion piece about {topic} based on the planner's outline. You provide objective insights and distinguish opinions from facts.",
            llm="gpt-4o-mini",
            allow_delegation=False,
            verbose=True
        )

    def editor(self):
        return Agent(
            role="Editor",
            goal="Edit a blog post to align with the organization's style",
            backstory="You review blog posts for journalistic best practices, balanced viewpoints, and brand voice alignment.",
            llm="gpt-4o-mini",
            allow_delegation=False,
            verbose=True
        )
