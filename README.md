# claptrap-telegram-bot

A Telegram bot to assist you for server related stuff. Currently you can use it to send files to your server. Or you could use scp or sftp like normal people but whatever.
There's also a notify.py script that will send you a message when processes you setup with it have stopped running (how cool is that? Right). 

To use the bot,
- Fill out the config.py.sample and save it as config.py
- Talk to BotFather and make your bot and get the token first. Put it in "key". 
- Put your own user name in admin.
- Fill in the "store" with the path to the directory where you want your uploaded files to go "/path/to/upload/". Make sure it's writable ofcourse. 
- Run the claptrap.py file
- Send /start to your newly made bot. It'll return your chat ID. Put that too in the config file (I'll simplify this step later using some password, pin based pairing, machine learning, blockchain or some other technology). 
- Yeah, now you can send files and stuff to your bot. 
- To use notify.py run the process you want and add ./notify.py as shown in the example. <br> 
Example: ``` nohup process_to_run && ./notify.py "Message for successful completion" || ./notify.py "Message for not so successfull completion" & ```
