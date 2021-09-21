/* eslint-disable */
export default function getListStudentIds(arr) {
  if (arr instanceof Array) {
    return arr.map((el) => el.id);
  }
  return [];
}
