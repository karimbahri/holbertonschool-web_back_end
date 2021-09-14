/* eslint-disable */
import { uploadPhoto, createUser } from './utils';

async function asyncUploadUser() {
  try {
    let photo = await uploadPhoto();
    let user = await createUser();
    return { photo, user };
  } catch (err) {
    return { photo: null, user: null };
  }
}
export default asyncUploadUser;
