/* eslint-disable */
const kue = require("kue");

const sendNotification = (phoneNumber, message) => {
  console.log(
    `Sending notification to ${phoneNumber}, with message: ${message}`
  );
};
const push_notification_code = kue.createQueue();
push_notification_code.process("push_notification_code", function (job, done) {
  const phoneNumber = job.data.phoneNumber;
  const message = job.data.message;
  sendNotification(phoneNumber, message, job, done);
});
