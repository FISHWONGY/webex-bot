# webex-bot

Chat GPT AI assistant w/ Webex integration

This project is a Webex Chatbot that uses OpenAI's GPT-3.5 model to provide automated responses. It was developed in Python and uses the OpenAI API, Webex API and Jira API for chat operations.

## ✨ Demo
![webex-bot](https://github.com/FISHWONGY/webex-bot/assets/59711659/30dea415-d609-4b30-8396-50865fcce965)



## ✨ Background

The core functionality of the chatbot is provided by OpenAI's GPT-3.5 model, specifically with the autocompletion API.
Webex is a collaboration platform that can be used as a messsaging tool. This project uses the Webex API to interact with users on the platform.

## ✨ Folder Structure
```
.
├── Dockerfile
├── README.md
├── app
│   ├── bot_commands.py
│   ├── helpers
│   │   ├── common_func.py
│   │   ├── jiraapi.py
│   │   └── openaiapi.py
│   ├── main.py
│   ├── prompts.py
│   └── utils.py
├── deploy
│   ├── common
│   ├── development
│   ├── production
│   └── staging
├── docker-compose.yml
├── pyproject.toml
└── skaffold.yaml

```

## ✨ Installation
1. ```git clone https://github.com/FISHWONGY/webex-bot/```

2. ```poetry install```

3. Set all env var

4. ```python main.py```

 ## ✨ Features

    - SQL Debugging and Optimization: The chatbot can understand SQL queries and help with debugging and optimization.
    - Code Assistance: The chatbot can provide assistance with code-related issues.
    - Jira Story Creation: The chatbot can create Jira stories based on user input.


 ## ✨ Usage

To use the bot, send messages to it on Webex using the following command format:

- For SQL debugging: ```!sqldebug <your SQL query> #error <your error message>```


- For SQL optimization: ```!sqlopt <your SQL query> #opt <your optimization related message>```


- For SQL formatting: ```!sqlformat <your SQL query>```


- For programming assistance: ```!codehelp -l <prog-lang> -q <your question or code>```


- To create a jira story: ```!jspost #{role} <story title>```

      - Optional parameters: !jspost #{role} <story title> -u <user-id> -e <epic-id> -t <team-id> -sp <story-points> 

- To get AI generated jira story content: ```!jsget #{role} <story title>```

