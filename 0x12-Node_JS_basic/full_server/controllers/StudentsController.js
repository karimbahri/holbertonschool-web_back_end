/* eslint-disable */
import readDatabase from "../utils";
export default class StudentsController {
  static getAllStudents(request, response, path) {
    const resolvedData = [];
    readDatabase(path)
      .then((data) => {
        for (let key in data) {
          resolvedData.push(
            `Number of students in ${key}: ${data[key].length}. List: ${data[
              key
            ].join(", ")}`
          );
        }
        response
          .status(200)
          .send(`This is the list of our students\n${resolvedData.join("\n")}`);
      })
      .catch((err) => {
        response.status(500).send("Cannot load the database");
      });
  }
  static getAllStudentsByMajor(request, response, path) {
    const params = request.params;
    if (params.major !== "CS" && params.major !== "SWE") {
      response.status(500).send("Major parameter must be CS or SWE");
    } else {
      readDatabase(path)
        .then((data) => {
          if (params.major === "SWE") {
            response.status(200).send(`List: ${data.SWE.join(", ")}`);
          } else if (params.major === "CS") {
            response.status(200).send(`List: ${data.CS.join(", ")}`);
          }
        })
        .catch((err) => {
          response.status(500).send("Cannot load the database");
        });
    }
  }
}
