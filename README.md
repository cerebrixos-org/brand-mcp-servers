# CerebrixOS MCP servers

Documentation, client configuration and registry entries for the Model Context Protocol (MCP) servers from CerebrixOS companies. Each product has its own folder. This repository holds documentation only; the servers run as hosted services or ship in each product's own CLI.

| Product | What it does | Hosted connector | Docs |
| --- | --- | --- | --- |
| HyperLake | Manage and query your data lake: clusters, catalogs, access policy, apps and agents | `https://mcp.hyperlake.cloud/hyperlake-mcp` | [hyperlake/](hyperlake) |
| PulseLake Experience Ops | Create and review AI surveys and chat with Agent Copilots | `https://mcp.pulselake.co/pulselake-experience-mcp` | [pulselake/](pulselake) |

Each hosted connector signs you in to your own tenant with OAuth and runs with your permissions. You need an account for the product.

## Layout

Every product folder contains `README.md`, `TOOLS.md`, `server.json` (the MCP Registry entry), `examples/` and, where relevant, install notes for AI agents.

## Adding a product

1. Copy an existing folder and rename it to the product.
2. Set `name`, `title`, `websiteUrl` and the `remotes` or `packages` in `server.json`, and set `repository.subfolder` to the folder name.
3. List only tools that exist in the hosted connector in `TOOLS.md`.
4. Add a row to the table above.

## Support and security

Support goes through each product's website. Report security issues privately to the owner of the product concerned; do not open a public issue.

## License

Documentation and examples are MIT licensed. The products themselves are provided under their own terms.
