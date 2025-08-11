# CCNP Trainer - Interactive CLI Quiz

This project provides an interactive Command Line Interface (CLI) quiz experience using the Gemini CLI. The main feature is the `/quizme` slash command, which allows you to test your knowledge on various topics.

## The `/quizme` Command

The core of this project is the `/quizme` command, designed to provide an interactive quiz experience directly within the Gemini CLI.

### How it Works

The `/quizme` command is implemented in the `slash_commands.py` file. The `quiz_me` function takes two arguments:

-   `question_style`: The style of questions you want to be asked (e.g., "multiple choice", "flashcard").
-   `topic`: The topic you want to be quizzed on (e.g., "CCNP", "Security").

Currently, the `quiz_me` function is a placeholder that confirms the quiz is starting. Here is the relevant code snippet from `slash_commands.py`:

```python
def quiz_me(question_style: str, topic: str):
    """
    A placeholder for the quiz_me slash command.
    """

    return f"Starting a {question_style} quiz on {topic}!"
```

In a full implementation, this function would:

1.  Fetch questions from a question bank based on the chosen `topic`.
2.  Present questions to the user in the specified `question_style`.
3.  Receive and evaluate the user's answers.
4.  Keep track of the user's score and provide feedback.

## Other Features

This project also includes several other slash commands:

-   **`/bandit`**: Runs the Bandit static analysis tool to find common security vulnerabilities in the Python code.
-   **`/ddg`**: Performs a web search using the DuckDuckGo API.
-   **`/nist`**: Displays the NIST guidelines for secure bot development.
-   **`/preferences`**: Shows the current user preferences for the Gemini CLI.

## Project Structure

-   `.gemini/commands/`: Contains the `.toml` files that define the custom Gemini CLI slash commands.
-   `slash_commands.py`: Implements the Python functions for the slash commands, including `quiz_me`.
-   `scraper.py`: A script that uses the `/ddg` command to scrape news from a website.
-   `requirements.txt`: Lists the project's Python dependencies.
-   `NIST_guildlines.md`: A document containing the NIST guidelines for bot development, which can be a source for quiz questions.
-   `.gitignore`: Specifies files and directories to be ignored by Git.

## Setup and Installation

To get this project up and running, follow these steps:

1.  **Clone the repository:**
    ```bash
    git clone <repository_url>
    cd <repository_name>
    ```

2.  **Create and activate a virtual environment:**
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

## Usage

Once the project is set up, you can interact with it through the Gemini CLI using the defined slash commands. The main command is `/quizme`:

-   **`/quizme`**: Starts an interactive quiz. You can specify the `question_style` and `topic`.
    -   Example: `/quizme question_style="multiple choice" topic="CCNP"`