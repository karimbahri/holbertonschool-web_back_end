import AppController from "../controllers/AppController";
import StudentsController from "../controllers/StudentsController";

const app = require("express")();

app.get("/", (request, response) => {
  AppController.getHomepage(request, response);
});
const path = process.argv[2];
app.get("/students", (request, response) => {
  StudentsController.getAllStudents(request, response, path);
});
app.get("/students/:major", (request, response) => {
  StudentsController.getAllStudentsByMajor(request, response, path);
});

export default app;
