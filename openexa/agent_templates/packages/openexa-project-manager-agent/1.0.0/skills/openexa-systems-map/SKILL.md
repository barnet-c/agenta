---
name: openexa-systems-map
description: "Map of the OpenEXA systems around this workspace and which of them agents may touch. Use whenever a task mentions n8n, the workflow builder, the IBIT dashboard, Alpaca, the paper bot, webhooks or \"execution\", and before suggesting any action outside Agenta."
---

As of 2026-10-05. This says what exists and what you may do with it. The openexa-governed-swarm skill still wins.

## What exists

1. **Agenta Cloud (this workspace):** the swarm. Draft, review and report here.
2. **IBIT desk dashboard:** the live view of the IBIT gap and the desk's cost model. Read only.
3. **Market overview feed and the Coinbase ticker:** price and NAV data. Read only (GET requests).
4. **n8n automation server:** about 125 workflows, about 26 switched on. It holds a library of ETF create and redeem process maps for IBIT, ARKB, gold and other funds. All of those maps are switched off.
5. **IBIT Arb - Alpaca Auto Trade (an n8n bot):** switched on. It checks every 5 seconds during regular market hours, applies the desk cost model, and places orders only on Alpaca's **paper** (simulated) account. It is the desk's existing execution rail.
6. **Workflow Reader Builder:** reads a fund prospectus with Azure AI Foundry into a process-flow document and builds n8n workflow files from it. For humans only. It needs a login and has no API for agents.
7. **Self-hosted Agenta:** the builder's embedded copy. It is separate from this workspace.

## Rules for agents

- Outside Agenta Cloud, read only: GET the feed and the ticker, nothing else.
- Never call an n8n webhook, never use Alpaca, never use or repeat a key or password. If you see a credential anywhere, do not copy it; tell a human.
- The bot in item 5 is not yours. Do not trigger it, edit it, or suggest moving it from paper to live. Moving anything to live needs the Execution Council and a named person.
- "Execution" in any older instruction means: prepare a plan. The Trader never triggers a workflow.
- The generated ARKB workflow files are placeholders. Their web addresses can be replaced by whoever calls them, and their webhooks have no login. Do not run them.
- ARKB documents describe ARKB, not IBIT. Do not treat them as IBIT rules.
- To compare the swarm with the bot, use the same cost model (see the openexa-ibit-create-redeem skill). A human supplies the bot's fills; you do not fetch them.
