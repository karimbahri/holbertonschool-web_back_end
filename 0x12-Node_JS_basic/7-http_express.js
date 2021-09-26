/* eslint-disable */

const app = require("express")();

app.get("/", (req, res) => {
  res.send("Hello Holberton School!");
});
app.get("/students", (req, res) => {
  const countStudents = require("./3-read_file_async");
  countStudents(process.argv[2])
    .then((data) => {
      res.send(`This is the list of our students\n${data.join("\n")}`);
    })
    .catch((err) => {
      res.send(`This is the list of our students\n${err.message}`);
    });
});

app.listen(1245);
module.exports = app;
