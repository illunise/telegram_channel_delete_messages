# README.md

# Telegram Message Deletion Bot

A simple Python script using **Telethon** to automatically delete messages from a specific Telegram channel.

## Features

- Connects to your Telegram account using **API ID** and **API Hash**.
- Iterates through all messages in a specified channel.
- Deletes messages one by one.
- Logs deleted messages and any errors encountered.

## Requirements

- Python 3.8+
- Telethon library

```bash
pip install telethon
```

## Setup

1. **Obtain Telegram API credentials:**
   - Go to [my.telegram.org](https://my.telegram.org) → API Development Tools → Create a new application to get `api_id` and `api_hash`.

2. **Update the script:**
   Replace the placeholders in the script:
   ```python
   api_id = 23415122
   api_hash = 'YOUR_API_HASH'
   session_name = 'ManishForward'
   channel = -1001985769215  # Replace with your channel ID
   ```

3. **Run the script:**
   ```bash
   python delete_messages.py
   ```

> ⚠️ **Warning:** Deleting messages is irreversible. Make sure you are deleting messages from the correct channel.

## Usage

- The script automatically deletes messages from the channel specified.
- It prints the IDs of deleted messages and logs any errors if a message could not be deleted.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

