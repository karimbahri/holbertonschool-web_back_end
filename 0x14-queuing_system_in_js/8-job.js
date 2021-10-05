/* eslint-disable */
module.exports = (jobs, queue) => {
  if (!(jobs instanceof Array)) {
    throw new Error("Jobs is not an array");
  }
  jobs.forEach((element) => {
    const item = queue
      .create("push_notification_code_2", element)
      .save((err) => {
        if (!err) {
          console.log(`Notification job created: ${item.id}`);
        }
        item.on("complete", () =>
          console.log(`Notification job ${item.id} completed`)
        );
        item.on("failed", (err) =>
          console.log(`Notification job ${item.id} failed: ${err}`)
        );
        item.on("progress", (progg) =>
          console.log(`Notification job ${item.id} ${progg}% complete`)
        );
      });
  });
};
