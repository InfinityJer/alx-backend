#!/usr/bin/yarn dev
import redis from 'redis';

// Create a Redis subscriber client
const subscriber = redis.createClient();

// Handle connection events
subscriber.on('connect', () => {
  console.log('Redis client connected to the server');
});

subscriber.on('error', (error) => {
  console.error(`Redis client not connected to the server: ${error}`);
});

// Subscribe to the channel
subscriber.subscribe('holberton school channel');

// Handle message events
subscriber.on('message', (channel, message) => {
  console.log(message);
  if (message === 'KILL_SERVER') {
    subscriber.unsubscribe();
    subscriber.quit();
  }
});
