/* eslint-disable */
import signUpUser from './4-user-promise';
import uploadPhoto from './5-photo-reject';

export default function handleProfileSignup(firstName, lastName, fileName) {
  return new Promise(() => {
    let signupPromise = undefined;
    let uploadPromise = undefined;

    signUpUser(firstName, lastName).then((data) => {
      signupPromise = data;
    });
    uploadPhoto(fileName).catch((err) => {
      uploadPromise = err.message;
    });
    const resolved = {
      status: 'fulfilled',
      value: signupPromise,
    };
    const rejected = {
      status: 'rejected',
      value: uploadPromise,
    };
    return [resolved, rejected];
  });
}
