# 🤖 Gemini Chatbot

A simple, fast, and clean chatbot powered by Google's Gemini AI. Chat about anything - movies, sports, coding, or just have a conversation!

![Python](https://img.shields.io/badge/python-3.8+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

## ✨ Features

- 💬 **Natural conversations** - Chat like you would with Google Gemini
- 🧮 **Calculator tool** - Perform calculations
- 👋 **Greeting functionality** - Friendly greetings
- 🧠 **Conversation memory** - Remembers context throughout the chat
- ⚡ **Fast startup** - Connects instantly
- 🎯 **Clean output** - No clutter, just responses
- 🔧 **Simple code** - Easy to understand and modify

## 📋 Prerequisites

- Python 3.8 or higher
- A Google AI Studio API key (free)

## 🚀 Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/gemini-chatbot.git
   cd gemini-chatbot
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up your API key**
   - Go to [Google AI Studio](https://aistudio.google.com/app/apikey)
   - Click "Create API key in new project"
   - Copy your API key
   - Create a `.env` file in the project directory:
     ```
     GOOGLE_API_KEY=your_api_key_here
     ```

4. **Run the chatbot**
   ```bash
   python chatbot.py
   ```

## 💡 Usage

Simply type your message and press Enter. The chatbot will respond naturally.

```
You: Why is Lightning McQueen the best?
Assistant: Lightning McQueen is a fantastic character! He's got incredible racing skills,
a great character arc from arrogant rookie to humble champion, and he learns the value
of friendship and teamwork. Plus, ka-chow! 🏎️

You: Add 25 and 17
Assistant: 42

You: quit
Goodbye!
```

### Available Commands

- Type any question or message to chat
- Type `quit`, `exit`, or `q` to end the conversation
- The chatbot can use tools like calculator when needed

## 🛠️ Built With

- [LangChain](https://python.langchain.com/) - Framework for LLM applications
- [Google Gemini](https://deepmind.google/technologies/gemini/) - Google's AI model
- [Python-dotenv](https://github.com/theskumar/python-dotenv) - Environment variable management

## 📁 Project Structure

```
gemini-chatbot/
├── chatbot.py          # Main chatbot application
├── requirements.txt    # Python dependencies
├── .env               # API key (create this yourself, not in repo)
├── .gitignore         # Git ignore file
├── LICENSE            # MIT License
└── README.md          # This file
```

## 🔧 Customization

### Adding New Tools

You can easily add new tools by defining them with the `@tool` decorator:

```python
@tool
def my_custom_tool(param: str) -> str:
    """Description of what this tool does."""
    return f"Result: {param}"
```

### Changing the Model

Edit the `models` list in `chatbot.py` to use different Gemini models:

```python
models = ["gemini-2.5-flash", "gemini-2.0-flash-exp", "gemini-flash-latest"]
```

### Adjusting Temperature

Change the `temperature` parameter (0.0 - 1.0) for more creative or focused responses:

```python
llm = ChatGoogleGenerativeAI(model=model, temperature=0.5)  # More focused
llm = ChatGoogleGenerativeAI(model=model, temperature=1.0)  # More creative
```

## ❓ Troubleshooting

### "API key expired" error
- Go to Google AI Studio and create a new API key
- Update your `.env` file with the new key

### "Rate limit exceeded" error
- You've hit the free tier limit (usually 15-60 requests per minute)
- Wait a minute and try again
- Consider upgrading your API plan

### Chatbot freezes
- Press `Ctrl+C` to interrupt
- Check your internet connection
- Verify your API key is valid

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🤝 Contributing

Contributions are welcome! Feel free to:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📧 Contact

Project Link: [https://github.com/yourusername/gemini-chatbot](https://github.com/yourusername/gemini-chatbot)

## 🙏 Acknowledgments

- Google Gemini team for the amazing AI model
- LangChain community for the excellent framework
- All contributors and users of this project

---

Made with ❤️ and Python
