
from strands import Agent
from strands_tools import editor, load_tool
from tools.text_count import text_count

SYSTEM_PROMPT = """You are a text analysis assistant with meta-tooling capabilities.
You have some existing tools. Use them when they fit the task.
When a required capability does not exist in your current tools, create it.

## TOOL NAMING
- File name and function name must match
- Example: tools/my_tool.py contains a function called my_tool

## TOOL STRUCTURE
Use the @tool decorator:

```python
from strands import tool

@tool
def tool_name(param1: str, param2: int = 10) -> dict:
    \"\"\"Description of what this tool does.

    Args:
        param1: What this parameter is
        param2: What this parameter is
    \"\"\"
    # implementation
    return {"result": "value"}
```

## CREATION WORKFLOW
1. Write the tool to a file in the tools/ directory using editor
2. Validate syntax: python -c "import ast; ast.parse(open('path').read())"
3. Run a quick test to verify it works
4. Load it with load_tool (path=file_path, name=function_name)
5. Retry the original task using the new tool

## CONSTRAINTS
- Check if a suitable tool already exists before creating one
- Do not modify existing tools unless explicitly asked
- Handle bad input gracefully — return an error dict, do not crash
- One tool, one job
"""

agent = Agent(
    system_prompt=SYSTEM_PROMPT,
    tools=[text_count, editor, load_tool],
)


agent(
    "How similar are the two articles in the data folder?"
)