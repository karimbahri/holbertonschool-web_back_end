/* eslint-disable */
describe("calculateNumber-test", function () {
  const assert = require("assert");
  const calculateNumber = require("./1-calcul");
  assert.equal(calculateNumber("SUM", 1, 3), 4);
  assert.equal(calculateNumber("SUM", 1.5, 3.5), 6);
  assert.equal(calculateNumber("SUM", 1.4, 3.5), 5);
  assert.equal(calculateNumber("SUM", 1.4, 3.4), 4);

  assert.equal(calculateNumber("SUBTRACT", 1.4, 4.5), -4);

  assert.equal(calculateNumber("DIVIDE", 1.4, 4.5), 0.2);

  assert.equal(calculateNumber("DIVIDE", 1.4, 0), "error");
});
