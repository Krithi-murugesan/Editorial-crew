from crewai import Task

class ContentTasks:
    def plan_task(self, agent, topic):
        return Task(
            description=f"1. Prioritize latest trends on {topic}. 2. Identify target audience. 3. Develop outline with SEO keywords.",
            expected_output="A comprehensive content plan document with outline and audience analysis.",
            agent=agent
        )

    def write_task(self, agent, topic):
        return Task(
            description=f"1. Use the plan to craft a blog post on {topic}. 2. Incorporate SEO naturally. 3. Ensure proper markdown structure.",
            expected_output="A well-written blog post in markdown format (2-3 paragraphs per section).",
            agent=agent
        )

    def edit_task(self, agent):
        return Task(
            description="Proofread the blog post for grammar and alignment with the brand's voice.",
            expected_output="A polished, publication-ready markdown blog post.",
            agent=agent
        )
