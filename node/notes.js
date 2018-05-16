const fs = require('fs');
const os = require('os');

// console.log(os.userInfo())
fs.appendFile("notes.txt", `hello world, ${os.userInfo()['username']}!\n`);
