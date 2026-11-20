# Awesome lists and product directories

Lists on GitHub and the web that take commercial products, CLIs or product sites, checked against each list's own rules on 20 November 2026. Every entry is one factual sentence, with no marketing words, as these lists require. Match the list's exact format and section ordering when you open the pull request.

## GitHub lists that accept commercial products

### SquadcastHub/awesome-sre-tools (about 1,500 stars)

Rules: no duplicates, add at the bottom of the section, no dead links, no marketing lingo in the PR. Pull request.

- Section "AI SRE Tools & SRE Copilots":
  `- [Watchtower](https://watchtower.cerebrixos.com) - Watches reliability, change safety, security and cost across Azure, AWS and Google Cloud accounts, and proposes fixes only as pull requests.`
- Section "Continuous Monitoring":
  `- [Trazio](https://trazio.cerebrixos.com) - One pipeline for logs, metrics, traces, security events, robot data and video, with read-only access for AI assistants over MCP.`

### agamm/awesome-ai-sre (about 150 stars)

Lists commercial AI SRE products next to open source ones. Pull request.

- Section "AI SRE Agents":
  `- [Watchtower](https://watchtower.cerebrixos.com) - Always-on agent for security, FinOps and drift findings across Azure, AWS and Google Cloud, where infrastructure changes only through a pull request a person merges.`
- Section "Observability Platforms":
  `- [Trazio](https://trazio.cerebrixos.com) - Logs, metrics, traces, security events, robot data and video in one pipeline, queried by your own AI assistant over MCP.`

### last9/awesome-sre-agents (about 100 stars)

Rules: AI agent with an SRE or DevOps use case, public URL, actively maintained, one factual sentence. Open source entries carry "(Open Source)", so ours carry nothing. Pull request.

- Section "SRE Agents":
  `- [Watchtower](https://watchtower.cerebrixos.com) - Scans Azure, AWS and Google Cloud accounts for security, cost and drift findings and opens fixes as pull requests for a person to merge.`

### gregoire-costory/awesome-agentic-finops (about 30 stars)

Rules: commercial tools allowed with the `vendor` tag and a genuine way to try them; factual, who it is for. Pull request.

- Section for MCP servers and AI cost agents:
  ``- [Watchtower](https://watchtower.cerebrixos.com) `vendor` - Scans Azure, AWS and Google Cloud accounts for cost, security and drift findings, with an MCP server at `https://watchtower.cerebrixos.com/mcp`; for platform and FinOps teams.``

### jmfontaine/awesome-finops (about 130 stars)

Has a "Commercial Tools" section. Format `[Name](Link) - Description.`, alphabetical, no leading "A" or "An", one pull request per suggestion.

- `- [Watchtower](https://watchtower.cerebrixos.com) - Cloud cost, security and drift scans across Azure, AWS and Google Cloud, with priced findings and fixes proposed as pull requests.`

### e2b-dev/awesome-ai-agents (about 31,000 stars)

Has a "Closed-source projects and companies" section. Submit by pull request or the list's Google Form, alphabetical order.

- `Forward Deployed` (https://forwardeployed.work): AI expert desk inside Claude, ChatGPT and other assistants for research, strategy, financial models and decks, with each job priced and approved before it runs.
- `Watchtower` (https://watchtower.cerebrixos.com): Always-on cloud operations agent for security, cost and drift across Azure, AWS and Google Cloud; changes only through pull requests.
- `Trazio` (https://trazio.cerebrixos.com): Security and observability data pipeline that your AI assistant investigates over MCP, read-only.
- `PulseLake` (https://pulselake.co): AI surveys, persona research and Agent Copilots, usable from AI assistants over MCP.

### toolleeo/awesome-cli-apps-in-a-csv (about 2,700 stars)

Issue with `name`, `homepage`, `git` (optional) and `description`. No open source rule is stated.

- `hyperlake`, https://hyperlake.cloud, description: `CLI for the HyperLake data lake: run SQL, manage catalogs and access policy, and serve an MCP server for AI assistants.`
- `pulselake`, https://pulselake.co, description: `CLI for PulseLake Experience Ops: create and review AI surveys, chat with Agent Copilots, and serve an MCP server.`

### adriannovegil/awesome-observability (about 750 stars)

No contributing rules; mostly open source but includes vendor platforms. Lower odds.

- Section "General Tools":
  `- [Trazio](https://trazio.cerebrixos.com) - Logs, metrics, traces, security events, robot data and video in one pipeline, with read-only MCP access for AI assistants.`

### samber/awesome-user-research (about 30 stars)

The Survey section lists commercial tools (Hotjar, Pendo, Refiner).

- Section "Survey":
  `- [PulseLake](https://pulselake.co) - AI-generated surveys and synthetic persona research, with submissions and Agent Copilots available to AI assistants over MCP.`

### More MCP lists (format: copy the list's existing entries)

Use the short descriptions from [web-forms.md](web-forms.md) and the endpoint URLs; mark every server as hosted with OAuth sign-in and an account needed.

- sylviangth/awesome-remote-mcp-servers: free and commercial welcome; state that each needs a paid or trial account.
- appcypher/awesome-mcp-servers, habitoai/awesome-mcp-servers, yzfly/Awesome-MCP-ZH: one line per server in the matching category.
- TensorBlock/awesome-mcp-servers: the repository's submit-server issue form, one per server.
- hashgraph-online/awesome-ai-plugins: Trazio, Watchtower and Forward Deployed as remote MCP plugins.

### jamesmurdza/awesome-ai-devtools

Lists proprietary tools; read its pull request template rules first.

- `- [Watchtower](https://watchtower.cerebrixos.com) — Comments on infrastructure pull requests with the live resources they touch, dependents and a risk score, and proposes cloud fixes as pull requests.`

### e2b-dev/awesome-ai-agents, also

- `Simulations` (https://simulations.cerebrixos.com): Decision simulation AI agent that runs synthetic persona research and multi-round world simulations before you commit to a decision.

## Skipped, and why

| List | Why not |
| --- | --- |
| sbilly/awesome-security, 4ndersonLin/awesome-cloud-security, kyrolabs/awesome-agents, slavakurilyak/awesome-ai-agents, igorbarinov/awesome-data-engineering | Open source projects only |
| wmariuss/awesome-devops | A tool without a public repository needs a website on a domain at least 6 months old; check each domain's age first |
| theopenlane/awesome-compliance | Only commercial platforms practitioners already recognize; no product landing pages |
| hesreallyhim/awesome-claude-code | GitHub resources with at least 100 stars, through an issue form |
| samber/awesome-olap | Commercial tools only if widely adopted |
| scadastrangelove/awesome-ai-security-tools | New or zero-star projects go to a watchlist first |
| rdmgator12/awesome-claude-connectors | Lists only connectors already in Anthropic's Claude directory; add ours after that listing |
| punkpeye/awesome-mcp-servers | Installable open source servers only |

## Web directories (need the owner's accounts)

Not checked in detail. Each takes a form with name, URL, one-line description, logo and category, and some charge for faster review: Product Hunt (one launch per product), There's An AI For That, Futurepedia, Toolify, AlternativeTo, SaaSHub, G2, Capterra, BetaList, DevHunt (developer tools: HyperLake CLI, Trazio, Watchtower).
