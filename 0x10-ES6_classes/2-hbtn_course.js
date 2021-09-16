/* eslint-disable */
export default class HolbertonCourse {
  constructor(name, length, students) {
    this.name = name;
    this.length = length;
    this.students = students;
  }
  set name(name) {
    if (typeof name !== 'string') throw new Error('Name must be a string');
    this._name = name;
  }
  get name() {
    return this._name;
  }
  set length(length) {
    if (typeof length !== 'number') throw new Error('Length must be a number');
    this._length = length;
  }
  get length() {
    return this._length;
  }
  set students(students) {
    if (
      !(students instanceof Array) ||
      students.forEach((el) => typeof el !== 'string')
    ) {
      throw new Error('Students must be an array of strings');
    }
    this._students = students;
  }
}
