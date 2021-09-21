/* eslint-disable */
export default function updateStudentGradeByCity(students, city, newGrades) {
  return students
    .filter((item) => item.location === city)
    .map((item) => {
      item.grade = "N/A";
      newGrades.map((element) => {
        if (element.studentId === item.id) item.grade = element.grade;
      });
      return item;
    });
}
