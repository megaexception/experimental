const fs = require('fs');
const os = require('os');

function wh() {
    user = os.userInfo();
    fs.appendFile("notes.txt", `hello world, ${user['username']}!\n`);
    return "Done";
}

module.exports.writehello = wh;
module.exports.adder = (a,b) => {
  return a+b;
}
