# HyperLake MCP server.
# Installs the published hyperlake CLI from npm and serves MCP over stdio.
FROM node:22-bookworm-slim

ARG HYPERLAKE_VERSION=0.2.9

RUN apt-get update \
    && apt-get install -y --no-install-recommends ca-certificates \
    && rm -rf /var/lib/apt/lists/* \
    && npm install -g "@cerebrixos/hyperlake@${HYPERLAKE_VERSION}" \
    && npm cache clean --force \
    && hyperlake version

USER node
WORKDIR /home/node

# Required at runtime: HYPERLAKE_HOST and HYPERLAKE_API_KEY (or HYPERLAKE_ACCESS_TOKEN).
ENTRYPOINT ["hyperlake", "mcp", "serve", "--stdio"]
