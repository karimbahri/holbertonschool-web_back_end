/* eslint-disable */
export default class HolbertonClass {
  constructor(size, location) {
    this._size = size;
    this._location = location;
  }
  [Symbol.toPrimitive](casted_type) {
    return casted_type === 'number' ? this._size : this._location;
  }
}
