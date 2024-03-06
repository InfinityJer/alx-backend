#!/usr/bin/yarn dev
import redis from 'redis';

// Create a Redis client
const client = redis.createClient();

// Handle connection events
client.on('connect', () => {
  console.log('Redis client connected to the server');
});

client.on('error', (error) => {
  console.error(`Redis client not connected to the server: ${error}`);
});

// Function to create a hash using hset
const createHash = () => {
  client.hset(
    'HolbertonSchools',
    'Portland', 50,
    'Seattle', 80,
    'New York', 20,
    'Bogota', 20,
    'Cali', 40,
    'Paris', 2,
    redis.print
  );
};

// Function to display the hash using hgetall
const displayHash = () => {
  client.hgetall('HolbertonSchools', (error, reply) => {
    if (error) {
      console.error(error);
    } else {
      console.log(reply);
    }
  });
};

// Call the functions
createHash();
displayHash();

// Close the connection
client.quit();
