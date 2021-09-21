/* eslint-disable */
export default function updateUniqueItems(structMap) {
  if (structMap instanceof Map) {
    for (let [key, val] of structMap) {
      if (val === 1) {
        structMap.set(key, 100);
      }
    }
  } else {
    throw new Error("Cannot process");
  }
  return structMap;
}
