# webex-bot

<p align="left">
  <a href="https://fishwongy.github.io/" target="_blank"><img src="https://img.shields.io/badge/Blog-Read%20About%20This%20Project-blue.svg" /></a>
  <!--<a href="https://twitter.com/intent/follow?screen_name=miguelgfierro" target="_blank"><img src="https://img.shields.io/twitter/follow/miguelgfierro?style=social" /></a>-->
</p>

Chat GPT AI assistant w/ Webex integration

This project is a Webex Chatbot that uses OpenAI's GPT-3.5 model to provide automated responses. It was developed in Python and uses the OpenAI API, Webex API and Jira API for chat operations.

## ✨ Demo
![webex-bot-demo](https://github.com/FISHWONGY/webex-bot/assets/59711659/fd409633-07a2-422f-92f1-5091dd3dac33)

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

## 💡 Software Architecture
![aiops-bot-architecture](https://github.com/FISHWONGY/webex-bot/assets/59711659/2c5fbe3c-2e9f-4138-b2de-eaf194177467)


## 🚀 Installation
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


- For programming assistance: ```!codeq -l <prog-lang> -q <your question or code>```


- To create a jira story: ```!jspost #{role} <story title>```

      - Optional parameters: !jspost #{role} <story title> -u <user-id> -e <epic-id> -t <team-id> -sp <story-points> 

- To get AI generated jira story content: ```!jsget #{role} <story title>```

