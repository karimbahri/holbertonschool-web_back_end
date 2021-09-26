/* eslint-disable */
module.exports = (path) => {
  const fs = require("fs");
  return new Promise((resolve, reject) => {
    fs.readFile(path, "utf-8", (err, data) => {
      if (err) {
        reject(Error("Cannot load the database"));
      } else {
        const dbs = data.split(/\r?\n/);
        // nbFields[0] -> SWE, nbFields[1] -> CS
        const nbFields = [0, 0];
        const csList = [];
        const SWEList = [];
        let count = 0;
        for (element of dbs) {
          const fields = element.split(",");
          if (fields[3] === "SWE") {
            nbFields[0]++;
            SWEList.push(fields[0]);
            count++;
          } else if (fields[3] === "CS") {
            nbFields[1]++;
            csList.push(fields[0]);
            count++;
          }
        }
        const resolveData = [];
        resolveData.push(`Number of students: ${count}`);
        console.log(resolveData[0]);
        if (csList.length) {
          resolveData.push(
            `Number of students in CS: ${nbFields[1]}. List: ${csList.join(
              ", "
            )}`
          );
          console.log(resolveData[1]);
        }
        if (SWEList.length) {
          resolveData.push(
            `Number of students in SWE: ${nbFields[0]}. List: ${SWEList.join(
              ", "
            )}`
          );
          console.log(resolveData[2]);
        }
        resolve(resolveData);
      }
    });
  });
};
