const notes = require('./notes.js');

console.log(notes.writehello());
console.log(notes.adder(81, 90));
console.log(notes.testLDSH());
notes.log("this is a test");

var myFunction = () => ({age: 23});
var myFunction = () => {
    age: 23
};
console.log(myFunction());

setTimeout(notes.timeout, 5000, "default");
console.log("Started timeout");
