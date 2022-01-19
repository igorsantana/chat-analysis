import { ApiClient } from '@twurple/api';
import authProvider from './auth.js';

authProvider.refresh()

const apiClient = new ApiClient({ authProvider });

const getUserId = async (username) => {
  const { id, name } = await apiClient.users.getUserByName(username);
  return { userId: id, streamer: name };
}

const getVodsFromUser = async (username) => {
  const { userId, streamer } = await getUserId(username);
  const { data } = await apiClient.videos.getVideosByUser(userId)
  const vods = data.map((video) => {
    const { id, streamId, views, title } = video;
    return { id, streamId, views, title, streamer };
  })
  return vods;
}

export { getUserId, getVodsFromUser }