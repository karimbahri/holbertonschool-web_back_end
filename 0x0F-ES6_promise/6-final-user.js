/* eslint-disable */
import signUpUser from './4-user-promise';
import uploadPhoto from './5-photo-reject';

export default function handleProfileSignup(firstName, lastName, fileName) {
  return new Promise(async () => {
    const resolved = {
      status: 'fulfilled',
      value: await signUpUser(firstName, lastName),
    };
    const rejected = {
      status: 'rejected',
      value: await uploadPhoto(fileName).catch((err) => {
        err.toString();
      }),
    };
    return [resolved, rejected];
  });
}
