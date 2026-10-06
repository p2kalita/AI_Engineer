from strands import Agent
from strands_tools import shell
from tools.text_count import text_count

agent = Agent(
    system_prompt=(
        "You are a helpful text analysis assistant. "
        "Answer the questions using the tools available"
    ),
    tools=[text_count, shell],
)
agent("how similar are two articles in the data folder")