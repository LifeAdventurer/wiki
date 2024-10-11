# Typing Contest Discord Bot

This is a Discord bot built with `discord.py` to facilitate typing contests in a server. The bot enables users to start contests, join them, submit WPM (words per minute) results, and display rankings based on average WPM.


## Prerequisties

- Python 3.11+
- Poetry (recommended) or pip

## Installation


### 1. Clone the repository:

```sh
git clone https://github.com/your-username/typing-contest-bot.git
cd typing-contest-bot
```

### 2. Install dependencies:

#### Using Poetry (recommended)

If you haven't installed Poetry yet, use the following command:

```sh
curl -sSL https://install.python-poetry.org | python3 -
```

Then, install all dependencies by running:

```sh
poetry install
```

Activate the virtual environment:

```sh
poetry shell
```

#### Using pip

Create and activate a virtual environment:

```sh
python -m venv venv
source venv/bin/activate # On Windows use `venv\Scripts\activate`
```

Then, to install all dependencies, run:

```sh
pip install -r requirements.txt
```

### 3. Configure the bot:

Create a `config.json` file in the `./config/` directory with the following structure:

```json
{
    "token": "your-discord-bot-token",
    "typist_role_name": "your-server-typist-role",
    "testing_role_name": "your-server-testing-role", // Optional, required only for debug mode
    "contests_held": 0
}
```

### 4. Run the bot:

To start the bot, run:

```sh
python main.py # Or `poetry run python main.py` if using Poetry
```

## Commands

- `!start`: Start a typing contest in the current channel.
- `!end`: End the current typing contest.
- `!status`: Check the status of the typing contest.
- `!join`: Join the typing contest.
- `!quit`: Quit the typing contest.
- `!list`: Display all current participants in the typing contest.
- `!next`: Proceed to the next round in the typing contest and view the current WPM results.
- `!wpm {wpm}`: Submit your WPM result for the current round.
- `!result`: View the WPM results table at any time, not just after advancing rounds.
- `!remind`: Sends a reminder to participants who haven't submitted their WPM for the current round. Use this if the round has ended and some participants have not yet submitted their results.
- `!remove {member}`: Remove a participant from the typing contest. Only the contest creator can use this.
- `!ban {member}`: Ban a participant from the typing contest. Once banned, they cannot join again. Only the contest creator can use this.
- `!getrole`: Assign yourself the typist role.
- `!commands`: Show this list of commands.

## Contributing

Please see the [CONTRIBUTING.md](https://github.com/LifeAdventurer/typing-contest-bot/blob/main/CONTRIBUTING.md) for guidelines on contributing to this project.

## License

This project is licensed under the GNU General Public License v3.0 (GPL-3.0). See the [`LICENSE`](https://github.com/LifeAdventurer/typing-contest-bot/blob/main/LICENSE) file for details.

<h2 align="center">Happy Typing and Good Luck!</h2>
