/* eslint-disable */
describe("calculateNumber-test", function () {
  const assert = require("assert");
  const calculateNumber = require("./0-calcul");
  assert.equal(calculateNumber(1, 3), 4);
  assert.equal(calculateNumber(1.5, 3.5), 6);
  assert.equal(calculateNumber(1.4, 3.5), 5);
  assert.equal(calculateNumber(1.4, 3.4), 4);
});
