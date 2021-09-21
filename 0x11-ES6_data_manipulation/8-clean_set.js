/* eslint-disable */
export default function cleanSet(set, startString) {
  const data = Array();
  if (startString !== "") {
    for (let element of set) {
      if (element.startsWith(startString))
        data.push(element.slice(startString.length));
    }
    return data.join("-");
  }
  return "";
}
