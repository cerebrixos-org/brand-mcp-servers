# Directory listings

Where each server is listed. Update this file when a listing goes live or changes. Checked 20 November 2026.

Status: **live**, **submitted** (waiting on review), **ready** (text prepared in [listings/](listings), not sent), **auto** (copied from the official MCP Registry once the server is published there), **n/a**.

| Directory | How to get listed | Who submits | HyperLake | PulseLake Experience Ops | Trazio | Forward Deployed | Watchtower |
| --- | --- | --- | --- | --- | --- | --- | --- |
| [Official MCP Registry](https://registry.modelcontextprotocol.io) | `server.json`, published with the [Publish to MCP Registry](.github/workflows/publish-mcp-registry.yml) workflow | Workflow, run by hand | live | live | live | live (`work.forwardeployed/forward-deployed`) | live |
| [GitHub MCP Registry](https://github.com/mcp) | Official registry entry, then an onboarding request in the github-mcp-server discussions | Owner (GitHub account) | after registry | after registry | after registry | ready | after registry |
| [Glama](https://glama.ai/mcp/connectors) | Add the connector URL, then claim it with `glama.json` or the Glama claim token | Owner (Glama account) | ready | ready | ready | ready | ready |
| [awesome-remote-mcp-servers (punkpeye)](https://github.com/punkpeye/awesome-remote-mcp-servers) | Pull request; needs a Glama connector badge first | PR | after Glama | after Glama | after Glama | after Glama | after Glama |
| [awesome-remote-mcp-servers (jaw9c)](https://github.com/jaw9c/awesome-remote-mcp-servers) | Pull request | PR | ready | ready | ready | ready | ready |
| [Docker MCP Catalog](https://hub.docker.com/mcp) | Pull request to docker/mcp-registry with `server.yaml`, `tools.json`, `readme.md` | PR | ready | ready | ready | ready | ready |
| [Cline MCP Marketplace](https://github.com/cline/mcp-marketplace) | Issue with repo link and 400 x 400 logo | Issue | ready | ready | ready | ready | ready |
| [Microsoft MCP Center](https://github.com/Azure/mcp-center) | Comment on issue #4 with server details | Issue comment | ready | ready | ready | ready | ready |
| [PulseMCP](https://www.pulsemcp.com) | Closed to submissions; imports from the official registry | none | auto | auto | auto | auto | auto |
| [mcp.directory](https://mcp.directory/submit) | Form with repo URL; also imports from the official registry | Owner | auto | auto | auto | auto | auto |
| [API Tracker](https://apitracker.io/mcp-servers) | Imports from the official registry | none | auto | auto | auto | auto | auto |
| [mcp.so](https://mcp.so/submit) | Web form (free queue, paid fast lane) | Owner | ready | ready | ready | ready | ready |
| [mcpservers.org](https://mcpservers.org/submit) | Web form (free queue, paid fast lane); also feeds wong2/awesome-mcp-servers | Owner | ready | ready | ready | ready | ready |
| [MCP Market](https://mcpmarket.com/submit) | Web form with repo URL (free queue, paid fast lane) | Owner | ready | ready | ready | ready | ready |
| [Smithery](https://smithery.ai/new) | Web form with the hosted URL; check status first, its gateway was reported shut down on 31 October 2026 | Owner (Smithery account) | check | check | check | check | check |
| [LobeHub](https://lobehub.com/mcp) | `lhm` CLI with browser sign-in | Owner | ready | ready | ready | ready | ready |
| [cursor.directory](https://cursor.directory) | Form with repo URL | Owner | ready | ready | ready | ready | ready |
| [Claude Connectors Directory](https://claude.com/docs/connectors/building/submission) | Product review: OAuth, tool annotations, privacy policy, icon, test account | Owner | later | later | later | later | later |
| [ChatGPT apps](https://developers.openai.com/apps-sdk) | Product review with verified publisher account | Owner | later | later | later | later | later |

Not used: `modelcontextprotocol/servers` (third-party list retired), `punkpeye/awesome-mcp-servers` (only servers whose source you can install; hosted servers go to the remote list), `wong2/awesome-mcp-servers` (takes no pull requests; use mcpservers.org), goose extensions (closed; uses the official registry), mcp-get (npm and PyPI packages only).

## CLIs

| CLI | Package | Runs the MCP server locally | Registry `packages` entry |
| --- | --- | --- | --- |
| HyperLake | [`@cerebrixos/hyperlake`](https://www.npmjs.com/package/@cerebrixos/hyperlake) | `hyperlake mcp serve --stdio` | Blocked: the package needs `"mcpName": "io.github.cerebrixos-org/hyperlake"` in its `package.json` |
| PulseLake Experience Ops | [`@cerebrixos/pulselake-experience`](https://www.npmjs.com/package/@cerebrixos/pulselake-experience) | `pulselake mcp serve --stdio` | Blocked: needs `"mcpName": "io.github.cerebrixos-org/pulselake"` |

Once a CLI release carries `mcpName`, add its `packages` block back to that product's `server.json` and publish a new version, so the registry and the directories that copy it show both the hosted and the local install.

