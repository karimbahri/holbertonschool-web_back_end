/* eslint-disable */
function createEmployeesObject(departmentName, employees) {
  const objs = [...employees];
  return {
    [`${departmentName}`]: objs,
  };
}

export default function createReportObject(employeesList) {
    const size = Object.keys(employeesList).length;
  return {
      allEmployees: employeesList,
      getNumberOfDepartments: () => size,
  };
};
