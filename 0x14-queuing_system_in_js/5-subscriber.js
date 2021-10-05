/* eslint disable */
import redis from "redis";
const promisify = require("util").promisify;
const client = redis.createClient();

client.on("connect", () => console.log("Redis client connected to the server"));
client.on("error", (err) =>
  console.log(`Redis client not connected to the server: ${err}`)
);
client.on("message", function (channel, message) {
  if (message === "KILL_SERVER") {
    client.unsubscribe();
    client.quit();
  }
  console.log(message);
});
client.subscribe("holberton school channel");
