/* eslint-disable */
export default function hasValuesFromArray(set, array) {
  let exist = true;
  array.forEach((element) => {
    if (set.has(element) === false) {
      exist = false;
    }
  });
  return exist;
}
