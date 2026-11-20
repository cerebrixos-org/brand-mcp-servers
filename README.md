# CerebrixOS MCP servers

Documentation, client configuration and registry entries for the Model Context Protocol (MCP) servers from CerebrixOS companies. Each product has its own folder. This repository holds documentation only; the servers run as hosted services or ship in each product's own CLI.

| Product | What it does | Hosted connector | Docs |
| --- | --- | --- | --- |
| HyperLake | Manage and query your data lake: clusters, catalogs, access policy, apps and agents | `https://mcp.hyperlake.cloud/hyperlake-mcp` | [hyperlake/](hyperlake) |
| PulseLake Experience Ops | Create and review AI surveys and chat with Agent Copilots | `https://mcp.pulselake.co/pulselake-experience-mcp` | [pulselake/](pulselake) |
| Trazio | Ask your AI assistant about your logs, traces, security events, robot runs and video. Read-only | `https://trazio.cerebrixos.com/mcp` | [trazio/](trazio) |
| Forward Deployed | Research, strategy, financial models and decks, priced and approved per job | `https://forwardeployed.work/mcp` | [cerebrixos/](cerebrixos) |

Each hosted connector signs you in to your own tenant with OAuth and runs with your permissions. You need an account for the product.

## Layout

Every product folder contains:

| File | Used by |
| --- | --- |
| `README.md` | Every directory; the listing page text |
| `TOOLS.md` | Readers and reviewers; list only tools the hosted connector exposes |
| `server.json` | The official MCP Registry, and the directories that copy from it |
| `glama.json` | Glama, to claim the listing |
| `llms-install.md` | Cline and other agents that install servers for a user |
| `icon.png` | 400 x 400 logo for Cline, Claude and other directories |
| `examples/` | Client configuration for Cursor, VS Code, Cline, Windsurf and others |

[LISTINGS.md](LISTINGS.md) tracks which directories list each server, and [listings/](listings) holds the text to paste into each directory's form or pull request.

## Adding a product

1. Copy [`_template/`](_template) to a folder named after the product and replace every `PRODUCT_*` placeholder.
2. In `server.json`, set `name`, `title`, `description` (100 characters at most), `websiteUrl`, `version` and the `remotes` URL, and set `repository.subfolder` to the folder name.
3. List only tools that exist in the hosted connector in `TOOLS.md`.
4. Add a 400 x 400 `icon.png`.
5. Add a row to the table above, a column to [LISTINGS.md](LISTINGS.md) and an entry to each file in [listings/](listings).

## Support and security

Support goes through each product's website. Report security issues privately to the owner of the product concerned; do not open a public issue.

## License

Documentation and examples are MIT licensed. The products themselves are provided under their own terms.
