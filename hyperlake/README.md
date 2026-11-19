# HyperLake MCP Server

**Run your data lake from Claude, Cursor, VS Code and any MCP client.**

HyperLake is a managed data lake and AI-infrastructure platform. The HyperLake
MCP server lets an AI assistant work with your HyperLake account: query
clusters with SQL, explore catalogs, build dashboards, deploy governed apps,
manage credentials and access, and run monitors, all through your own
HyperLake permissions.

**Website:** [hyperlake.cloud](https://hyperlake.cloud) ·
**Docs:** [docs.hyperlake.cloud](https://docs.hyperlake.cloud/quickstart/mcp-client/) ·
**npm:** [`@cerebrixos/hyperlake`](https://www.npmjs.com/package/@cerebrixos/hyperlake) ·
**PyPI:** [`hyperlake`](https://pypi.org/project/hyperlake/)

> You need a HyperLake account to use this server.
> [Get started at hyperlake.cloud](https://hyperlake.cloud).

This repository contains documentation and client configuration for the
HyperLake MCP server. The server itself ships in the `hyperlake` CLI, which is
distributed through npm and PyPI.

## What you can do

| Area | Examples |
| --- | --- |
| **SQL and data exploration** | List clusters, catalogs, schemas and tables. Run SQL against a cluster. |
| **Dashboards** | Draft a dashboard from SQL, preview, validate, publish and run it locally. |
| **Catalogs and credentials** | Create catalogs, discover the fields each adapter needs, manage vault credentials and external secret stores. |
| **Access control** | Grant, update and revoke catalog access. Manage app collaborators and access requests. |
| **Clusters and networking** | Check cluster status and configuration, update IP allowlists, and set up new AWS clusters. |
| **Apps and Kubernetes actions** | Browse app definitions and versions, preview and deploy governed Helm apps, run approved Kubernetes actions. |
| **Observability** | Query logs and metrics with read-only SQL. Diagnose a cluster. |
| **Monitors** | Create, run and review governed data monitors and their run history. |
| **Semantic data lake** | Turn a natural-language question into reviewed semantic SQL against your metrics and dimensions. |
| **Agents** | Create, validate and chat with HyperLake Agents. Talk to other agents over A2A. |
| **FinOps** | Estimate query risk and inspect warehouse usage. |

See [TOOLS.md](TOOLS.md) for the full tool list. Every tool runs with the
permissions of the signed-in HyperLake user. Actions that change
infrastructure require explicit confirmation.

## Hosted connector (no install)

Claude, ChatGPT and other clients that support remote MCP servers can connect
to the hosted HyperLake connector instead of running anything locally:

```text
https://mcp.hyperlake.cloud/hyperlake-mcp
```

Add it as a custom connector, choose your HyperLake tenant, sign in and
approve the `hyperlake:mcp` scope. Each connection is bound to one tenant and
runs with that user's HyperLake permissions. The hosted connector offers a
reviewed subset of the tools: account and cluster status, catalogs, apps,
agents and catalog access policy. It does not include SQL execution, cluster
tokens or any delete tool. See [TOOLS.md](TOOLS.md). Disconnect at any time
from your HyperLake account to revoke its tokens.

## Quick start (local server)

1. Get your HyperLake **host** (your tenant URL, shown as
   `https://your-tenant.example.com` below) and an **API key** from your
   HyperLake account.
2. Add the server to your MCP client using one of the configurations below.
3. Ask your assistant something like *"List my HyperLake clusters and show the
   tables in the sales catalog."*

The server needs Node.js 20 or later when you run it through `npx`. No other
install step is needed: `npx` downloads the `hyperlake` binary on first run.

### Configuration

| Environment variable | Required | Description |
| --- | --- | --- |
| `HYPERLAKE_HOST` | Yes | Your HyperLake tenant URL, including `https://`. |
| `HYPERLAKE_API_KEY` | Yes, or an access token | Your HyperLake API key. |
| `HYPERLAKE_ACCESS_TOKEN` | Alternative to API key | An OAuth access token. |
| `HYPERLAKE_EMAIL` | No | The email of the HyperLake user. |

You can skip the environment variables by signing in once with the CLI. The
server then reads the saved configuration:

```bash
npx -y @cerebrixos/hyperlake@latest auth login \
  --host https://your-tenant.example.com \
  --email you@example.com \
  --api-key YOUR_API_KEY
```

## Client setup

### Claude Desktop

Add this to `claude_desktop_config.json`
(Settings → Developer → Edit Config):

```json
{
  "mcpServers": {
    "hyperlake": {
      "command": "npx",
      "args": ["-y", "@cerebrixos/hyperlake@latest", "mcp", "serve", "--stdio"],
      "env": {
        "HYPERLAKE_HOST": "https://your-tenant.example.com",
        "HYPERLAKE_API_KEY": "YOUR_API_KEY"
      }
    }
  }
}
```

### Claude Code

```bash
claude mcp add hyperlake \
  --env HYPERLAKE_HOST=https://your-tenant.example.com \
  --env HYPERLAKE_API_KEY=YOUR_API_KEY \
  -- npx -y @cerebrixos/hyperlake@latest mcp serve --stdio
```

### Cursor

Add this to `~/.cursor/mcp.json`, or to `.cursor/mcp.json` in a project:

```json
{
  "mcpServers": {
    "hyperlake": {
      "command": "npx",
      "args": ["-y", "@cerebrixos/hyperlake@latest", "mcp", "serve", "--stdio"],
      "env": {
        "HYPERLAKE_HOST": "https://your-tenant.example.com",
        "HYPERLAKE_API_KEY": "YOUR_API_KEY"
      }
    }
  }
}
```

### VS Code (GitHub Copilot agent mode)

Add this to `.vscode/mcp.json`. VS Code prompts for the API key and stores it
securely.

```json
{
  "inputs": [
    {
      "type": "promptString",
      "id": "hyperlake-api-key",
      "description": "HyperLake API key",
      "password": true
    }
  ],
  "servers": {
    "hyperlake": {
      "type": "stdio",
      "command": "npx",
      "args": ["-y", "@cerebrixos/hyperlake@latest", "mcp", "serve", "--stdio"],
      "env": {
        "HYPERLAKE_HOST": "https://your-tenant.example.com",
        "HYPERLAKE_API_KEY": "${input:hyperlake-api-key}"
      }
    }
  }
}
```

### Windsurf, Cline and other clients

Any client that launches a local MCP server can use the same command:

```text
npx -y @cerebrixos/hyperlake@latest mcp serve --stdio
```

Set `HYPERLAKE_HOST` and `HYPERLAKE_API_KEY` in the client's environment
settings. Ready-to-copy files for each client are in [`examples/`](examples).

### OpenAI Codex CLI

Add this to `~/.codex/config.toml`:

```toml
[mcp_servers.hyperlake]
command = "npx"
args = ["-y", "@cerebrixos/hyperlake@latest", "mcp", "serve", "--stdio"]
env = { HYPERLAKE_HOST = "https://your-tenant.example.com", HYPERLAKE_API_KEY = "YOUR_API_KEY" }
```

### Docker

```bash
docker build -t hyperlake-mcp .
docker run -i --rm \
  -e HYPERLAKE_HOST=https://your-tenant.example.com \
  -e HYPERLAKE_API_KEY=YOUR_API_KEY \
  hyperlake-mcp
```

Client configuration for the Docker image:

```json
{
  "mcpServers": {
    "hyperlake": {
      "command": "docker",
      "args": ["run", "-i", "--rm", "-e", "HYPERLAKE_HOST", "-e", "HYPERLAKE_API_KEY", "hyperlake-mcp"],
      "env": {
        "HYPERLAKE_HOST": "https://your-tenant.example.com",
        "HYPERLAKE_API_KEY": "YOUR_API_KEY"
      }
    }
  }
}
```

### Local HTTP (Streamable HTTP)

For clients that connect to a URL instead of launching a process:

```bash
npx -y @cerebrixos/hyperlake@latest mcp serve --http
```

The server listens on `http://127.0.0.1:8787/mcp`. It binds to loopback only,
validates browser origins and does not log MCP payloads. Binding to another
address requires `--allow-remote` and a bearer token; see
`hyperlake mcp serve --help`.

## Other ways to install

```bash
# npm (global)
npm install -g @cerebrixos/hyperlake

# Python
pip install hyperlake
```

After a global install, use `hyperlake mcp serve --stdio` as the command, and
run `hyperlake mcp config --format json-stdio` to print a ready-to-paste
configuration with the absolute binary path.

## Security

- The local server runs on your machine and talks only to your HyperLake host. The hosted connector authenticates with OAuth (PKCE) and sealed, tenant-bound tokens.
- Your API key or access token comes from environment variables or your local
  HyperLake configuration file and is not included in tool output. Tools that
  connect to a cluster use short-lived cluster tokens.
- Every tool call runs with your HyperLake user's permissions.
- Tools that change infrastructure, access or credentials require explicit
  confirmation.

Report security issues to the HyperLake team through
[hyperlake.cloud](https://hyperlake.cloud).

## Support

- Product and account: [hyperlake.cloud](https://hyperlake.cloud)
- Documentation: [docs.hyperlake.cloud](https://docs.hyperlake.cloud/quickstart/mcp-client/)
- Issues with this repository: open a GitHub issue.

## License

The documentation and configuration examples in this repository are licensed
under the [MIT License](LICENSE). The `hyperlake` CLI and HyperLake service are
provided by CerebrixOS under their own terms.
