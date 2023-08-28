import json
import os

import openai


openai.api_key = os.environ['OPENAI_API_KEY']

enrollPrompt = "Please provide: Your full name, your phone number, your email, and your kid age."

def getPrompt():
    f = open("prompts/application_prompt.txt")
    prompt = f.read()
    f.close()
    return prompt

def format_properties_as_string(properties_dict):
    property_titles = {
        "parentName": "Your Name",
        "parentPhoneNumber": "Your Phone Number",
        "parentEmail": "Parent Email",
        "childAge": "The Child Age"
    }

    formatted_string = ""
    for prop_name, value in properties_dict.items():
        if prop_name not in property_titles: continue
        title = property_titles.get(prop_name, prop_name)  # Use original name if not in dictionary
        formatted_string += f'{title}: {value}\n\n'

    return formatted_string

def extract_properties(json_string):
    extracted_data = {
        "allDataExist": None,
        "response": None,
        "parentName": None,
        "parentPhoneNumber": None,
        "parentEmail": None,
        "childAge": None
    }

    # Attempt to parse JSON and extract values
    try:
        data = json.loads(json_string)
        for key in extracted_data.keys():
            extracted_data[key] = data.get(key)
    except json.JSONDecodeError as json_error:
        print(f"JSON parsing error: {json_error}")
        try:
            for key in extracted_data.keys():
                start_index = json_string.find(f'"{key}":') + len(f'"{key}":')
                end_index = json_string.find(',', start_index) if ',' in json_string[start_index:] else json_string.find('}', start_index)
                if start_index != -1 and end_index != -1:
                    value = json_string[start_index:end_index].strip(' "')
                    extracted_data[key] = value
        except Exception as e:
            print(f"Error during string manipulation: {e}")

    return extracted_data

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
    responseData = extract_properties(response)

    if responseData['allDataExist'] == True:
        response = f"{responseData['response']}\n\n{format_properties_as_string(responseData)}"
    else:
        response = responseData['response']

        response = f"{'' if response is None else response + ', '}\n\n{enrollPrompt}"

    return response


if __name__ == '__main__':
    input_data = ""
    print("Welcome to GenAi Application assistant (type exit to stop)")
    print(enrollPrompt)
    while input_data != "exit":
        input_data = input()
        if input_data.lower() == "exit":
            break
        response, done = complete(input_data)
        print(response)
        print(done)


    print("Bye bye")