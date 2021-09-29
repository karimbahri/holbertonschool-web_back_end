/* eslint-disable */
module.exports = function (type, a, b) {
  return type === "SUM"
    ? Math.round(a) + Math.round(b)
    : type === "SUBTRACT"
    ? Math.round(a) - Math.round(b)
    : type === "DIVIDE"
    ? b !== 0
      ? Math.round(a) / Math.round(b)
      : "Error"
    : undefined;
};
