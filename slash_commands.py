

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

def generate_gns3_config(topic):
    if topic != "OSPF":
        return "GNS3 configuration generation is only supported for OSPF at the moment."

    try:
        with open("gns3_topology.py", "r") as f:
            topology = json.load(f)
    except FileNotFoundError:
        return "gns3_topology.py file not found."
    except json.JSONDecodeError:
        return "Invalid JSON in gns3_topology.py."

    if not os.path.exists("gns3_configs"):
        os.makedirs("gns3_configs")

    for router in topology["routers"]:
        config = f"hostname {router['name']}\n\n"
        for interface in router["interfaces"]:
            config += f"interface {interface['name']}\n"
            config += f" ip address {interface['ip_address']} {interface['subnet_mask']}\n"
            config += f" no shutdown\n\n"
        
        config += "router ospf 1\n"
        config += f" router-id {router['name'].replace('R','')}.{router['name'].replace('R','')}.{router['name'].replace('R','')}.{router['name'].replace('R','')}\n"
        config += " network 10.0.0.0 0.0.0.255 area 0\n"

        with open(f"gns3_configs/{router['name']}_config.txt", "w") as f:
            f.write(config)

    return "GNS3 configuration files have been generated in the 'gns3_configs' directory."

def quiz_me(question_style: str, topic: str):
    try:
        with open("question_bank.py", "r") as f:
            question_bank = json.load(f)
    except FileNotFoundError:
        return "question_bank.py file not found."
    except json.JSONDecodeError:
        return "Invalid JSON in question_bank.py."

    if topic not in question_bank:
        return f"Topic '{topic}' not found in the question bank."

    questions = question_bank[topic]
    score = 0

    for i, q in enumerate(questions):
        print(f"Question {i+1}: {q['question']}")
        for option, text in q['options'].items():
            print(f"  {option}: {text}")
        
        user_answer = input("Your answer (A, B, C, or D): ").upper()

        if user_answer == q['answer']:
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The correct answer is {q['answer']}.")

    final_score = (score / len(questions)) * 100
    result = f"You scored {final_score:.2f}%."

    if final_score < 50:
        result += "\n" + generate_gns3_config(topic)

    return result

