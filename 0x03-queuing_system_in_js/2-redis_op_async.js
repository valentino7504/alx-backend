import { createClient, print } from 'redis';
import { promisify } from 'util';

const client = createClient();
client.on('error', (err) => console.log(`Redis client not connected to the server: ${err}`));

client.on('connect', () => console.log('Redis client connected to the server'));

/**
 * @type {function(string): Promise<string>}
 */
client.get = promisify(client.get).bind(client);

const setNewSchool = async (schoolName, value) => {
  client.set(schoolName, value, print);
}

const displaySchoolValue = async (schoolName) => {
  try {
    const value = await client.get(schoolName);
    console.log(value);
  } catch (error) {
    console.log(error);
    throw error;
  }
};

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
