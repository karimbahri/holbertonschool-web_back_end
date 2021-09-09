export default function createEmployeesObject(departmentName, employees) {
  const objs = [...employees];
  return {
    [`${departmentName}`]: objs,
  };
}
