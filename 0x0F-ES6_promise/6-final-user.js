/* eslint-disable */
import signUpUser from './4-user-promise';
import uploadPhoto from './5-photo-reject';

export default function handleProfileSignup(firstName, lastName, fileName) {
  return new Promise(async (resolve) => {
    const resolved = {
      status: 'fulfilled',
      value: await signUpUser(firstName, lastName),
    };
    let photoPromise = undefined;
    try {
      await uploadPhoto(fileName);
    } catch (err) {
      photoPromise = err.toString();
    }
    const rejected = {
      status: 'rejected',
      //   value: await uploadPhoto(fileName).catch((err) => {
      //     err;
      //   }),
      value: photoPromise,
    };
    return resolve([resolved, rejected]);
  });
}
