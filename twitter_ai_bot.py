import os
import time
import re
import tweepy
import random
import colorama
from datetime import datetime
from colorama import Fore, Style
from groq import Groq
from dotenv import load_dotenv

colorama.init(autoreset=True)

load_dotenv() 

# Load environment variables
GROQ_API_KEY = os.environ.get("GROQ_API_KEY")
TWITTER_API_KEY = os.environ.get("TWITTER_API_KEY")
TWITTER_API_KEY_SECRET = os.environ.get("TWITTER_API_KEY_SECRET")
TWITTER_ACCESS_TOKEN = os.environ.get("TWITTER_ACCESS_TOKEN")
TWITTER_ACCESS_TOKEN_SECRET = os.environ.get("TWITTER_ACCESS_TOKEN_SECRET")

if not all([GROQ_API_KEY, TWITTER_API_KEY, TWITTER_API_KEY_SECRET, TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_TOKEN_SECRET]):
    print(Fore.RED + "Missing one or more required environment variables.")
    exit(1)

# Initialize clients
groq_client = Groq(api_key=GROQ_API_KEY)
twitter_client = tweepy.Client(
    consumer_key=TWITTER_API_KEY,
    consumer_secret=TWITTER_API_KEY_SECRET,
    access_token=TWITTER_ACCESS_TOKEN,
    access_token_secret=TWITTER_ACCESS_TOKEN_SECRET
)

# Hashtag and cashtag pool
hashtags = ['#AI', '#Crypto', '#Automation', '#Groq', '#TwitterBot']
cashtags = ['$BTC', '$ETH', '$SOL']

generated_tweets = []

# Prompt file path (customizable)
PROMPT_FILE = "./prompt.txt"

def load_prompt():
    try:
        with open(PROMPT_FILE, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        print(Fore.RED + f"Prompt file not found at: {PROMPT_FILE}")
        exit(1)

def remove_emojis(text):
    emoji_pattern = re.compile("[\U00010000-\U0010ffff]", flags=re.UNICODE)
    return emoji_pattern.sub(r'', text)

def generate_tweet(tweet_count):
    prompt = load_prompt()
    temperature = max(1.8 - (tweet_count // 5) * 0.1, 0.5)
    retries = 0

    while retries < 5:
        try:
            response = groq_client.chat.completions.create(
                messages=[
                    {"role": "system", "content": prompt},
                    {"role": "user", "content": "Create a tweet based on the above."}
                ],
                model="llama-3.2-3b-preview",
                temperature=temperature,
                max_tokens=200,
                top_p=1,
            )

            tweet = response.choices[0].message.content.strip().strip('"').strip("'")
            if len(tweet) < 5:
                print(Fore.RED + "Generated tweet is too short. Skipping.")
                return None

            if random.random() < 0.3:
                tweet += f" {random.choice(hashtags)} {random.choice(cashtags)}"

            return tweet

        except Exception as e:
            print(Fore.RED + f"Error: {e}")
            retries += 1
            time.sleep(2)

    return None

def post_tweet(tweet):
    try:
        response = twitter_client.create_tweet(text=tweet)
        if response.data:
            print(Fore.GREEN + "Tweet posted successfully!")
        else:
            print(Fore.RED + "Tweet failed to post.")
    except Exception as e:
        print(Fore.RED + f"Error posting tweet: {e}")

def log_tweet(tweet):
    clean = remove_emojis(tweet)
    generated_tweets.append(clean)
    with open("tweets_log.txt", "a", encoding="utf-8") as f:
        f.write(f"{datetime.now().isoformat()} - {clean}\n")

def main():
    count = 0
    print(Fore.CYAN + "Starting AI Twitter Bot...")

    while True:
        tweet = generate_tweet(count)
        if tweet:
            print(Fore.YELLOW + f"\nGenerated Tweet #{count+1}:")
            print(Fore.WHITE + tweet)
            post_tweet(tweet)
            log_tweet(tweet)
            count += 1
        else:
            print(Fore.RED + "Tweet generation failed.")

        print(Fore.CYAN + f"Waiting before next tweet...")
        time.sleep(1800)  # 30 min

if __name__ == "__main__":
    main()
