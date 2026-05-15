# VPS Deployment Guide (Ubuntu/Debian)

This guide provides step-by-step instructions to deploy the **VJ Filter Bot** on a VPS running Ubuntu or Debian.

## Prerequisites

- A VPS with Ubuntu 20.04+ or Debian 10+.
- Basic knowledge of using the terminal.
- [Telegram API ID and Hash](https://my.telegram.org).
- [Telegram Bot Token](https://t.me/BotFather).
- [MongoDB URI](https://www.mongodb.com/).

## Step 1: Update System and Install Dependencies

Connect to your VPS via SSH and run the following commands:

```bash
sudo apt update && sudo apt upgrade -y
sudo apt install python3-pip ffmpeg git -y
```

## Step 2: Clone the Repository

```bash
git clone https://github.com/VJBots/VJ-Filter-Bot
cd VJ-Filter-Bot
```

## Step 3: Install Required Python Packages

```bash
pip3 install -U -r requirements.txt
```

## Step 4: Configure Environment Variables

You can set environment variables directly in your shell or use a `.env` file. To use a `.env` file, create it in the root directory:

```bash
nano .env
```

Add your variables like this (replace with your actual values):

```env
API_ID=1234567
API_HASH=your_api_hash
BOT_TOKEN=your_bot_token
DATABASE_URI=mongodb+srv://user:pass@cluster.mongodb.net/test
LOG_CHANNEL=-100123456789
ADMINS=7597291420
CHANNELS=-100987654321
```

Press `Ctrl+O`, `Enter`, then `Ctrl+X` to save and exit.

## Step 5: Run the Bot

You can start the bot using:

```bash
python3 bot.py
```

### Running in the Background (Recommended)

To keep the bot running after you close the SSH session, use `screen` or `pm2`.

#### Using Screen:
1. Start a new screen session:
   ```bash
   screen -S vjbot
   ```
2. Run the bot:
   ```bash
   python3 bot.py
   ```
3. Detach from the session by pressing `Ctrl+A`, then `D`.
4. To return to the session later:
   ```bash
   screen -r vjbot
   ```

#### Using PM2 (Advanced):
1. Install PM2:
   ```bash
   sudo apt install nodejs npm -y
   sudo npm install pm2 -g
   ```
2. Start the bot:
   ```bash
   pm2 start bot.py --name vjbot --interpreter python3
   ```
3. Monitor the bot:
   ```bash
   pm2 logs vjbot
   ```

## Troubleshooting

- **Regex Warnings:** These have been fixed in the latest code.
- **Database Errors:** Ensure your MongoDB URI is correct and your IP is whitelisted in MongoDB Atlas settings.
- **Missing Dependencies:** Run `pip3 install -U -r requirements.txt` again to ensure all packages are installed.

For more support, join [SUPREME_BOTz Update Channel](https://t.me/SUPREME_BOTz).
