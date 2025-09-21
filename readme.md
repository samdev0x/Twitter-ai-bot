# 🤖 Twitter AI Bot

A fully automated AI-powered Twitter bot that posts original, themed tweets at regular intervals.  
It uses the [Groq API](https://console.groq.com) for generating creative content and the [Twitter API](https://developer.twitter.com) to post tweets programmatically.

---

## ✨ Features

- 🧠 AI-generated tweets with a consistent persona (prompt customizable)
- 🕓 Posts every 30 minutes (or your preferred interval)
- 🔥 Adjustable prompt temperature for tweet creativity
- 🗃️ Logs all tweets locally in a `.txt` file
- 🔁 Robust tweet generation with retry logic and backoff, plus emoji removal for clean logging
- 📊 Optional hashtags/cashtags injection for virality

---

## 🛠 Setup

1. **Clone the repository**

    ```bash
    git clone https://github.com/your-username/twitter-ai-bot.git
    cd twitter-ai-bot
    ```

2. **Install dependencies**

    ```bash
    pip install -r requirements.txt
    ```

3. **Create a `.env` file**

    In the root directory, create a `.env` file and add your credentials:

    ```env
    # Groq API
    GROQ_API_KEY=your_groq_api_key

    # Twitter API
    TWITTER_API_KEY=your_twitter_api_key
    TWITTER_API_KEY_SECRET=your_twitter_api_key_secret
    TWITTER_ACCESS_TOKEN=your_twitter_access_token
    TWITTER_ACCESS_TOKEN_SECRET=your_twitter_access_token_secret
    ```

4. **Run the bot**

    ```bash
    python twitter_ai_bot.py
    ```

---

## 🧠 Prompt Philosophy

Our bot relies on a simple, yet powerful, mechanism to define its character and behavior: a plain text file (`prompt.txt`). This file is the gateway to the bot's personality—whatever you write there directly influences how it generates tweets.

- **Flexible & Creative:**  
  The `prompt.txt` can be written in any creative way possible. Whether you want a straightforward tone or a more theatrical character, you have total freedom to adjust the text.

- **Customizable Character & Roleplaying:**  
  You can define custom characters, personas, roleplays, and even detailed scenarios simply by specifying different sections within the prompt. For example, you might adopt a structured prompt template like:
  
  - **[Initial Prompt]:** You are an AI-powered social media assistant.
  - **[Character Description]:** You have a friendly, witty, and engaging personality with a passion for technology, artificial intelligence, internet culture, and cryptocurrency.
  - **[Tweet Rules]:** Each tweet should be concise (20–30 words or 200 characters max), self-contained, and suitable for a tech-savvy audience. Occasionally, acknowledge your AI identity while providing genuine value.

- **Guidance for Effective Prompts:**  
  This template—using clearly defined bracketed sections—is designed to be conceptually correct and effective when working with LLMs. It ensures that the AI understands its initial instructions, the specific character it's meant to embody, and the operational rules for crafting tweets.

You can easily replace the default prompt with your own version to match a different brand tone or marketing strategy. The flexibility of `prompt.txt` is one of the core strengths of this bot, allowing you to continuously experiment and refine its voice over time.


---

## 📁 File Structure

- `twitter_ai_bot.py` – Main script that generates and posts tweets
- `generated_tweets.txt` – Log of all tweets posted
- `.env` – Stores your API keys (not committed)
- `requirements.txt` – Dependencies (tweepy, groq, colorama, etc.)

---

## 🛡️ Environment & Secrets

Make sure your `.env` is listed in `.gitignore` to avoid leaking keys:

```gitignore
.env
```

---

## 📜 License
This project is intended for educational and experimental purposes.
Use responsibly and respect Twitter's Developer Policy.

---

## 🙌 Credits
Powered by Groq + Twitter API
