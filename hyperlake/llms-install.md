# Installing the HyperLake MCP server

These steps are for AI agents (such as Cline) installing this server for a
user.

## Prerequisites

- Node.js 20 or later (`node --version`).
- A HyperLake account. Ask the user for:
  - their HyperLake host, the tenant URL including `https://`
  - their HyperLake API key

Do not guess either value. If the user has no account, point them to
https://hyperlake.cloud.

## Configuration

Add this entry to the MCP settings file and replace the two placeholder values
with what the user gave you:

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

The first run downloads the `hyperlake` binary through npm. No other install
step is needed.

## Verify

After the server starts, call `hyperlake_whoami`. It returns the signed-in
identity and cluster count. If it reports missing host or credentials, check
the two environment variables.

## Notes

- Tools that change infrastructure, access or credentials ask for explicit
  confirmation. Ask the user before setting `confirm` to `true`.
- The API key is not included in tool output. Never write it into chat or
  project files.
