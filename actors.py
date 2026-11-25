"""Allowlisted Public Records Actors that this plugin may run."""

from __future__ import annotations

ACTORS: list[dict[str, str]] = [
    {
        "id": "publicrecords/etsy-search-scraper",
        "actor": "etsy-search-scraper",
        "name": "Etsy Search MCP: Listings, Prices & Best Sellers",
        "one_line": "Etsy search results by keyword or category: price, rating, reviews, Bestseller badge, ad flag and search rank.",
        "store_url": "https://apify.com/publicrecords/etsy-search-scraper",
        "endpoint": "https://mcp.apify.com?tools=publicrecords/etsy-search-scraper"
    },
    {
        "id": "publicrecords/etsy-shop-velocity",
        "actor": "etsy-shop-velocity",
        "name": "Etsy Shop Daily Sales MCP",
        "one_line": "Daily, 7-day and 28-day sales for 370,000+ Etsy shops, measured from each shop's public sales counter.",
        "store_url": "https://apify.com/publicrecords/etsy-shop-velocity",
        "endpoint": "https://mcp.apify.com?tools=publicrecords/etsy-shop-velocity"
    },
    {
        "id": "publicrecords/sports-odds-api",
        "actor": "sports-odds-api",
        "name": "Sports Odds API MCP: BetRivers, Unibet, Paf, Svenska Spel",
        "one_line": "Live and pre-game betting odds from BetRivers, Unibet, Paf, Svenska Spel and ATG in one call, with the best price per outcome.",
        "store_url": "https://apify.com/publicrecords/sports-odds-api",
        "endpoint": "https://mcp.apify.com?tools=publicrecords/sports-odds-api"
    },
    {
        "id": "publicrecords/company-social-profile-finder",
        "actor": "company-social-profile-finder",
        "name": "Company Social MCP: Website to LinkedIn & Social Links",
        "one_line": "Finds a company's LinkedIn, X, YouTube, Instagram and Facebook profiles from its name or website, with evidence.",
        "store_url": "https://apify.com/publicrecords/company-social-profile-finder",
        "endpoint": "https://mcp.apify.com?tools=publicrecords/company-social-profile-finder"
    },
    {
        "id": "publicrecords/legistar-meetings-scraper",
        "actor": "legistar-meetings-scraper",
        "name": "City Council Meetings MCP (Legistar)",
        "one_line": "City council meetings, agenda items and documents for any city on Legistar, with source links.",
        "store_url": "https://apify.com/publicrecords/legistar-meetings-scraper",
        "endpoint": "https://mcp.apify.com?tools=publicrecords/legistar-meetings-scraper"
    },
    {
        "id": "publicrecords/eu-ted-notices-scraper",
        "actor": "eu-ted-notices-scraper",
        "name": "EU TED Tenders MCP: Daily Procurement Notices",
        "one_line": "EU procurement notices from TED (Tenders Electronic Daily): buyer, CPV, value, deadline and source link.",
        "store_url": "https://apify.com/publicrecords/eu-ted-notices-scraper",
        "endpoint": "https://mcp.apify.com?tools=publicrecords/eu-ted-notices-scraper"
    },
    {
        "id": "publicrecords/govcon-opportunity-feed",
        "actor": "govcon-opportunity-feed",
        "name": "Federal Contracts MCP: SAM.gov + Grants.gov",
        "one_line": "New US federal contract and grant notices from SAM.gov and Grants.gov in one feed, with source links.",
        "store_url": "https://apify.com/publicrecords/govcon-opportunity-feed",
        "endpoint": "https://mcp.apify.com?tools=publicrecords/govcon-opportunity-feed"
    },
    {
        "id": "publicrecords/grants-gov-scraper",
        "actor": "grants-gov-scraper",
        "name": "Grants.gov MCP: Open Federal Grants",
        "one_line": "Open US federal grants from Grants.gov: agency, deadline, eligibility and source link.",
        "store_url": "https://apify.com/publicrecords/grants-gov-scraper",
        "endpoint": "https://mcp.apify.com?tools=publicrecords/grants-gov-scraper"
    },
    {
        "id": "publicrecords/usaspending-awards-scraper",
        "actor": "usaspending-awards-scraper",
        "name": "USAspending Awards MCP: Federal Contract & Grant Awards",
        "one_line": "US federal contract and grant awards from USAspending by agency, recipient, NAICS and period.",
        "store_url": "https://apify.com/publicrecords/usaspending-awards-scraper",
        "endpoint": "https://mcp.apify.com?tools=publicrecords/usaspending-awards-scraper"
    },
    {
        "id": "publicrecords/uk-find-a-tender-scraper",
        "actor": "uk-find-a-tender-scraper",
        "name": "UK Tenders MCP: Find a Tender & Contracts Finder",
        "one_line": "UK government tenders from Find a Tender and Contracts Finder: buyer, value, deadline and source link.",
        "store_url": "https://apify.com/publicrecords/uk-find-a-tender-scraper",
        "endpoint": "https://mcp.apify.com?tools=publicrecords/uk-find-a-tender-scraper"
    },
    {
        "id": "publicrecords/ashby-jobs-scraper",
        "actor": "ashby-jobs-scraper",
        "name": "Ashby Jobs MCP: New Postings Since Any Date",
        "one_line": "New job postings from any Ashby job board since a date or window (24h, 7d, 30d), with full details.",
        "store_url": "https://apify.com/publicrecords/ashby-jobs-scraper",
        "endpoint": "https://mcp.apify.com?tools=publicrecords/ashby-jobs-scraper"
    },
    {
        "id": "publicrecords/lever-jobs-scraper",
        "actor": "lever-jobs-scraper",
        "name": "Lever Jobs MCP: New Postings Since Any Date",
        "one_line": "New job postings from any Lever job board since a date or window (24h, 7d, 30d), with full details.",
        "store_url": "https://apify.com/publicrecords/lever-jobs-scraper",
        "endpoint": "https://mcp.apify.com?tools=publicrecords/lever-jobs-scraper"
    },
    {
        "id": "publicrecords/spotify-play-count-scraper",
        "actor": "spotify-play-count-scraper",
        "name": "Spotify Play Count & Monthly Listeners MCP",
        "one_line": "Spotify play count for every track, plus an artist's monthly listeners and followers, from a track, album, playlist or artist link.",
        "store_url": "https://apify.com/publicrecords/spotify-play-count-scraper",
        "endpoint": "https://mcp.apify.com?tools=publicrecords/spotify-play-count-scraper"
    },
    {
        "id": "publicrecords/google-ads-transparency-scraper",
        "actor": "google-ads-transparency-scraper",
        "name": "Google Ads Transparency MCP: Competitor Ads",
        "one_line": "A competitor's new, running and stopped Google ads from the Google Ads Transparency Center, with first and last shown dates.",
        "store_url": "https://apify.com/publicrecords/google-ads-transparency-scraper",
        "endpoint": "https://mcp.apify.com?tools=publicrecords/google-ads-transparency-scraper"
    },
    {
        "id": "publicrecords/calibration-ledger",
        "actor": "calibration-ledger",
        "name": "Calibration Ledger MCP: Forecast Track Records (beta)",
        "one_line": "An organization's forecast track record (IMF, OECD, Fed, ECB SPF, listed issuers): errors, bias and band coverage. Beta.",
        "store_url": "https://apify.com/publicrecords/calibration-ledger",
        "endpoint": "https://mcp.apify.com?tools=publicrecords/calibration-ledger"
    },
    {
        "id": "publicrecords/greenhouse-jobs-scraper",
        "actor": "greenhouse-jobs-scraper",
        "name": "Greenhouse Jobs MCP: New Postings Since Any Date",
        "one_line": "New job postings from any Greenhouse job board since a date or window (24h, 7d, 30d), with full details.",
        "store_url": "https://apify.com/publicrecords/greenhouse-jobs-scraper",
        "endpoint": "https://mcp.apify.com?tools=publicrecords/greenhouse-jobs-scraper"
    },
    {
        "id": "publicrecords/smartrecruiters-jobs-scraper",
        "actor": "smartrecruiters-jobs-scraper",
        "name": "SmartRecruiters Jobs MCP: New Postings Since Any Date",
        "one_line": "New job postings from any SmartRecruiters careers site since a date or window (24h, 7d, 30d), with full details.",
        "store_url": "https://apify.com/publicrecords/smartrecruiters-jobs-scraper",
        "endpoint": "https://mcp.apify.com?tools=publicrecords/smartrecruiters-jobs-scraper"
    },
    {
        "id": "publicrecords/tennis-scores-api",
        "actor": "tennis-scores-api",
        "name": "Tennis Scores API: ATP & WTA Live Scores, Results, Rankings",
        "one_line": "Every ATP and WTA match for a date or a whole tournament (Grand Slams, singles, doubles, mixed): set-by-set scores, tiebreaks, seeds, round, court and winner, plus ATP/WTA rankings. No login, no proxy.",
        "store_url": "https://apify.com/publicrecords/tennis-scores-api",
        "endpoint": ""
    }
]

ALLOWED_IDS: frozenset[str] = frozenset(a["id"] for a in ACTORS)
ALLOWED_BY_SHORT: dict[str, str] = {a["actor"]: a["id"] for a in ACTORS}

def resolve_actor_id(value: str) -> str | None:
    raw = (value or "").strip().lstrip("@")
    if not raw:
        return None
    if raw in ALLOWED_IDS:
        return raw
    if raw in ALLOWED_BY_SHORT:
        return ALLOWED_BY_SHORT[raw]
    slashed = raw.replace("~", "/")
    if slashed in ALLOWED_IDS:
        return slashed
    return None
