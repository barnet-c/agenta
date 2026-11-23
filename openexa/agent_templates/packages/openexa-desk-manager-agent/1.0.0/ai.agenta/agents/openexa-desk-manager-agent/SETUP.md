# Setting up Desk Manager Agent

Part of the OpenEXA team: **Fund desk**, Orchestration.

## Model

Use **gpt-5.6-luna** (openai) on the **Pi** harness. The project needs that provider connected in Settings > Providers & Models.

## Permissions

The OpenEXA team runs this agent with the runner set to **allow_reads** (allow reads, ask before anything that changes something). Set the same in the agent's settings after you create it.

## Agents it hands work to

Create these agents from their OpenEXA templates first, then add each one to this agent as an agent tool:

- Data Health Agent
- Portfolio Manager Agent
- Risk Manager Agent
- Compliance Agent
- IBIT Arbitrage Trader
- Operations and Settlement Agent
- Ledger Auditor
- Project Manager Agent
