# Design decisions

[Project](../README.md) · [Architecture](architecture.md) · [Code tour](code-tour.md)

## Load capabilities explicitly

Registry validation detects co-loading cycles; the session exposes only tools allowed by the current active surface. [Inspect the source](../evidence/E13.md).

## Guard dispatch in code

An inactive tool produces a structured recovery path. Registration and write contracts are checked before reaching the handler. [Inspect the source](../evidence/E15.md).

## Check the context budget before sending

The budget gate estimates input, releases stale outputs, summarizes older history and returns a recoverable error if the request remains too large. [Inspect the source](../evidence/E16.md).

## Cache a stable prefix

The key includes channel, agent, template and skill profile. Ordering the same skill IDs differently does not change that profile. It is a provider request option, not a local conversation cache. [Inspect the source](../evidence/E17.md).

## Preserve event order across retries

Run events use transactional sequence allocation. The full worker and persistence services remain outside this sample. [Inspect the source](../evidence/E18.md).

