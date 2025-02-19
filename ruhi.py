from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup 
from telegram.ext import ( 
    ApplicationBuilder, 
    CommandHandler, 
    MessageHandler, 
    filters, 
    CallbackQueryHandler, 
    ContextTypes, 
) 
 
# Bot start message with an image and buttons 
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE): 
    # Image to send when the bot starts 
    image_url = "https://envs.sh/Y5G.jpg"  # Replace with the image URL you want to show 
     
    # Inline keyboard for buttons 
    keyboard = [ 
        [InlineKeyboardButton("Animate", callback_data="animate")], 
        [InlineKeyboardButton("Image", callback_data="image")], 
        [InlineKeyboardButton("Joke", callback_data="joke")], 
        [InlineKeyboardButton("Visit Website", url="https://anshu908.github.io/graphic-designer-portfolio/")], 
        [InlineKeyboardButton("Send Text", callback_data="text")], 
        [InlineKeyboardButton("Owner", callback_data="owner")], 
        [InlineKeyboardButton("Support💢", url="https://anshu908.github.io/Resume-portfolio-/")],  # Support URL 
        [InlineKeyboardButton("Update🤍", url="https://t.me/ansh_hack")]  # Update URL 
    ] 
    reply_markup = InlineKeyboardMarkup(keyboard) 
 
    # Send the image and the message with buttons 
    await update.message.reply_photo( 
        photo=image_url,  
        caption="Hello! Please use the buttons below. 😊",  
        reply_markup=reply_markup 
    ) 
 
# Inline button handler 
async def button(update: Update, context: ContextTypes.DEFAULT_TYPE): 
    query = update.callback_query 
    await query.answer() 
 
    # Animation button with multiple types 
    if query.data == "animate": 
        animation_options = [ 
            "https://media.giphy.com/media/26AHONQ79FdWZhAI0/giphy.gif",  # General GIF 
            "https://media.giphy.com/media/1tS5p58nauzLu/giphy.gif",  # Funny GIF 
            "https://media.giphy.com/media/l0HlAfw9XWl3PUF0U/giphy.gif",  # Dancing GIF 
            "https://media.giphy.com/media/3o7ZehL4r5YhG9lzO0/giphy.gif",  # Cool animation 
            "https://media.giphy.com/media/26AOV0hvB8ubUqMj2/giphy.gif",  # Cute Animal 
        ] 
         
        # Select one of the animations randomly 
        import random 
        selected_animation = random.choice(animation_options) 
         
        await query.message.reply_animation( 
            animation=selected_animation, caption="Enjoy this animation! 🎬" 
        ) 
     
    # Image button: Change image every time clicked 
    elif query.data == "image": 
        image_options = [ 
            "https://envs.sh/Y5n.jpg",  # Example Image 1 
            "https://graph.org/file/7b3d3f778a4bcc46a7f5d.jpg",  # Example Image 2 
            "https://graph.org/file/9ab991293a986ebf6bfc9.mp4",  # Example Image 3 
            "https://envs.sh/z7t.jpg",  # Example Image 4 
            "https://graph.org/file/a8528768ccdbd8b179654.jpg",  # Example Image 5 
        ] 
         
        # Select a new random image each time 
        selected_image = random.choice(image_options) 
         
        await query.message.reply_photo( 
            photo=selected_image, caption="Here's a new image for you! 🖼️" 
        ) 
     
    # Joke button 
    elif query.data == "joke": 
        joke = "Do you know when an error occurs in programming?\nWhen code is written without tea! ☕😅" 
        await query.message.reply_text(joke) 
     
    # Text button 
    elif query.data == "text": 
        await query.message.reply_text("If you face any problem, you can talk to the OWNER (●'◡'●) @cyber_ansh 📜") 
     
    # Owner button 
    elif query.data == "owner": 
        await query.message.reply_text("You can contact the OWNER here: @cyber_ansh") 
 
# Message response handler 
async def respond(update: Update, context: ContextTypes.DEFAULT_TYPE): 
    user_message = update.message.text 
    response = f"You said: '{user_message}'\nMy reply: Wow! You're very smart! 🤖" 
    keyboard = [[InlineKeyboardButton("Start Over", callback_data="start")]] 
    reply_markup =InlineKeyboardMarkup(keyboard) 
 
    await update.message.reply_text(response, reply_markup=reply_markup) 
 
# Main bot setup 
def main(): 
    TOKEN = "8007060492:AAFNr28xUM6QnX4w6AIRrj2Um43ZpEa_5ZU"  # Replace with your bot token 
    application = ApplicationBuilder().token(TOKEN).build() 
 
    # Handlers 
    application.add_handler(CommandHandler("start", start)) 
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, respond)) 
    application.add_handler(CallbackQueryHandler(button)) 
 
    # Start the bot 
    application.run_polling() 
 
if__name__ == "__main__": 
    main()
