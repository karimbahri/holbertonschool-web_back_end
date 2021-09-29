/* eslint-disable */
describe("calculateNumber-test", function () {
  const assert = require("assert");
  const calculateNumber = require("./1-calcul");

  it("checking for simple operation", function () {
    assert.equal(calculateNumber("SUM", 1, 3), 4);
    assert.equal(calculateNumber("SUM", 1.5, 3.5), 6);
    assert.equal(calculateNumber("SUM", 1.4, 3.5), 5);
    assert.equal(calculateNumber("SUM", 1.4, 3.4), 4);

    assert.equal(calculateNumber("SUBTRACT", 1.4, 4.5), -4);

    assert.equal(calculateNumber("DIVIDE", 1.4, 4.5), 0.2);

    assert.equal(calculateNumber("DIVIDE", 1.4, 0), "Error");
  });
  it("checking for edges cases", function () {
    assert.equal(isNaN(calculateNumber(1, 3)), true);
    assert.equal(isNaN(calculateNumber("DIVID", 1.4, 0)), true);
  });
});
