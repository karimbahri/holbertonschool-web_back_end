export default function createIteratorObject(report) {
  /* eslint-disable */
  const array = [];
  let i = 0;
  const employees = report.allEmployees
  for (let key in employees) {
    for (let element of employees[key]) {
        array[i] = element;
        i++;
    }
  }
  return array;
}
