/* eslint-disable */
module.exports = (path) => {
  const fs = require("fs");
  try {
    const dbs = fs.readFileSync(path, "utf-8").split(/\r?\n/);
    // nbFields[0] -> SWE, nbFields[1] -> CS
    const nbFields = [0, 0];
    const csList = [];
    const SWEList = [];
    console.log(`Number of students: ${dbs.length - 1}`);
    for (element of dbs) {
      const fields = element.split(",");
      if (fields[3] === "SWE") {
        nbFields[0]++;
        SWEList.push(fields[0]);
      } else if (fields[3] === "CS") {
        nbFields[1]++;
        csList.push(fields[0]);
      }
    }
    if (csList.length)
      console.log(
        `Number of students in CS: ${nbFields[1]}. List: ${csList.join(", ")}`
      );
    if (SWEList.length)
      console.log(
        `Number of students in SWE: ${nbFields[0]}. List: ${SWEList.join(", ")}`
      );
  } catch (err) {
    console.log("Cannot load the database");
  }
};
