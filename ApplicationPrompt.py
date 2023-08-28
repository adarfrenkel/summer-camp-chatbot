import json
import os

import openai
from langchain.chat_models import ChatOpenAI
from langchain.chains import create_extraction_chain


openai.api_key = os.environ['OPENAI_API_KEY']

schema = {
    "properties": {
        "allDataExist": {"type": "boolean"},
        "response": {"type": "string"},
        "parentName": {"type": "string"},
        "phoneNumber": {"type": "string"},
        "email": {"type": "string"},
        "age": {"type": "integer"},
    },
    "required": ["parentName", "phoneNumber","age"],
}
def completeLangChain(input_data: str):
    response = chain.run(input_data)
    print(response)
    if response is list:
        response = response[0]
    responseData = json.loads(response)

    print(responseData)
    all_data_exist = responseData["allDataExist"]
    if all_data_exist == "true":
        return responseData, True
    else:
        return responseData, False
llm = ChatOpenAI(temperature=0.9, model="gpt-4")
chain = create_extraction_chain(schema, llm)


def getPrompt():
    f = open("prompts/application_prompt.txt")
    prompt = f.read()
    f.close()
    return prompt

def complete(input_data: str):
    prompt = getPrompt()
    max_tokens = 150
    temperature = 1

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

    # uncomment to see json result
    # print(responseData)

    response = responseData['response']
    return response


if __name__ == '__main__':
    input_data = ""
    print("Welcome to GenAi Application assistant (type exit to stop)")
    print("Please provide the following information: your full name, phone number, email, and kid age.")
    while input_data != "exit":
        input_data = input()
        if input_data.lower() == "exit":
            break
        response, done = complete(input_data)
        print(response)
        print(done)


    print("Bye bye")