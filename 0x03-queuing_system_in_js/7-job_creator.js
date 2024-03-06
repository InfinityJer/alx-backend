#!/usr/bin/yarn dev
import kue from 'kue';

// Array of jobs data
const jobs = [
  {
    phoneNumber: '4153518780',
    message: 'This is the code 1234 to verify your account'
  },
  {
    phoneNumber: '4153518781',
    message: 'This is the code 4562 to verify your account'
  },
  // Add more job data as needed
];

// Create a queue with Kue
const queue = kue.createQueue();

// Loop through the jobs array and create jobs
jobs.forEach((jobData, index) => {
  const job = queue.create('push_notification_code_2', jobData)
    .save((err) => {
      if (!err) {
        console.log(`Notification job created: ${job.id}`);
      }
    });

  // Job completion
  job.on('complete', () => {
    console.log(`Notification job ${job.id} completed`);
  });

  // Job failure
  job.on('failed', (err) => {
    console.log(`Notification job ${job.id} failed: ${err}`);
  });

  // Job progress
  job.on('progress', (progress) => {
    console.log(`Notification job ${job.id} ${progress}% complete`);
  });
});
