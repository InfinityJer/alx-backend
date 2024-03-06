#!/usr/bin/yarn dev
import kue from 'kue';

// Array of blacklisted phone numbers
const blacklistedNumbers = ['4153518780', '4153518781'];

// Create a queue with Kue
const queue = kue.createQueue();

// Function to send notification
function sendNotification(phoneNumber, message, job, done) {
  // Track progress of the job
  job.progress(0, 100);

  // Check if phone number is blacklisted
  if (blacklistedNumbers.includes(phoneNumber)) {
    return done(new Error(`Phone number ${phoneNumber} is blacklisted`));
  }

  // Progress to 50%
  job.progress(50, 100);

  // Log notification
  console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);

  // Complete the job
  done();
}

// Process jobs from the queue
queue.process('push_notification_code_2', 2, (job, done) => {
  const { phoneNumber, message } = job.data;

  // Call sendNotification function
  sendNotification(phoneNumber, message, job, done);
});
