/* eslint-disable */
export default function getStudentsByLocation(arr, city) {
  const cities = arr.filter((item) => item.location === city);
  return cities;
}
