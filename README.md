# Public Records Dify plugin

**Author:** Public Records  
**Version:** 0.0.1  
**Type:** Tool  
**Source repository:** https://github.com/GeminiGeorge22/publicrecords-dify-plugin  
**Contact:** mark-merchand-zs9fmg@mail.grokbot.com

**Try it, tell us, and star it if it helped.** Run any Public Records Actor on your own Apify account, then [leave feedback](https://github.com/GeminiGeorge22/publicrecords-mcp/blob/main/BETA.md). A star is welcome if this repo saved you time. Stars are optional and are never rewarded.

See also [publicrecords-mcp](https://github.com/GeminiGeorge22/publicrecords-mcp) (MCP servers) and [publicrecords-skills](https://github.com/GeminiGeorge22/publicrecords-skills) (Agent Skills).

A Dify tool plugin that runs [Public Records](https://apify.com/publicrecords) Apify Actors from a Chatflow, Workflow, or Agent. It calls the official Apify API with **the end user's own Apify API token**, entered as a plugin credential. The plugin never ships a token and never uses a shared or built-in credential. Actor runs are billed to that user's Apify account.

## Setup

1. Install the plugin in Dify (Marketplace, or install from the `.difypkg` in a self-hosted workspace).
2. Open the plugin credentials and paste **your own** Apify API token. Create one in the [Apify Console](https://console.apify.com/settings/integrations) under Settings → Integrations.
3. Save. Dify validates the token with `GET https://api.apify.com/v2/users/me`.
4. Add the tools to a Chatflow, Workflow, or Agent.

You need an Apify account (the free plan is enough to start) and a Dify Cloud or Community Edition workspace. Outbound HTTPS to `https://api.apify.com` must be allowed.

## Credentials

| Credential | Required | Where to get it |
| --- | --- | --- |
| Apify API token | Yes | [Apify Console → Settings → Integrations](https://console.apify.com/settings/integrations) |

Use only a token you own. Do not put a token in Actor input, in this repository, or in a workflow export.

## Usage

Three tools are provided:

- **List Public Records Actors** — returns the allowlisted Actor ids, short descriptions, and Store URLs. Call this first when you need an id.
- **Run a Public Records Actor** — starts one allowlisted Actor with a JSON input object, optionally waits for it to finish (default 90 seconds, maximum 150), and returns the default dataset items on success.
- **Get Apify dataset items** — reads items from a dataset id, typically `default_dataset_id` from a previous run.

Only allowlisted `publicrecords/*` Actors can be started. The plugin talks only to `https://api.apify.com`.

### Example: run Grants.gov

After the credential is saved, call **Run a Public Records Actor** with:

- Actor: `publicrecords/grants-gov-scraper`
- Actor input JSON: `{"query":"education","maxItems":20}`
- Wait for finish: `90`

Input fields differ by Actor. See the Store page linked by **List Public Records Actors**, or the pages under https://apify.com/publicrecords.

### Allowlisted Actors

The catalog covers 18 Public Records Actors, including job boards, government tenders and grants, marketplace data, ads transparency, sports odds, and tennis scores. Store URLs follow `https://apify.com/publicrecords/<actor>`.

Remote MCP endpoints (where an Actor also ships as MCP) follow `https://mcp.apify.com?tools=publicrecords/<actor>` and are listed by the list-actors tool. They are not required to use this Dify plugin.

## Connection requirements

- HTTPS to `https://api.apify.com`
- A valid Apify API token belonging to the Dify user who installs the plugin
- Python 3.12 runtime (provided by Dify's plugin runner)

## Development

```bash
# Python 3.12
python3.12 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Package for the Dify Marketplace (produces a `.difypkg` next to this directory):

```bash
dify-plugin plugin package .
```

## Security and privacy

See [PRIVACY.md](./PRIVACY.md). Tokens are sent only to the Apify API and are not logged by this plugin.

## License

MIT. Copyright (c) 2026 publicrecords
