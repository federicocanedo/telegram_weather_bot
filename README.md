# Simple telegram weather bot

Created for Hikko's technical test

### Running the bot

I developed the bot to be runned with Docker, it can be runned locally but I haven't tested it with differents python/libraries versions.

Python 3.10, libraries in requiremtents.txt file

To run the bot with docker you can run the following command:
```
docker run -it \
-e TELEGRAM_TOKEN=telegram_token_here \
-e WEATHER_API_KEY=openweather_key_here \
-e OPENAI_API_KEY=openai_key_here \
$(docker build . -q)
```

The counter will be reset every time the cointainer is run, however you could create a volume to save the counter.json file in the project root.
