import json
import os

import openai

openai.api_key = os.environ['OPENAI_API_KEY']


def getPrompt():
    f = open("prompts/router_prompt.txt")
    prompt = f.read()
    f.close()
    return prompt


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
    responseData = json.loads(response)
    state = responseData['intent']
    question = responseData['question']
    return state, question





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