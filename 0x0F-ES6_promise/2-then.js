/* eslint-disable */
function handleResponseFromAPI(promise) {
  promise
    .then(() => {
      return {
        status: 200,
        body: 'success',
      };
    })
    .catch(() => new Error())
    .finally(() => {
      console.log('Got a response from the API');
    });
}
export default handleResponseFromAPI;
