from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import conf

KEY = conf.bot["key"];
ADMIN = conf.bot["admin"];
STORE = conf.bot["store"];

updater = Updater(KEY, use_context=True);
dp = updater.dispatcher

updater.start_polling();

# start command
def start(update, context):
    update.message.reply_text("Hi. This is your chat id: " + str(update.message.chat_id));

dp.add_handler(CommandHandler("start", start));


# fileupload 
def file_upload(update, context):
    
    if (not is_authorized(update)):
        return 
    
    filename = generate_file_name(update.message.document);

    print(filename);
    file_recv = update.message.document.get_file();
    file_recv.download(custom_path = STORE + filename);
    update.message.reply_text("Your file has been saved with the name " + filename);

dp.add_handler(MessageHandler(Filters.document, file_upload));


# todo
def is_authorized(update):
    if (update.message.chat.username == ADMIN): 
        return True;
    return False; 

    
def generate_file_name(document):
    try:
        extension = "." + document.file_name.split(".")[1];
    except IndexError:
        extension = "";

    file_id = document.file_unique_id;
    original_filename = document.file_name.split(".")[0];

    filename = original_filename + "_" + file_id + extension; 
    return filename;
