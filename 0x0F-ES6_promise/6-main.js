import handleProfileSignup from './6-final-user';
(async () => {
  console.log(await handleProfileSignup('Bob', 'Dylan', 'bob_dylan.jpg'));
})();
