# Installing the Pulselake MCP server

These steps are for AI agents (such as Cline) installing this server for a
user.

## Preferred: hosted connector

If the client supports remote MCP servers with OAuth, add
`https://mcp.pulselake.co/pulselake-experience-mcp`. The user signs in through
the browser. No key or install is needed.

## Local server

Ask the user for their Pulselake host (an `https://` URL) and their user API
key. Do not guess either. If the user has no account, point them to
https://pulselake.co.

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

## Verify

Call `pulselake_list_projects`. It returns the first page of projects the user
can see.

## Notes

- Create a survey only when the user asks. Call `pulselake_survey_expected_fields`
  first to find an enabled project type.
- Survey submitters include names and emails. Treat them as personal data.
