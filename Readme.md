# GenAI Summer Camp Chatbot

Welcome to the GenAI Summer Camp Chatbot project! This chatbot is designed to provide information about the fictional GenAI Summer Camp and assist parents in the application process for their kids.

## Table of Contents

- [About the Project](#about-the-project)
- [Directory Structure and Explanation](#directory-structure-and-explanation)
- [Open Questions](#open-questions)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Run](#run)

## About the Project

The GenAI Summer Camp Chatbot is built using the LLM (Language Learning Model). 
The project consists of two main tasks:
1. **GenAI Summer Camp Information**: This includes details about the camp's offerings, values, policies, location, dates, pricing, and age range.
2. **Assistant Creation**: This involves developing specific prompts to guide the user interaction.

## Directory Structure and Explanation

```
.
├── main.py
├── RouterPrompt.py
├── QuestionPrompt.py
├── ApplicationPrompt.py
├── assets/
│   ├── summer_camp_summary.txt
│   └── summer_camp_faq.txt
└── prompts/
    ├── router_prompt.txt
    ├── question_prompt.txt
    ├── application_prompt.txt
    ├── generate_faq_prompt.txt
    └── generate_summary_description_prompt.txt
```

- **main.py**: The primary entry point. Orchestrates the flow of the chatbot, calling functions from other Python files.
- **RouterPrompt.py**: Contains logic for the Router Prompt, determining if the parent wants to ask a question or sign their kid up.
- **QuestionPrompt.py**: Handles questions from parents using information from the assets files and provides answers.
- **ApplicationPrompt.py**: Manages the application process, collecting details, and validating the kid's age.
- **assets/**: Generated files containing a summary of the camp and frequently asked questions.
- **prompts/**: Contains templates or structures for the various prompts used in the chatbot.

## Open Questions

- How can the process be optimized with more time?



- What methods would be effective for testing the prompts' performance?
- What potential edge cases are currently not addressed?

### Getting Started

## Prerequisites

- Ensure you have Python 3.9 installed.
- Familiarity with the LLM is beneficial.
- Install the required libraries:
  - [openai](https://github.com/openai/openai-python)
  - [langchain](https://python.langchain.com/docs/get_started/introduction.html)

## Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/adarfrenkel/summer-camp-chatbot
   ```
2. Navigate to the project directory:
   ```sh
   cd summer-camp-chatbot
   ```
3. Install the required packages:
   ```sh
   pip install -r requirements.txt
   ```
4. Set your OPENAI_API_KEY:
   ```sh
   export OPENAI_API_KEY = <YOUR OPENAI API KEY>
   ```

## Run

1. Run the main script to interact with the chatbot:
   ```sh
   python main.py
   ```
