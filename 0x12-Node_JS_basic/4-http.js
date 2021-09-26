/* eslint-disable */
const http = require("http");
const app = http.createServer((req, res) => {
  res.end("Hello Holberton School!");
});
app.listen("127.0.0.1:1245");
module.exports = app;
