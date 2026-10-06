# Meta-Tooling with Strands Agents

An agent that builds its own tools at runtime when it hits a task outside its current capabilities.
Read the full blog here: https://builder.aws.com/content/3IO189piaHzh5VrzvgfAyDZe9j2/agents-can-build-their-own-tools-now

## Setup

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Configure your model provider (AWS Bedrock credentials via environment or AWS CLI profile).

## Run

**Step 1 — The basic agent (works for counting number of characters, words and sentences in text, fails for most other questions):**

```bash
python basic_agent.py
```

Has a `text_count` tool that handles "how many words?" fine. Then you ask "how similar are these two articles?" There's no tool for that, and the agent cannot answer satisfactorily.

**Step 2 — The meta-tooling agent (builds what it needs):**

```bash
python metatooling_agent.py
```

Same similarity question. The agent recognizes it lacks a tool, creates a `text_similarity` tool with the `@tool` decorator, tests it, loads it into its live registry, and answers — all in one conversation.

## What's here

```
├── basic_agent.py           # Has word_count — works for some tasks, fails for others
├── metatooling_agent.py     # Has meta-tools — builds what's missing
├── data/
│   ├── article_1.txt        # Article about semiconductor shortage
│   └── article_2.txt        # Similar article, different wording
├── tools/
│   └── word_count.py        # Pre-built tool (the one the agent already has)
└── requirements.txt
```

## How it works

Three meta-tools enable dynamic tool creation:

- **shell** — filesystem access, syntax validation, running tests
- **editor** — writes Python files to disk
- **load_tool** — registers a new tool into the agent's live registry at runtime

The system prompt provides structure: naming conventions, the `@tool` decorator template, and an ordered workflow (write → validate → test → load → retry).

## References

- [Strands Agents SDK](https://github.com/strands-agents/sdk-python)
- [Meta-Tooling Docs](https://strandsagents.com/docs/examples/python/meta_tooling/)
