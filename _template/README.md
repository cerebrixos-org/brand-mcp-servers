# PRODUCT_TITLE MCP Server

**PRODUCT_HEADLINE: one sentence on what someone can ask their AI assistant to do.**

PRODUCT_INTRO: two or three sentences. Say what the server can and cannot do (read-only or not) and whose permissions it runs with.

**Website:** [PRODUCT_WEBSITE](https://PRODUCT_WEBSITE) ·
**Privacy:** [privacy policy](https://PRODUCT_WEBSITE/privacy) ·
**Support:** support@cerebrixos.com

> You need a PRODUCT_TITLE account. [Get started](https://PRODUCT_WEBSITE).

## Connect

Hosted connector, nothing to install:

```text
https://PRODUCT_MCP_URL
```

Add it as a custom connector in Claude or ChatGPT and sign in. In Claude Code:

```bash
claude mcp add --transport http PRODUCT_SLUG https://PRODUCT_MCP_URL
```

Configuration for other clients is in [examples/](examples).

## What you can do

| Area | Example prompt |
| --- | --- |
| PRODUCT_AREA | PRODUCT_EXAMPLE_PROMPT |

See [TOOLS.md](TOOLS.md) for the full tool list.
