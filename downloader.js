import { promises as fs } from 'fs';
import { resolve } from 'path';
import downloadChatLog from './src/chat.js';
import { getVodsFromUser } from './src/twitch.js'

const getStreamers = async () => {
  const path = resolve('.', 'src/metadata/streamers_top100_19012022.json');
  const { streamers } = JSON.parse(await fs.readFile(path, 'UTF-8'));
  return streamers;
}

const splitVodsIntoChunks = (streamers) => {
  const n = 5
  return new Array(Math.ceil(streamers.length / n))
    .fill()
    .map(_ => streamers.splice(0, n))
}

const sleep = (ms) => new Promise((resolve) => setTimeout(resolve, ms));

(async () => {
  const streamers = await getStreamers();

  for (const streamer of streamers) {

    const vods = splitVodsIntoChunks(await getVodsFromUser(streamer));
    const [first5Vods, _] = vods;
    if (!!first5Vods) {
      await Promise.all(first5Vods.map(async (vod) => downloadChatLog(vod)))
    }
    await sleep(10000);
  }
})();