import sys
import json

def triage_error_log(log_content):
    summary = {
        "status": "Untriaged",
        "type": "Unknown",
        "message": "Could not determine specific error message.",
        "context": "No specific context extracted.",
        "slack_ready_summary": ""
    }

    lines = log_content.splitlines()
    error_keywords = ["Error", "Exception", "Failed", "Traceback"]

    for i, line in enumerate(lines):
        for keyword in error_keywords:
            if keyword in line:
                summary["status"] = "Triaged"
                summary["type"] = keyword
                summary["message"] = line.strip()

                # Try to get context
                start_index = max(0, i - 2)
                end_index = min(len(lines), i + 3)
                summary["context"] = "\n".join(lines[start_index:end_index]).strip()
                break
        if summary["status"] == "Triaged":
            break

    if summary["status"] == "Untriaged":
        summary["message"] = "No common error keywords found. Please review manually."
        summary["context"] = log_content[:500] + "..." if len(log_content) > 500 else log_content

    summary["slack_ready_summary"] = f"""
*Error Triage Report*
*Status:* {summary['status']}
*Type:* {summary['type']}
*Message:* ```{summary['message']}```
*Context:*
```
{summary['context']}
```
"""
    return summary

if __name__ == "__main__":
    if len(sys.argv) > 1:
        error_log_content = sys.argv[1]
        result = triage_error_log(error_log_content)
        print(result["slack_ready_summary"])
    else:
        print("Usage: python triage_error.py \"<error_log_content>\"")
