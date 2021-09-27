/* eslint-disable */
export default function (path) {
  return new Promise((resolve, reject) => {
    require("fs").readFile(path, "utf-8", (err, data) => {
      if (err) {
        reject(Error(err));
      } else {
        const dbs = data.split(/\r?\n/);
        // nbFields[0] -> SWE, nbFields[1] -> CS
        const nbFields = [0, 0];
        const csList = [];
        const SWEList = [];
        let count = 0;
        for (let element of dbs) {
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
        const resoved = {
          csList,
          SWEList,
        };
        resolve(resoved);
      }
    });
  });
}
