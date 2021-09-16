/* eslint-disable */
export default class HolbertonCourse {
  constructor(name, length, students) {
    this.name = name;
    this.length = length;
    this.students = students;
  }
  set name(name) {
    if (typeof name !== 'string') throw new TypeError('Name must be a string');
    this._name = name;
  }
  get name() {
    return this._name;
  }
  set length(length) {
    if (typeof length !== 'number')
      throw new TypeError('Length must be a number');
    this._length = length;
  }
  get length() {
    return this._length;
  }
  set students(students) {
    if (
      !(students instanceof Array) ||
      check_elements_type('string', students)
    ) {
      throw new TypeError('Students must be an array of strings');
    }
    this._students = students;
  }
  get students() {
    return this._students;
  }
}

const check_elements_type = (type, array) => {
  for (let el of array) if (typeof el !== 'string') return true;
};
