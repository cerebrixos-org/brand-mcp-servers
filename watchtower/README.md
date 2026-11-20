# Watchtower MCP Server

**Ask Claude, ChatGPT or any MCP client what needs attention across your code and clouds: security, cost, drift and change safety.**

Watchtower watches reliability, change safety, security and cost across your Azure, AWS and Google Cloud accounts and the repositories behind them, and reports what needs attention. The MCP server lets an AI assistant read your findings, reports and compliance assessments and start scans. Infrastructure only ever changes through a pull request a person merges; no MCP tool runs commands or opens a pull request on its own.

**Website:** [watchtower.cerebrixos.com](https://watchtower.cerebrixos.com) ·
**Privacy:** [cerebrixos.com/privacy](https://cerebrixos.com/privacy) ·
**Support:** support@cerebrixos.com

> You need a Watchtower workspace. Sign-up is installing the Watchtower GitHub App. [Get started](https://watchtower.cerebrixos.com).

## Connect

Hosted connector, one address for everyone, nothing to install:

```text
https://watchtower.cerebrixos.com/mcp
```

Add it as a custom connector in Claude or ChatGPT, sign in with GitHub or Microsoft, pick your workspace if you have more than one, and approve. In Claude Code:

```bash
claude mcp add --transport http watchtower https://watchtower.cerebrixos.com/mcp
```

Then run `/mcp`, pick `watchtower` and **Authenticate**. Configuration for other clients is in [examples/](examples).

## What you can do

| Area | Example prompt |
| --- | --- |
| Posture | Summarise Watchtower's status and anything high severity. |
| Scans | Start a security scan, wait for it, then compare it with the previous run. |
| Cost | Which FinOps findings are priced, and which are unpriced estimates? |
| Compliance | Run the SOC 2 assessment and list unknown controls with their missing evidence. |
| Change safety | What depends on this resource, and what would this pull request touch? |

An assessment is not a certification. Unavailable cost is reported as unavailable, never as $0.

## Access

| Signed in as | Access |
| --- | --- |
| GitHub organization owner or workspace administrator | Read findings, reports, assessments, costs and events; start scans and assessments |
| Microsoft member (billing owner or viewer) | Read only |
| Anyone else | Refused |

OAuth sign-in never grants approval of fixes, settings or key management. Tools outside the granted access are not listed. Every tool carries a title and read-only, destructive and open-world hints.

See [TOOLS.md](TOOLS.md) for the tool list.

Watchtower is part of Forward Deployed Solutions from CerebrixOS (Ockham Labs Inc.).
