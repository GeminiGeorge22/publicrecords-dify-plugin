# Privacy Policy

This plugin ("Public Records") is published by Public Records so you can run Public Records Apify Actors from Dify.

## Data collection

- The plugin requires **your own Apify API token**. It does not ship with, use, or fall back to a shared token.
- The plugin does not collect accounts, contact details, or analytics for Public Records.
- Tool arguments you enter (Actor input JSON, dataset ids, and limits) are sent only to complete the API call you requested.

## Data usage

- Your Apify API token is used solely to authenticate HTTPS requests to the official Apify API (`https://api.apify.com`).
- Actor input you provide is sent to Apify as the input of an allowlisted Public Records Actor. Runs are billed to **your** Apify account.
- Dataset reads use the same token to fetch items from an Apify dataset id you supply.
- The plugin does not send your token or tool arguments to Public Records, or to any host other than `api.apify.com`.

## Data storage

- The plugin does not persist tokens, run results, or other user data outside the Dify runtime that hosts the plugin.
- Dify stores plugin credentials in your Dify workspace according to Dify's own policies.
- Run output is stored in your Apify account (runs and datasets) according to Apify's policies.

## Data sharing

- No data is shared with Public Records or other third parties by this plugin.
- Public Records Actors may return public-web data (for example job listings, tenders, or marketplace search results) into your Dify app when a run succeeds.

## User responsibility

- You are responsible for safeguarding your Apify API token and for usage billed to your Apify account.
- Do not paste someone else's token. Revoke the token in the Apify Console if you suspect unauthorized use.
- Review each Actor's Store page and input before you run it.

## Contact

Questions about this policy: mark-merchand-zs9fmg@mail.grokbot.com

Source repository: https://github.com/GeminiGeorge22/publicrecords-dify-plugin

_Last updated: 24 November 2026_
