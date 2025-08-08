

import sys
import os
import io
import contextlib
import asyncio
import subprocess
import json

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
    output = ""
    
    # Run Bandit as a subprocess
    command = [sys.executable, '-m', 'bandit', '-r', path, '-f', 'txt']
    process = subprocess.run(command, capture_output=True, text=True)

    print(process.stdout)
    if process.stderr:
        print(process.stderr)

    if process.returncode == 0:
        print("Bandit scan completed. No issues found.")
    else:
        print(f"Bandit scan completed. Issues found (exit code: {process.returncode}).")

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

async def quizme():
    with open('encor_questions.json', 'r') as f:
        data = json.load(f)
    return data['Architecture']
