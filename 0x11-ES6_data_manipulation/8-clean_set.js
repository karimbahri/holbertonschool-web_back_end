/* eslint-disable */
export default function cleanSet(set, startString) {
  const data = Array();
  if (startString !== "" && typeof startString === "string") {
    for (let element of set) {
      if (typeof element === "string")
        if (element.startsWith(startString))
          data.push(element.slice(startString.length));
    }
    const joined = data.join("-");
    return joined;
  }
  return "";
}
