from crewai import Crew, Process
from agents import ContentAgents
from tasks import ContentTasks

class ContentCrew:
    def __init__(self, topic):
        self.topic = topic
        self.agents = ContentAgents()
        self.tasks = ContentTasks()

    def run(self):
        # Initialize Agents
        planner = self.agents.planner()
        writer = self.agents.writer()
        editor = self.agents.editor()

        # Initialize Tasks
        task1 = self.tasks.plan_task(planner, self.topic)
        task2 = self.tasks.write_task(writer, self.topic)
        task3 = self.tasks.edit_task(editor)

        # Form the Crew
        crew = Crew(
            agents=[planner, writer, editor],
            tasks=[task1, task2, task3],
            process=Process.sequential,
            verbose=True
        )
        return crew.kickoff()
