# Setting up Operations and Settlement Agent

Part of the OpenEXA team: **Fund desk**, Stage 6 · Settle.

## Model

Use **sonnet** (anthropic) on the **Claude** harness. The project needs that provider connected in Settings > Providers & Models.

## Permissions

The OpenEXA team runs this agent with the runner set to **allow_reads** (allow reads, ask before anything that changes something). Set the same in the agent's settings after you create it.

## Who calls it

Desk Manager Agent hands work to this agent. After creating both, add this agent as a tool in Desk Manager Agent.
