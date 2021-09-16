import ClassRoom from './0-classroom';
/*  eslint-disable */
export default function initializeRooms() {
  const data = Array();
  data.push(new ClassRoom(19));
  data.push(new ClassRoom(20));
  data.push(new ClassRoom(34));

  return data;
}
