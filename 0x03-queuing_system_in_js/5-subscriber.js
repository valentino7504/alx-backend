import { createClient } from "redis";

const client = createClient();
client.on('error', (err) => console.log(`Redis client not connected to the server: ${err}`));

client.on('connect', () => console.log('Redis client connected to the server'));

const listener = (channel, msg) => {
  if (msg) {
    console.log(msg);
  }
  if (msg === 'KILL_SERVER') {
    client.unsubscribe('holberton school channel');
    client.quit();
  }
};

client.subscribe('holberton school channel');
client.on('message', listener);
