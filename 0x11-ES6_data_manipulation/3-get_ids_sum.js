/* eslint-disable */
export default function getStudentIdsSum(students) {
  return students.reduce((sum, student) => {
    return sum + student.id;
  }, 0);
}
