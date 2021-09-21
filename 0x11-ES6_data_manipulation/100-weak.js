/* eslint-disable */
export const weakMap = new WeakMap();
export function queryAPI(end_point) {
  if (weakMap.has(end_point) === false) weakMap.set(end_point, 0);
  weakMap.set(end_point, 1 + weakMap.get(end_point));
  const edp = weakMap.get(end_point);
  if (edp >= 5) throw new Error("Endpoint load is high");
}
