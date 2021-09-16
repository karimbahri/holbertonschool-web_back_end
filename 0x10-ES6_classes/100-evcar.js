import Car from './10-car';
/* eslint-disable */
export default class EVCar extends Car {
  constructor(brand, motor, color, range) {
    super()._brand = brand;
    this._motor = motor;
    this._color = color;
    this._range = range;
  }
  cloneCar() {
    return new Car();
  }
}
