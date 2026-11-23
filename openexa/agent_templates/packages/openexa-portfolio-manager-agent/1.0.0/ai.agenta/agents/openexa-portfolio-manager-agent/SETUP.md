# Setting up Portfolio Manager Agent

Part of the OpenEXA team: **Fund desk**, Stage 3 · Decide.

## Model

Use **opus[1m]** (anthropic) on the **Claude** harness. The project needs that provider connected in Settings > Providers & Models.

## Permissions

The OpenEXA team runs this agent with the runner set to **allow_reads** (allow reads, ask before anything that changes something). Set the same in the agent's settings after you create it.

## OpenEXA tools

This agent reads OpenEXA data through the OpenEXA MCP server. In Settings > MCPs, connect `https://app.openexa.com/api/mcp` with the header `Authorization` set to the OpenEXA MCP key, then add the OpenEXA MCP to this agent.

## Agents it hands work to

Create these agents from their OpenEXA templates first, then add each one to this agent as an agent tool:

- Regime Agent
- Strategy Agent
- IBIT Create/Redeem Analyst
- ARKB Analyst
- FBTC Analyst
- Gold/IAU Analyst
- Filing Analyst

## Who calls it

Desk Manager Agent hands work to this agent. After creating both, add this agent as a tool in Desk Manager Agent.
