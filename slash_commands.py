

import sys
import os
import io
import contextlib
import asyncio

from duckduckgo_mcp_server.server import DuckDuckGoSearcher
from mcp.server.fastmcp import Context
from bandit.cli import main as bandit_main

# Mock Context class for our simple client
class MockContext(Context):
    async def info(self, message: str):
        pass

    async def error(self, message: str):
        print(f"ERROR: {message}")

    async def warn(self, message: str):
        print(f"WARN: {message}")

    async def debug(self, message: str):
        pass

class StringIOWithNoName(io.StringIO):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = None

async def run_bandit(path="."):

    print(f"Running bandit on: {path}")
    
    # Create a StringIOWithNoName object to capture output
    captured_output = StringIOWithNoName()
    
    # Temporarily redirect sys.stdout to our captured_output
    original_stdout = sys.stdout
    sys.stdout = captured_output
    
    original_argv = sys.argv
    try:
        sys.argv = ['bandit', '-r', path, '-f', 'txt']
        bandit_main.main()
        output = captured_output.getvalue()
        print(output) # Print the captured output to the original stdout
    except SystemExit as e:
        output = captured_output.getvalue()
        print(output) # Print the captured output to the original stdout
        if e.code == 0:
            print("Bandit scan completed. No issues found.")
        else:
            print(f"Bandit scan completed. Issues found (exit code: {e.code}).")
    finally:
        sys.stdout = original_stdout # Restore original stdout
        sys.argv = original_argv

async def perform_duckduckgo_search(query: str):
    searcher = DuckDuckGoSearcher()
    mock_ctx = MockContext()
    results = await searcher.search(query, mock_ctx)
    if results:
        return searcher.format_results_for_llm(results)
    else:
        return "No results found or an error occurred."

async def run_duckduckgo(query: str = "Python programming"):
    print(f"Running DuckDuckGo search for: {query}")
    results = await perform_duckduckgo_search(query)
    print("\n--- DuckDuckGo Search Results ---")
    print(results)

if __name__ == '__main__':
    # Example of how to run the slash commands
    run_bandit()
    asyncio.run(run_duckduckgo("latest AI news"))
