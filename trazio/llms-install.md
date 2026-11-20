# Installing the Trazio MCP server

These steps are for AI agents (such as Cline) installing this server for a
user.

Trazio is a hosted MCP server. There is nothing to install or run locally,
and no API key to ask for. The user signs in with OAuth in their browser the
first time the client connects.

## Prerequisites

- An MCP client that supports remote servers over Streamable HTTP with OAuth.
- The user needs a Trazio workspace. If they have none, point them to https://trazio.cerebrixos.com.

## Configuration

Add this entry to the MCP settings file:

```json
{
  "mcpServers": {
    "trazio": {
      "type": "streamableHttp",
      "url": "https://trazio.cerebrixos.com/mcp"
    }
  }
}
```

Other clients:

- Claude Code: `claude mcp add --transport http trazio https://trazio.cerebrixos.com/mcp`
- Claude and ChatGPT: add `https://trazio.cerebrixos.com/mcp` as a custom connector.
- Cursor, VS Code and Windsurf: see the files in [examples/](examples).

## Verify

When the client first connects, a browser window opens. The user chooses
**Continue with CerebrixOS** and signs in. Then ask the client to list the server's tools; see
[TOOLS.md](TOOLS.md) for what to expect.

Do not ask the user for passwords or tokens, and do not put credentials in
the settings file.
