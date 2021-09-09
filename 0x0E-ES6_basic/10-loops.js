export default function appendToEachArrayValue(array, appendString) {
  let i = 0;
  /* eslint-disable */
  for (const element of array) {
    let value = array[i];
    array[i] = appendString + value;
    i++;
  }

  return array;
}
