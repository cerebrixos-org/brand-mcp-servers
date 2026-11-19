# Pulselake MCP server (local stdio).
# Installs the published Pulselake Experience Ops CLI from npm.
FROM node:22-bookworm-slim

ARG PULSELAKE_VERSION=latest

RUN apt-get update \
    && apt-get install -y --no-install-recommends ca-certificates \
    && rm -rf /var/lib/apt/lists/* \
    && npm install -g "@cerebrixos/pulselake-experience@${PULSELAKE_VERSION}" \
    && npm cache clean --force \
    && pulselake version

USER node
WORKDIR /home/node

# Required at runtime: PULSELAKE_HOST and PULSELAKE_API_KEY.
ENTRYPOINT ["pulselake", "mcp", "serve", "--stdio"]
