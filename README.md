# Gemini CLI Project Template

This project serves as a template for developing Python applications that integrate with the Gemini Command Line Interface (CLI). It demonstrates how to incorporate external Python packages like `bandit` for security analysis and `duckduckgo_mcp_interface` for web searches, and expose their functionalities as custom Gemini CLI slash commands.

## Features

- **Gemini CLI Integration:** Provides a structured way to define and manage custom slash commands for the Gemini CLI.
- **Bandit Integration:** Includes a slash command (`/bandit`) to run the Bandit static analysis tool on your project, helping identify common security vulnerabilities in Python code.
- **DuckDuckGo Search Integration:** Offers a slash command (`/ddg`) to perform web searches using the DuckDuckGo API, leveraging the `duckduckgo_mcp_interface`.
- **NIST Guidelines Reference:** Contains a reference to NIST guidelines (`/nist`) for secure bot development, emphasizing best practices for handling sensitive information.
- **Configurable Preferences:** Introduces a preference system (`/preferences`) that allows the Gemini CLI to understand and adapt to user-defined preferences for various tasks, such as preferred tools for web searches, project analysis, and security scanning.

## Setup and Installation

To get this project up and running, follow these steps:

1.  **Clone the repository:**
    ```bash
    git clone <repository_url>
    cd <repository_name>
    ```

2.  **Create and activate a virtual environment:**
    It's highly recommended to use a virtual environment to manage project dependencies.
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Install dependencies:**
    Install the required Python packages using `pip`.
    ```bash
    pip install -r requirements.txt
    ```

## Usage

Once the project is set up, you can interact with it through the Gemini CLI using the defined slash commands.

-   **`/bandit`**: Runs the Bandit static analysis tool on the project.
-   **`/ddg`**: Performs a DuckDuckGo web search. You can specify a query as an argument.
-   **`/nist`**: Displays the NIST guidelines for bot development.
-   **`/preferences`**: Shows the current preferences configured for the Gemini CLI's behavior.

## Project Structure

-   `.gemini/commands/`: Contains the `.toml` files defining the custom Gemini CLI slash commands.
-   `slash_commands.py`: Implements the Python functions that are executed by the slash commands.
-   `requirements.txt`: Lists the project's Python dependencies.
-   `NIST_guildlines.md`: Document outlining NIST guidelines for bot development.
-   `.gitignore`: Specifies files and directories to be ignored by Git.

