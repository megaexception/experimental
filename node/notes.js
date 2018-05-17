const fs = require('fs');
const os = require('os');
const readline = require('readline');
const _ = require("lodash");

function wh() {
    console.log(`Running ${arguments.callee.name} function`);
    let user = os.userInfo();
    fs.appendFile("notes.txt", `hello world, ${user['username']}!\n`);
    return "Done";
}

module.exports.writehello = wh;
module.exports.adder = (a, b) => {
    console.log(`Running ${arguments.callee.name} function`);
    return a + b;
};
module.exports.testLDSH = function testLDSH() {
    console.log(`Running ${arguments.callee.name} function`);
    console.log(_.isString(true));
    console.log(_.isString("Foobar"));
    let fArray = _.uniq(['FOo', 1, 2, 'Foo', 1, 2, 34, 5]);
    console.log(`Uniquified array: '${fArray}'.`)
};
module.exports.log = msg => console.log(`LOG:${new Date()}> ${msg}`);
module.exports.timeout = (arg) => console.log(`Timeout for ${arg}`);
module.exports.enumlines = (list_lines) => {
    for (let i = 0; i < list_lines.length; i++) {
        console.log(`${i}. ${list_lines[i]}`)
    }
};
module.exports.readfile = fname => {
    let list_lines = [];
    let input = fs.createReadStream(fname);
    input.on('end', () => {
        // console.log(list_lines);
        module.exports.enumlines(list_lines);
    });
    const reader = readline.createInterface({input: input});
    reader.on('line', line => list_lines.push(line));
};