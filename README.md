# Key Stalker

A Windows desktop application packaged as a standalone executable for **user-authorized keyboard activity monitoring**.

## Installation Guide

### System Requirements

* Windows 10 or Windows 11
* 64-bit Windows
* No Python installation is required
* No `pip` installation is required

### Installation

1. Download the latest `keystalkersetup.exe` installer.
2. Double-click the installer.
3. If Windows displays a User Account Control prompt, click **Yes**.
4. Follow the installation wizard.
5. Complete the installation.

The application will be installed under:

```text
C:\Program Files\keystalker\
```

The main executable is:

```text
C:\Program Files\keystalker\keystalker.exe
```

### Starting the Application

After installation, the application can be started from the Start Menu:

```text
Start Menu
└── Key Stalker
```

The application can also be started directly from:

```text
C:\Program Files\keystalker\keystalker.exe
```

### Automatic Startup

The application can be configured to start automatically when the Windows user logs in.

The startup configuration uses Windows Task Scheduler:

```text
Trigger: At log on
Run: keystalker.exe
Run mode: Current logged-in user
```

This runs the application in the user's normal Windows session.

## Configuration

The application uses environment variables for configuration.

Create a `.env` file in the project root:

```text
keystalker/
├── .env
├── pyproject.toml
└── src/
    └── keystalker/
```

Example:

```env
TELEGRAM_API=your_bot_token
TELEGRAM_CHAT_ID=your_chat_id
```

The application loads these values using `python-dotenv`.

### Important Security Rule

Never commit `.env` to GitHub.

Add the following to `.gitignore`:

```gitignore
.env
```

For documentation, you can provide a safe `.env.example`:

```env
TELEGRAM_API=your_bot_token
TELEGRAM_CHAT_ID=your_chat_id
```

Users should copy `.env.example` to `.env` and enter their own configuration values.

## Telegram Bot Setup

The application can use a Telegram bot for authorized notifications.

### Create a Telegram Bot

1. Open Telegram.
2. Search for **@BotFather**.
3. Open the official BotFather account.
4. Send:

```text
/newbot
```

5. Enter a name for the bot.

Example:

```text
Key Stalker Bot
```

6. Enter a unique username for the bot. Telegram bot usernames normally end with `bot`.

Example:

```text
KeyStalkerBot
```

7. BotFather will provide a bot token.

Example format:

```text
123456789:AAExampleTokenValue
```

8. Store the token securely. Do not commit it to GitHub or expose it in logs.

### Configure the Bot Token

Add the token to `.env`:

```env
TELEGRAM_API=123456789:AAExampleTokenValue
```

The value should contain the token itself. Do not prepend `bot`.

### Get the Telegram Chat ID

1. Open the newly created bot in Telegram.
2. Click **Start** or send:

```text
/start
```

3. Retrieve the bot updates using the Telegram Bot API.
4. Find the `chat.id` value in the returned message.

Example:

```json
{
    "message": {
        "chat": {
            "id": 123456789,
            "type": "private"
        }
    }
}
```

The value:

```text
123456789
```

is the chat ID.

Add it to `.env`:

```env
TELEGRAM_API=123456789:AAExampleTokenValue
TELEGRAM_CHAT_ID=123456789
```

### Verify Telegram Configuration

The application should load the configuration using:

```python
import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.environ["TELEGRAM_API"]
CHAT_ID = os.environ["TELEGRAM_CHAT_ID"]
```

Never print the bot token in application logs.

## Development Setup

Python is required only for development.

### Clone the Repository

```powershell
git clone <repository-url>
cd keystalker
```

### Create a Virtual Environment

```powershell
python -m venv .venv
```

### Activate the Virtual Environment

```powershell
.\.venv\Scripts\Activate.ps1
```

### Install the Project

The project dependencies are defined in `pyproject.toml`.

Run:

```powershell
python -m pip install -e .
```

This installs the package and its declared dependencies.

### Run the Application

```powershell
python -m keystalker
```

## Building the Executable

### Install PyInstaller

```powershell
python -m pip install pyinstaller
```

### Build the Windows Executable

```powershell
python -m PyInstaller --onefile --noconsole --name keystalker --paths src src\keystalker\__main__.py
```

After a successful build:

```text
dist\
└── keystalker.exe
```

The generated executable is a standalone Windows application and does not require Python or `pip` on the target machine.

## Creating the Installer

The Windows installer is created using **Inno Setup**.

The installer packages:

```text
dist\keystalker.exe
```

and installs it into:

```text
C:\Program Files\keystalker\
```

The generated installer is:

```text
keystalkersetup.exe
```

The installer can also configure the application's authorized automatic startup through Windows Task Scheduler.

## Troubleshooting

### Application Does Not Start

Run the executable manually:

```text
C:\Program Files\keystalker\keystalker.exe
```

For development/debugging, build the application without `--noconsole` so that runtime errors are visible in the terminal.

### Python Package Cannot Be Found

Make sure the project has been installed:

```powershell
python -m pip install -e .
```

Then run:

```powershell
python -m keystalker
```

### Telegram Configuration Error

Verify that `.env` contains:

```env
TELEGRAM_API=your_bot_token
TELEGRAM_CHAT_ID=your_chat_id
```

Also verify that:

* The bot token is valid.
* The chat ID is correct.
* The bot can access the target chat.
* Internet connectivity is available.
* Firewall/proxy configuration allows the required HTTPS connection.
* TLS certificates are trusted.

Do not permanently disable TLS certificate verification.

### Automatic Startup Does Not Occur

Open:

```text
Task Scheduler
```

Then check:

```text
Task Scheduler Library
└── Key Stalker
```

Verify:

```text
Trigger:
At log on
```

and:

```text
Action:
C:\Program Files\keystalker\keystalker.exe
```

The task should run in the appropriate logged-in user's session.

## Security

The application should only be installed and used with the knowledge and authorization of the device owner or affected users.

Never commit sensitive information such as:

* Telegram bot tokens
* API keys
* Passwords
* Private certificates
* `.env` files

Add sensitive files to `.gitignore`:

```gitignore
.env
.venv/
__pycache__/
build/
dist/
*.egg-info/
```

If a secret is accidentally committed to a public repository, revoke or regenerate it immediately.

## Project Structure

```text
keystalker/
├── .env
├── .gitignore
├── pyproject.toml
├── keystalker.spec
├── requirements.txt
└── src/
    └── keystalker/
        ├── __init__.py
        ├── __main__.py
        └── actions/
            ├── __init__.py
            └── mailer.py
```

## Author

**Anurag Kumar**
Full-Stack Software Engineer

🌐 **Website:** [anuragkumar.co.in](https://anuragkumar.co.in)
💼 **LinkedIn:** [Anurag Kumar](https://www.linkedin.com/in/anurag-kumar-6a7106228/)
💻 **GitHub:** [anurag-kumar01](https://github.com/anurag-kumar01)


For questions, suggestions, or contributions, please open an issue or submit a pull request through the repository.

