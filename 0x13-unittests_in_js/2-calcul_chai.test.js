/* eslint-disable */
describe("calculateNumber-test", function () {
  const chai = require("chai");
  const exprect = chai.exprect;
  const calculateNumber = require("./2-calcul_chai");

  it("checking for simple operation", function () {
    exprect(calculateNumber("SUM", 1, 3)).to.equal(4);
    exprect(calculateNumber("SUM", 1.5, 3.5)).to.equal(6);
    exprect(calculateNumber("SUM", 1.4, 3.5)).to.equal(5);
    exprect(calculateNumber("SUM", 1.4, 3.4)).to.equal(4);

    exprect(calculateNumber("SUBTRACT", 1.4, 4.5)).to.equal(-4);

    exprect(calculateNumber("DIVIDE", 1.4, 4.5)).to.equal(0.2);

    exprect(calculateNumber("DIVIDE", 1.4, 0)).to.equal("Error");
  });
  it("checking for edges cases", function () {
    exprect(isNaN(calculateNumber(1, 3))).to.equal(true);
    exprect(isNaN(calculateNumber("DIVID", 1.4, 0))).to.equal(true);
    exprect(isNaN(calculateNumber())).to.equal(true);
    exprect(calculateNumber("SUM", -1.4, -3)).to.equal(-4);
    exprect(calculateNumber("SUBTRACT", -1.4, -4.5)).to.equal(3);
    exprect(calculateNumber("DIVIDE", 1.4, -4.5)).to.equal(-0.25);
    exprect(calculateNumber("DIVIDE", -1.4, 4.5)).to.equal(-0.2);
    exprect(calculateNumber("DIVIDE", -1.4, -4.5)).to.equal(0.25);
  });
});
