# Draftbot
## Usage 
```bash
git clone https://github.com/winzyu/draftbot.git
cd draftbot
```
## Discord Bot Documentation
You will need to create your own discord bot, invite it to your desired server and obtain your discord API key, for more information, refer to the following:
https://discord.com/developers/docs/reference

After inviting the bot to your desired server and configuring your discord API token, you can run the program:

```python3 draftbot.py```

and use the command in any of your discord text channels:
```\map <map-name>```

The program leverages the Levenshtein distance library to find the closest match to whatever you input for ```<map-name>```
