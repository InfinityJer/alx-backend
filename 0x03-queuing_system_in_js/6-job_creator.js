#!/usr/bin/yarn dev
import kue from 'kue';

// Create a queue with Kue
const queue = kue.createQueue();

// Create an object containing the job data
const jobData = {
  phoneNumber: '1234567890', // Sample phone number
  message: 'Hello from your job creator!', // Sample message
};

// Create a job and push it to the queue
const job = queue.create('push_notification_code', jobData);

// Handle job creation events
job.on('enqueue', (jobId) => {
  console.log(`Notification job created: ${jobId}`);
});

// Handle job completion events
job.on('complete', () => {
  console.log('Notification job completed');
});

// Handle job failure events
job.on('failed', () => {
  console.log('Notification job failed');
});

// Save the job to the queue
job.save();
