from bs4 import BeautifulSoup
import json

with open('page.html', 'r') as f:
    soup = BeautifulSoup(f.read(), 'html.parser')

questions = []

for question_tag in soup.find_all('p'):
    if question_tag.find('strong'):
        question_text = question_tag.find('strong').text.strip()
        choices = []
        correct_answer = ''
        explanation = ''

        next_sibling = question_tag.find_next_sibling()
        while next_sibling and next_sibling.name == 'p' and next_sibling.find('span'):
            choice_span = next_sibling.find('span')
            choice_text = next_sibling.text.strip()
            choices.append(choice_text)
            if 'style' in choice_span.attrs and 'color: #ff0000;' in choice_span['style']:
                correct_answer = choice_text
            next_sibling = next_sibling.find_next_sibling()

        if next_sibling and next_sibling.name == 'p' and 'Explanation:' in next_sibling.text:
            explanation = next_sibling.text.replace('Explanation:', '').strip()

        # Basic validation to avoid adding non-question content
        if choices and correct_answer:
            questions.append({
                "question": question_text,
                "choices": choices,
                "answer": correct_answer,
                "explanation": explanation
            })


with open('encor_questions.json', 'r') as f:
    data = json.load(f)

if 'General' not in data:
    data['General'] = []

data['General'].extend(questions)

with open('encor_questions.json', 'w') as f:
    json.dump(data, f, indent=2)

print(f"Added {len(questions)} questions to the General section.")
