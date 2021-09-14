/* eslint-disable */
const uploadPhoto = require('./utils').uploadPhoto;
const createUser = require('./utils').createUser;

function handleProfileSignup() {
  return Promise.all([uploadPhoto(), createUser()])
    .then((data) => {
      console.log(`${data[0].body} ${data[1].firstName} ${data[1].lastName}`);
    })
    .catch(() => console.log('Signup system offline'));
}
export default handleProfileSignup;
