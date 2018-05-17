const fs = require('fs');
const os = require('os');
const _ = require("lodash");

function wh() {
  console.log(`Running ${arguments.callee.name} function`)
  user = os.userInfo();
  fs.appendFile("notes.txt", `hello world, ${user['username']}!\n`);
  return "Done";
}

module.exports.writehello = wh;
module.exports.adder = (a, b) => {
  console.log(`Running ${arguments.callee.name} function`)
  return a + b;
}
module.exports.testLDSH = function testLDSH() {
  console.log(`Running ${arguments.callee.name} function`)
  console.log(_.isString(true))
  console.log(_.isString("Foobar"))
  var fArray = _.uniq(['FOo',1,2,'Foo',1,2,34,5])
  console.log(`Uniquified array: '${fArray}'.`)
}