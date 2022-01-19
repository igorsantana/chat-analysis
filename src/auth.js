import { RefreshingAuthProvider } from '@twurple/auth';
import { promises as fs } from 'fs';
import { resolve } from 'path';
import dotenv from 'dotenv';

dotenv.config()

const clientId = process.env.CLIENT_ID;
const clientSecret = process.env.CLIENT_SECRET;
const tokenPath = resolve('.', 'src/metadata/tokens.json');
const tokenData = JSON.parse(await fs.readFile(tokenPath, 'UTF-8'));

const authConfig = {
  clientId, clientSecret,
  onRefresh: async (newTokenData) => await fs.writeFile(tokenPath, JSON.stringify(newTokenData, null, 4), 'UTF-8')
};
const authProvider = new RefreshingAuthProvider(authConfig, tokenData)

export default authProvider;