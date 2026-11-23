# OpenEXA agent-team templates

Templates for Agenta's Templates gallery ("Agent Marketplace"), one per agent in the OpenEXA agent team, shown
under the category **OpenEXA Agent Team** next to Agenta's own templates (which stay unchanged).

| Path | What it holds |
| --- | --- |
| `agent_templates/catalog.json` | One record per template (keys start with `openexa-` so they never collide with Agenta's). |
| `agent_templates/authors/openexa.json` | The OpenEXA author shown on the cards. |
| `agent_templates/packages/<key>/1.0.0/` | Each template: `plugin.json`, `ai.agenta/agents.json`, `AGENTS.md` (instructions), `SETUP.md` (model, permissions, OpenEXA tools, which agents it calls), and its skills. |
| `merge_templates.py` | Appends these templates to Agenta's bundled catalog (standard library only). |

This folder is not used by Agenta on its own. To serve it, the VM:

1. runs `python3 openexa/merge_templates.py api/oss/src/resources/agent_templates/catalog.json openexa/agent_templates/catalog.json <merged catalog.json>` after each update, and
2. mounts into the `api` container (read-only): the merged `catalog.json` over `/app/oss/src/resources/agent_templates/catalog.json`, `agent_templates/authors/openexa.json` at `.../agent_templates/authors/openexa.json`, and `agent_templates/packages` at `.../agent_templates/openexa/packages`.

The templates are generated from the agent team in the OpenEXA app repo (`agents/` and `agents/registry.json`);
regenerate them rather than editing by hand, and give a changed template a new version folder.
