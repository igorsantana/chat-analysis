# chat-analysis
This project aims to transform interactions in streamers chat into data. By downloading the chat from the VODs, I want to see if there are streamers that have similar chat interactions.
Another goal of this project is to build a ML model that will train with the downloaded chat, and will generate messages to post in those streamers chat given the last few messages that are being posted in chat.

## How to run:

* Download [TwitchDownloader](https://github.com/lay295/TwitchDownloader) and put it in the base folder (CLI).
* In the metadata folder, it must contain two json files:
  * `tokens.json`: File that contain the tokens that authorize your application to use the Twitch API, as explained [here](https://twurple.js.org/docs/auth/providers/refreshing.html)
  * `streamers.json`: File that contain a list of streamers that you want to download the chat from the recent VODS. `{ "streamers": [] }`
* `.env`: The dotenv file must contain the `CLIENT_ID` and `CLIENT_SECRET` for the Twitch API.

## Goals:

* [ ] Filter chat log of default messages, like subscription and gifting subs.
* [ ] Decide the model to get the embeddings
* [ ] Apply the model to the chat messages
* [ ] Get some info from data lol dont know yet
