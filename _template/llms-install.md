# Installing the PRODUCT_TITLE MCP server

These steps are for AI agents (such as Cline) installing this server for a
user.

PRODUCT_TITLE is a hosted MCP server. There is nothing to install or run locally,
and no API key to ask for. The user signs in with OAuth in their browser the
first time the client connects.

## Prerequisites

- An MCP client that supports remote servers over Streamable HTTP with OAuth.
- The user needs a PRODUCT_TITLE account. If they have none, point them to https://PRODUCT_WEBSITE.

## Configuration

Add this entry to the MCP settings file:

```json
{
  "mcpServers": {
    "PRODUCT_SLUG": {
      "type": "streamableHttp",
      "url": "https://PRODUCT_MCP_URL"
    }
  }
}
```

Other clients:

- Claude Code: `claude mcp add --transport http PRODUCT_SLUG https://PRODUCT_MCP_URL`
- Claude and ChatGPT: add `https://PRODUCT_MCP_URL` as a custom connector.
- Cursor, VS Code and Windsurf: see the files in [examples/](examples).

## Verify

When the client first connects, a browser window opens. The user chooses
**Continue with CerebrixOS** and signs in. Then ask the client to list the server's tools; see
[TOOLS.md](TOOLS.md) for what to expect.

Do not ask the user for passwords or tokens, and do not put credentials in
the settings file.
