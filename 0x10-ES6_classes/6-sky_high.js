/* eslint-disable */
import Building from './5-building';
export default class SkyHighBuilding extends Building {
  constructor(sqft, floors) {
    super(sqft);
    this.floors = floors;
  }
  get floors() {
    return this._floors;
  }
  set floors(floors) {
    this._floors = floors;
  }
  evacuationWarningMessage() {
    return `Evacuate slowly the ${this.floors} floors`;
  }
}
