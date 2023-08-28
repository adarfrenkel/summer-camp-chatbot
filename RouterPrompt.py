import json
import os

import openai

openai.api_key = os.environ['OPENAI_API_KEY']


def getPrompt():
    f = open("prompts/router_prompt.txt")
    prompt = f.read()
    f.close()
    return prompt

def extract_intent_and_question(json_string):
    intent = None
    question = None

    # Attempt to parse JSON and extract values
    try:
        data = json.loads(json_string)
        intent = data.get("intent")
        question = data.get("question")
    except json.JSONDecodeError as json_error:
        print(f"JSON parsing error: {json_error}")
        try:
            intent_start = json_string.find('"intent":') + len('"intent":')
            intent_end = json_string.find('"', intent_start + 1)
            intent = json_string[intent_start:intent_end]

            question_start = json_string.find('"question":') + len('"question":')
            question_end = json_string.find('"', question_start + 1)
            question = json_string[question_start:question_end]
        except Exception as e:
            print(f"Error during string manipulation: {e}")

    return intent, question

def complete(input_data: str):
    prompt = getPrompt()
    max_tokens = 100  # Set the maximum token limit
    temperature = 0  # Set the temperature

    messages = [
        {"role": "system", "content": prompt + input_data},
    ]

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        max_tokens=max_tokens,
        temperature=temperature,
        messages=messages)
    response = response.choices[0].message.content
    return extract_intent_and_question(response)





if __name__ == '__main__':
    inputData = ""
    print("Welcome to GenAi assistant (type exit to stop)")
    while inputData != "exit":
        print("How can I help?")
        inputData = input()
        if inputData.lower() == "exit":
            break
        response = complete(inputData)
        print(response)

    print("Bye bye")