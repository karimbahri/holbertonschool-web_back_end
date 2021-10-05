/* eslint-disable */
const kue = require("kue");
const data = {
  phoneNumber: "",
  message: "",
};

const push_notification_code = kue.createQueue();
const notification_code = push_notification_code
  .create("push_notification_code", data)
  .save((err) => {
    console.log(`Notification job created: ${notification_code.id}`);
  });

notification_code.on("complete", function () {
  console.log("Notification job completed");
});
notification_code.on("failed", function () {
  console.log("Notification job failed");
});
