import { exec } from 'child_process'
import fs from 'fs';
import { resolve } from 'path';
import cli from 'cli-progress'

const multibar = new cli.MultiBar({
  clearOnComplete: false,
  hideCursor: true

}, cli.Presets.shades_grey);


const _chatLog = (vod, fulfill, reject) => {
  const dir = resolve('.', `src/logs/${vod.streamer}`);
  if (!fs.existsSync(dir)) {
    fs.mkdirSync(dir)
  }
  const cmd = `./TwitchDownloaderCLI -m ChatDownload --id ${vod.id} -o ${dir}/${vod.id}.txt`
  const child = exec(cmd);
  console.log(`[${vod.streamer}] [${vod.title}] [${vod.id}]`)
  const progressBar = multibar.create({}, cli.Presets.shades_classic);
  progressBar.start(100, 0);

  child.stdout.on('data', (data) => {
    const percentage = data.split(' ').slice(-1)[0].split('%')[0]
    progressBar.update(parseInt(percentage))
  })

  child.on('close', (code) => {
    progressBar.stop();
    fulfill()
  })
}

const downloadChatLog = (vod) => {
  const promise = new Promise(function (fulfill, reject) {
    _chatLog(vod, fulfill, reject);
  })
  return promise
}

export default downloadChatLog;
