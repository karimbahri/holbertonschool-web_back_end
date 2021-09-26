const http = require("http");

const app = http.createServer((req, res) => {
  const url = req.url;

  if (url === "/") res.end("Hello Holberton School!");
  else if (url === "/students") {
    const countStudents = require("./3-read_file_async");
    countStudents(process.argv[2])
      .then((data) => {
        res.write("This is the list of our students\n");
        res.end(data.join("\n"));
      })
      .catch((err) => {
        res.end(`This is the list of our students\n${err.message}`);
      });
  }
});

app.listen(1245);
module.exports = app;
