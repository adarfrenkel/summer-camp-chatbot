# GenAI Summer Camp Chatbot

Welcome to the GenAI Summer Camp Chatbot project! This chatbot is designed to provide information about the fictional GenAI Summer Camp and assist parents in the application process for their kids.

## Table of Contents

- [About the Project](#about-the-project)
- [Directory Structure](#directory-structure)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
- [Open Questions](#open-questions)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## About the Project

The GenAI Summer Camp Chatbot is built using the LLM (Language Learning Model). The project consists of two main tasks:

1. **GenAI Summer Camp Information**: This includes details about the camp's offerings, values, policies, location, dates, pricing, and age range.
2. **Assistant Creation**: This involves developing specific prompts to guide the user interaction:
   - **Router Prompt**: Determines if the parent wants to ask a question about the camp or sign their kid up.
   - **Question Prompt**: Handles questions from parents and provides answers based on the camp information.
   - **Application Prompt**: Manages the application process, collecting necessary details and validating the kid's age.

## Directory Structure

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

## Getting Started

### Prerequisites

- Ensure you have Python 3.x installed.
- Familiarity with the LLM is beneficial.
- Install the required libraries:
  - [openai](https://github.com/openai/openai-python)
  - [langchain](https://python.langchain.com/docs/get_started/introduction.html)

### Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/your-repo-link/genai-summer-camp-chatbot.git
   ```
2. Navigate to the project directory:
   ```sh
   cd genai-summer-camp-chatbot
   ```
3. Install the required packages:
   ```sh
   pip install -r requirements.txt
   ```

## Usage

1. Run the main script to interact with the chatbot:
   ```sh
   python main.py
   ```

## Open Questions

- How can the process be optimized with more time?
- What methods would be effective for testing the prompts' performance?
- What potential edge cases are currently not addressed?

## Contributing

Contributions are what make the open-source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

Distributed under the MIT License. See `LICENSE` for more information.

## Contact

Your Name - [adar.frenkel@gmail.com](mailto:adar.frenkel@gmail.com)

Project Link: [https://github.com/your-username/genai-summer-camp-chatbot](https://github.com/your-username/genai-summer-camp-chatbot)

---

Let me know if this updated version meets your requirements or if you'd like any further modifications!