# 🤖 Twitter AI Bot

A fully automated AI-powered Twitter bot that posts original, themed tweets at regular intervals.  
It uses the [Groq API](https://console.groq.com) for generating creative content and the [Twitter API](https://developer.twitter.com) to post tweets programmatically.

---

## ✨ Features

- 🧠 AI-generated tweets with a consistent persona (prompt customizable)
- 🕓 Posts every 30 minutes (or your preferred interval)
- 🔥 Adjustable prompt temperature for tweet creativity
- 🗃️ Logs all tweets locally in a `.txt` file
- 🔁 Retry logic with backoff and emoji removal
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

The bot runs on a customizable character prompt.  
By default, it uses an "AI girl" persona with dark humor and crypto themes.  
You can replace the prompt with your own character, brand tone, or marketing strategy.

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
generated_tweets.txt
```

---

## 📜 License
This project is intended for educational and experimental purposes.
Use responsibly and respect Twitter's Developer Policy.

---

## 🙌 Credits
Powered by Groq + Twitter API