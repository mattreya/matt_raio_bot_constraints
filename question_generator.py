import json
from default_api import google_web_search

def generate_questions(topic):
    prompt = f"Generate 5 multiple choice questions with answers and explanations for the following CCNP ENCOR topic: {topic}"
    response = google_web_search.run(prompt)
    # This is a placeholder for the actual response from the LLM
    # In a real implementation, you would parse the response from the LLM
    # and format it into the desired JSON structure.
    return [
        {
            "question": f"This is a sample question about {topic}?",
            "choices": ["Choice A", "Choice B", "Choice C", "Choice D"],
            "answer": "Choice A",
            "explanation": f"This is an explanation for the sample question about {topic}."
        }
    ] * 5

# Get the exam topics for the Architecture section
architecture_topics = [
    "1.1 Explain the different design principles used in an enterprise network",
    "1.2 Differentiate between on-premises and cloud infrastructure deployments",
    "1.3 Explain the working principles of the Cisco SD-WAN solution",
    "1.4 Explain the working principles of the Cisco SD-Access solution",
    "1.5 Differentiate hardware and software switching mechanisms"
]

questions = []
for topic in architecture_topics:
    questions.extend(generate_questions(topic))

with open('encor_questions.json', 'r') as f:
    data = json.load(f)

data['Architecture'].extend(questions)

with open('encor_questions.json', 'w') as f:
    json.dump(data, f, indent=2)

print(f"Added {len(questions)} questions to the Architecture section.")
