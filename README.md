# IP Info Bot

[![Python](https://img.shields.io/badge/Python-3.6%2B-blue.svg)](https://www.python.org/)
[![Telegram](https://img.shields.io/badge/Telegram-Bot-blue.svg)](https://core.telegram.org/bots)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

## Table of Contents

- [Project Overview](#ip-info-bot)
- [File Structure](#file-structure)
- [Technical Details](#technical-details)
- [Installation](#installation)
- [Usage](#usage)
- [Extending the Bot](#extending-the-bot)
- [Supported Operating Systems](#supported-operating-systems)
- [Troubleshooting](#troubleshooting)
- [License](#license)
- [Contribution](#contribution)

## Project Overview

This project implements a Telegram bot that provides detailed information about any public IP address using the `ip_info_ye` package. The bot is designed for extensibility and ease of use, with a focus on cross-platform compatibility.



## File Structure

- `main.py`: Core Telegram bot implementation handling commands and IP lookups.
- `README.md`: Project documentation.

## Technical Details

### main.py

- Utilizes `pyTelegramBotAPI` for Telegram bot interactions.
- Handles commands:
  - `/start`: Sends a welcome message.
  - `/help`: Provides usage instructions.
  - `/ip <IP_address>`: Fetches and displays detailed IP information.
- Automatically installs missing dependencies (`pyTelegramBotAPI`, `ip-info-ye`) if not present.
- Formats output using Markdown with tables for readability.

## Installation

Ensure Python 3.x is installed on your system. The bot will attempt to auto-install required packages if missing.

### Download Map

| Operating System | Icon | Download / Install Instructions                          |
|------------------|------|----------------------------------------------------------|
| Windows          | 🪟   | [Download Python](https://www.python.org/downloads/windows/) |
| Linux            | 🐧   | Use your package manager, e.g., `sudo apt install python3` |
| MacOS            | 🍎   | [Download Python](https://www.python.org/downloads/macos/) or `brew install python` |
| Other            | 💻   | [Python Downloads](https://www.python.org/downloads/)     |

Alternatively, manually install dependencies:

```bash
pip install pyTelegramBotAPI ip-info-ye
```

## Usage

### Running the Bot

```bash
python main.py
```

## Extending the Bot

- Add new commands by defining new handlers in `main.py`.
- Enhance IP data retrieval by extending or replacing the `ip_info_ye` package usage.

## Supported Operating Systems

- Windows
- Linux
- MacOS
- Other Unix-like systems

## Troubleshooting

- If the bot fails to start, ensure Python 3.x is installed and accessible via the command line.
- Check internet connectivity for IP data retrieval.
- Review console output for error messages.

## License

This project is provided "as-is" without any warranties. Use at your own risk.

## Contribution

Contributions are welcome. Please fork the repository and submit pull requests for improvements or bug fixes.
