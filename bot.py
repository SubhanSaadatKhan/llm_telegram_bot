from telegram.ext import Application, CommandHandler, MessageHandler
from telegram.ext.filters import TEXT
import torch
from transformers import pipeline

# Load the model pipeline
pipe = pipeline("text-generation", model="TinyLlama/TinyLlama-1.1B-Chat-v1.0", torch_dtype=torch.bfloat16)

# Replace 'YOUR_API_TOKEN' with your bot's token
API_TOKEN = '7336526901:AAFxXtjWXiQqQKHa1iP9zl9a2BXCL4BOJkc'

async def start(update, context):
    """Handler for the /start command."""
    await update.message.reply_text("Hello! I'm your bot. Send me a message!")

async def process(update, context):
    """Handler for processing user messages."""
    user_message = update.message.text
    # Generate response using the LLM
    outputs = pipe(user_message, min_length=100, max_length=150, do_sample=True, temperature=0.1, top_k=50, top_p=0.9)
    # Extract the generated text
    generated_text = outputs[0]["generated_text"]
    # Send the generated text as a reply
    await update.message.reply_text(generated_text)

def main():
    """Main function to set up the bot."""
    # Set up the bot application
    application = Application.builder().token(API_TOKEN).build()

    # Add handlers for commands and messages
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(TEXT, process))

    # Start polling for updates
    application.run_polling()

if __name__ == '__main__':
    main()
