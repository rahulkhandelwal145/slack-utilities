import os
from dotenv import load_dotenv
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler
from HuggingFaceAI import get_rephrase_text

# Load environment variables from .env file
load_dotenv()

# Access tokens from environment
SLACK_BOT_TOKEN = os.getenv("SLACK_BOT_TOKEN")
SLACK_APP_TOKEN = os.getenv("SLACK_APP_TOKEN")

# Initialize Slack app
app = App(token=SLACK_BOT_TOKEN)

@app.command("/rephrase")
def handle_mention(ack, command, say):
    ack()  # Acknowledge the command request from Slack
    user = command["user_id"]
    text = command["text"]
    rephrased_text = get_rephrase_text(text)
    say(f"{rephrased_text}")


if __name__ == "__main__":
    handler = SocketModeHandler(app, SLACK_APP_TOKEN)
    handler.start()
