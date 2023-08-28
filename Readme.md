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

#### 1. How can the process be optimized with more time?
With more time, the chatbot process can be optimized in several ways:
- **Enhanced Data Validation:** Implement robust techniques, especially for the application process, to ensure data integrity and security.
- **User Experience Enhancement:** Develop a user context system to tailor interactions, such as suggesting activities based on a parent's previous inquiries.
- **Expand Knowledge Base:** Broaden the chatbot's knowledge with more FAQs and relevant information, enhancing its response accuracy.
- **Refined Error Handling:** Improve mechanisms to gracefully manage unexpected situations, ensuring coherent and helpful responses.
- **Prompt Hacking Defense:** Employ commonsense strategies and advanced prompt techniques, like instruction defense and XML tagging, to bolster security against potential hacking attempts.

#### 2. What methods would be effective for testing the prompts' performance?
To ensure the chatbot prompts perform optimally and provide users with accurate and relevant responses, several testing methods can be employed:
- **Error Rate Monitoring:** Track how often the chatbot provides incorrect or irrelevant answers, which can highlight issues with the prompt's design.
- **Automated Testing:** Use scripts with predefined inputs to systematically check the chatbot's responses for accuracy and consistency.
- **Edge Case Testing:** Examine the chatbot's ability to handle uncommon scenarios or inputs, ensuring comprehensive coverage.
- **Sentiment Analysis:** Analyze user responses to measure their overall satisfaction and detect potential areas of confusion or frustration.
- **A/B Testing:** Test different versions of a prompt on separate user groups to identify which phrasing or structure yields the best results.
- **User Feedback:** Collect direct feedback after interactions to understand users' perceptions of the chatbot's clarity, relevance, and helpfulness.

#### 3. What potential edge cases are currently not addressed?
The following are some potential edge cases that have not been addressed:
- **Contradictory Instructions:** Users might provide conflicting directives in a single input, such as "Tell me about the camp but don't mention the dates."
- **Multiple Questions in One Input:** The chatbot might get confused if users pose several questions within a single sentence, especially if it's designed to address only one query at a time.
- **Ambiguous Queries:** Some questions can be open to multiple interpretations, potentially leading the chatbot to respond based on an unintended interpretation.
- **Incomplete or Fragmented Inputs:** The chatbot might struggle with understanding the context if users provide fragmented sentences or incomplete thoughts.
- **Uncommon User Inputs:** The chatbot might not recognize or know how to process symbols, emojis, or non-standard characters input by users.

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
