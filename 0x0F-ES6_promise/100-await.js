/* eslint-disable */
import uploadPhoto from './utils';
import createUser from './utils';
let photo;
let user;
async function asyncUploadUser() {
  try {
    photo = await uploadPhoto();
    user = await createUser();
    return { photo, user };
  } catch (err) {
    return { photo: null, user: null };
  }
}
export default asyncUploadUser;
