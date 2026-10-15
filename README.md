# AI Agent Harness

**The execution layer behind Chals AI’s assistant**

*A Chals AI case study — built by Ignacio Soler.*

<a id="the-project"></a>

I built the execution layer that connects an AI assistant to skills, tools and application capabilities. It manages which tools are available, how calls are dispatched, how context is assembled and how execution handles failures and retries.

I built this project end to end on my own, using AI tools for all programming. My work covered product definition, technical decisions, implementation, integration and validation.

[Watch the agent](#watch-the-agent) · [Explore the implementation](#explore-the-implementation) · [Run the component sample](#run-the-component-sample) · [Español](docs/LEEME.md)

## What I built

- Skill loading, capability controls and tool dispatch.
- Context-budget handling and prompt-cache key construction.
- Recovery logic and persistent execution events.

**Status:** Implemented during May–July 2026 as part of an earlier Chals AI product generation.

## Watch the agent

**Chals AI — AI Assistant for Google Sheets.** This product video shows the assistant inside Google Sheets. The technical material below focuses on selected components of the agent implementation.

[![Play Chals AI — AI Assistant for Google Sheets](https://i.ytimg.com/vi/Oo4Bd8iGeUY/hqdefault.jpg)](https://www.youtube.com/watch?v=Oo4Bd8iGeUY)

[Watch on YouTube](https://www.youtube.com/watch?v=Oo4Bd8iGeUY) · [Media provenance](docs/demos/manifest.json).

![AI Agent Harness illustrated architecture](docs/overview.svg)

## Explore the implementation

The runnable component contains the original local prompt-cache key builder. Selected source excerpts document the wider work: skill loading, tool dispatch, context management, recovery and event persistence.

| Entry | What to look at |
|---|---|
| [prompt_cache.py](source/prompt_cache.py) | Original executable component |
| [demo.py](demo.py) | Synthetic fixtures and 5 checked behaviors |
| [Architecture](docs/architecture.md) | The wider system and the sample boundary |
| [Design decisions](docs/decisions.md) | Tradeoffs with source links |
| [Code tour](docs/code-tour.md) | 8 selected excerpts from the wider construction |
| [Provenance](provenance.json) | Original paths, commits, hashes and documented redactions |

**Stack across the project:** Python · OpenAI Agents SDK · skills / tools · prompt caching · Firestore · Cloud Tasks.

This public case study includes selected original code and an isolated runnable sample with synthetic data. Production integrations and customer data remain private. Original paths, commits, hashes and redactions are recorded in [provenance.json](provenance.json).

<a id="run-the-sample"></a>

## Run the component sample

Run the original local prompt-cache key builder locally with synthetic data. Requires **Python 3.10+**, with no package installation or account setup.

```sh
git clone https://github.com/nasoler123/ai-agent-harness.git
cd ai-agent-harness
python3 -I demo.py
python3 verify.py
```

Expected observations:

- Repeated inputs and the same skill set in a different order keep the same key.
- Changing capabilities, channel or prompt content changes the key.
- The demo makes no model request and does not measure cache hit rate.

The sample runs offline and rejects network connections and external subprocesses. `verify.py` checks local links, instruction parity, the source hash, credential patterns and the recorded results of the component checks. [Recorded local results](verification.json).

## More from Chals AI

These projects cover my work across business automation, financial software, AI agents and data infrastructure.

[Data Platform and MCP](https://github.com/nasoler123/data-platform-mcp) · [Financial Modeling SaaS](https://github.com/nasoler123/financial-modeling-saas) · [Invoice Automation](https://github.com/nasoler123/invoice-automation)

[Ignacio Soler](https://github.com/nasoler123) · [LinkedIn](https://www.linkedin.com/in/ignacio-soler-esteban/)
