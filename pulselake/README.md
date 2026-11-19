# Pulselake MCP Server

**Create and review AI surveys, and chat with Agent Copilots, from Claude,
ChatGPT, Cursor, VS Code and any MCP client.**

Pulselake Experience Ops lets an AI assistant work with your Pulselake
account: discover projects, queue AI survey creation, read survey links,
submissions and respondents, and chat with the Agent Copilots you can access.
Every tool runs with your own Pulselake permissions, in your tenant only.

**Website:** [pulselake.co](https://pulselake.co)

> You need a Pulselake account. [Get started at pulselake.co](https://pulselake.co).

This repository contains documentation and client configuration. The server
ships in the `pulselake` CLI.

## What you can do

| Area | Examples |
| --- | --- |
| **Projects** | List the Experience Ops projects you can see. |
| **Surveys** | Discover enabled project types, queue an AI survey, wait for the job, read the survey, its links, submissions and respondents. |
| **Agent Copilots** | List and inspect Agents, chat with them, list and upload conversation files, and manage a conversation's project scope. |

See [TOOLS.md](TOOLS.md) for the full tool list.

### Example prompts

- *"List my Pulselake projects, then show me my five most recent surveys."*
- *"Create a customer satisfaction survey for our onboarding project. Show me
  the enabled project types first."*
- *"How many completed submissions does the onboarding survey have? Show me
  the answers to question 3."*
- *"Chat with my support Agent and ask what it knows about refund requests."*

## Local server

The local server needs your Pulselake host and a user API key.

| Environment variable | Required | Description |
| --- | --- | --- |
| `PULSELAKE_HOST` | Yes | Your Pulselake URL, including `https://`. |
| `PULSELAKE_API_KEY` | Yes | Your Pulselake user API key. |

```json
{
  "mcpServers": {
    "pulselake": {
      "command": "npx",
      "args": ["-y", "@cerebrixos/pulselake-experience@latest", "mcp", "serve", "--stdio"],
      "env": {
        "PULSELAKE_HOST": "https://YOUR_HOST",
        "PULSELAKE_API_KEY": "YOUR_USER_KEY"
      }
    }
  }
}
```

Or sign in once and let the CLI store your session:

```bash
pulselake auth login --host https://YOUR_HOST --email YOU --api-key YOUR_USER_KEY
pulselake mcp serve --stdio
```

Ready-to-copy files for Claude Desktop, Cursor, VS Code and Cline are in
[`examples/`](examples). `pulselake mcp config --format json-stdio` prints a
configuration with the absolute binary path.

> The npm package `@cerebrixos/pulselake-experience` is released after
> registry publication succeeds. Until then, download the
> `pulselake_VERSION_OS_ARCH` archive from the CLI releases.

## Hosted connector

Connect directly, with no install. Sign-in uses OAuth: you choose your
Pulselake workspace, sign in there and approve access.

```text
https://mcp.pulselake.co/pulselake-experience-mcp
```

In Claude, open Settings, then Connectors, then **Add custom connector**, and
paste the URL. In Claude Code:

```bash
claude mcp add --transport http pulselake https://mcp.pulselake.co/pulselake-experience-mcp
```

The hosted connector accepts files of up to 512 KiB for conversation uploads
and does not read the server's filesystem.

## Security and privacy

- Every tool call uses the signed-in user's permissions. Cluster and source
  credentials cannot access surveys or project discovery.
- Credentials are sent only in request headers and never appear in tool
  output.
- `pulselake_list_survey_submitters` returns respondent names and emails.
  Anonymous respondents are returned as null.
- Tools that create surveys, send chat messages, upload files or change a
  conversation's project scope act only when you ask for them.

## Support

- Product and account: [pulselake.co](https://pulselake.co)
- Email: vc@pulselake.co
- Privacy policy: [pulselake.co/privacy](https://www.pulselake.co/privacy)
  and terms: [pulselake.co/terms](https://www.pulselake.co/terms)
- Issues with this repository: open a GitHub issue.

## License

The documentation and configuration examples in this repository are licensed
under the [MIT License](LICENSE). The `pulselake` CLI and Pulselake service are
provided by CerebrixOS under their own terms.
