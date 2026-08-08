# GeoIP-Locator

A simple Python command-line tool to fetch approximate geolocation details (country, region, city, and coordinates) for any IPv4 address using the free [ip-api.com](http://ip-api.com) API.

## Features

- 🌍 Look up location details for any public IP address
- 📡 Automatically detect and locate your own public IP
- 🖥️ Simple interactive command-line menu
- ⚡ No API key required (uses ip-api.com's free tier)

## How It Works

The script sends a request to `ip-api.com`'s JSON endpoint:

```
http://ip-api.com/json/<ip_address>
```

- If you provide a specific IP address, it fetches location data for that IP.
- If you leave the IP address blank, the API automatically detects and uses **your own public IP** (the IP your device is using to reach the internet).

The API returns a JSON response containing fields like `country`, `regionName`, `city`, `lat`, and `lon`, which the script parses and displays in a readable format.

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/<your-username>/GeoIP-Locator.git
   cd GeoIP-Locator
   ```

2. Install the required dependency:
   ```bash
   pip install requests
   ```

## Usage

Run the script:

```bash
python geoip_locator.py
```

You'll see a menu with three options:

```
Checking your last location using IP address
Chose your option:
1. Manually enter an IP Address
2. Fetch My IP Address automatically
3. Exit
```

- **Option 1** — Enter any public IPv4 address manually to look up its location.
- **Option 2** — Automatically fetch and locate your own public IP address.
- **Option 3** — Exit the program.

### Example Output

```
=== Location Results ===
IP Address:   103.149.126.34
Country:      India
Region/State: Maharashtra
City:         Pune
Coordinates:  18.5211, 73.8502
========================
```

## Important Notes & Limitations

- **This is NOT GPS-level tracking.** IP-based geolocation estimates location based on how ISPs register their IP address blocks, not real-time GPS data.
- **Coordinates are approximate.** The `lat`/`lon` values usually point to the ISP's regional infrastructure (like a local exchange or data center), not the exact physical location of the device using that IP. Accuracy of a few to tens of kilometers is normal.
- **Country and region-level accuracy is generally reliable.** City-level accuracy varies depending on the ISP and region.
- **Private/reserved IPs will fail.** IPs like `127.0.0.1`, `192.168.x.x`, or `10.x.x.x` are not public and will return errors, since they aren't routable on the public internet.
- **Rate limits apply.** ip-api.com's free tier allows a limited number of requests per minute. For heavier use, consider their paid plans or an alternative provider.

## Tech Stack

- Python 3
- [`requests`](https://pypi.org/project/requests/) library
- [ip-api.com](http://ip-api.com) — free IP geolocation API

## License

This project is open-source and available under the [MIT License](LICENSE).

## Disclaimer

This tool is intended for educational and informational purposes only (e.g., understanding network geolocation, debugging, learning API integration). Do not use it to locate or track individuals without their consent — IP-based location data is approximate and should never be relied upon for precise tracking.
