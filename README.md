# Gemini CLI Base Repository

This repository serves as the foundational project for developing and integrating custom slash commands with the Gemini Command Line Interface (CLI). It is designed as a base on which other specialized repositories and projects can be built, extending the Gemini CLI's capabilities with new functionalities.

## Available Slash Commands

This project provides the following core slash commands:

-   **`/askgordon`**: Provides intelligent assistance or answers questions within the Gemini CLI context.
-   **`/bandit`**: Runs the Bandit static analysis tool on your project to identify common security vulnerabilities in Python code.
-   **`/ddg`**: Performs web searches using the DuckDuckGo API.

-   **`/mcp_catalog_lookup`**: Allows you to search and retrieve information from the Docker Multi-Cloud Platform (MCP) Catalog.
-   **`/mcp_toolkit_selector`**: Assists in determining the best Docker tool from the MCP Toolkit for a specific task or requirement.
-   **`/nist`**: Displays the NIST guidelines for secure bot development.
-   **`/preferences`**: Shows the current user preferences configured for the Gemini CLI's behavior.
-   **`/trivy`**: Runs a Trivy filesystem scan on the current directory to identify security vulnerabilities in project dependencies and configurations.

## Building on This Base

Other repositories can leverage the framework and existing commands provided here. By cloning this repository and extending its `slash_commands.py` or adding new `.toml` command definitions, developers can quickly create specialized Gemini CLI tools tailored to specific domains or tasks.

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

## Project Structure

-   `.gemini/commands/`: Contains the `.toml` files defining the custom Gemini CLI slash commands.
-   `slash_commands.py`: Implements the Python functions that are executed by the slash commands.
-   `trivy_commands.py`: Implements the Python functions for Trivy scans.
-   `requirements.txt`: Lists the project's Python dependencies.
-   `NIST_guildlines.md`: Document outlining NIST guidelines for bot development.
-   `question_bank.py`: Contains questions and answers for the `/quizme` command (even though `/quizme` is not listed as a primary command, the file might still be present in the repo).
-   `gns3_topology.py`: Defines the GNS3 network topology for the `/quizme` command.
-   `GNS3_INSTRUCTIONS.md`: Provides instructions for GNS3 configurations.
-   `test_quiz.py`: Contains unit tests for the quiz functionality.
-   `scraper.py`: A script that uses the `/ddg` command to scrape news from a website.
-   `.gitignore`: Specifies files and directories to be ignored by Git.