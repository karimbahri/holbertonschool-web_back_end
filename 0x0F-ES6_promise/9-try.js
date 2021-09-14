/* eslint-disable */
function guardrail(mathFunction) {
  const queue = Array();
  try {
    queue.push(mathFunction());
  } catch (err) {
    queue.push(String(err));
  }
  queue.push('Guardrail was processed');
  return queue;
}
export default guardrail;
