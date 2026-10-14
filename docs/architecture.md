# Architecture

[Project](../README.md) · [Design decisions](decisions.md) · [Code tour](code-tour.md)

## System built

```mermaid
flowchart LR
    A["Skill registry"] --> B
    B["Active session"] --> C
    C["Guarded dispatch"] --> D
    D["Trace / recovery"]
```

I assembled the agent and its skill session, registry and dispatch surface, with capability gates, concrete tool contracts, loop recovery, context-budget handling, prompt-cache options and durable run events.

## Runnable boundary

The executable sample checks the original local prompt-cache key builder. Skill loading, tool dispatch, budget management and event persistence are documented excerpts, not an independently bootable agent in this repository.

The local route is `synthetic fixture → original component → checked result`. [Read the component](../source/prompt_cache.py) and [run the fixture](../demo.py). The network is blocked before the component is imported.

## External dependencies of the full system

Python · OpenAI Agents SDK · skills / tools · prompt caching · Firestore · Cloud Tasks. The original product connects these components through shared runtime and account context. This repository preserves selected examples and a bounded local demonstration.
