# Setting up IBIT Create/Redeem Analyst

Part of the OpenEXA team: **Fund desk**, Stage 1 · Signal.

## Model

Use **gpt-5.6-luna** (openai) on the **Pi** harness. The project needs that provider connected in Settings > Providers & Models.

## Permissions

The OpenEXA team runs this agent with the runner set to **allow_reads** (allow reads, ask before anything that changes something). Set the same in the agent's settings after you create it.

## OpenEXA tools

This agent reads OpenEXA data through the OpenEXA MCP server. In Settings > MCPs, connect `https://app.openexa.com/api/mcp` with the header `Authorization` set to the OpenEXA MCP key, then add the OpenEXA MCP to this agent.

## Who calls it

Portfolio Manager Agent hands work to this agent. After creating both, add this agent as a tool in Portfolio Manager Agent.
