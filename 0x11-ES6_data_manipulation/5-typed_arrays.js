/* eslint-disable */
export default function createInt8TypedArray(length, position, value) {
  try {
    const buff = new ArrayBuffer(length);
    const data_view = new DataView(buff);
    data_view.setInt8(position, value);
    return data_view;
  } catch (err) {
    throw new Error("Position outside range");
  }
}
