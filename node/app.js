const notes = require("./notes.js");

// console.log(notes.writehello());
// console.log(notes.adder(81, 90));
// console.log(notes.testLDSH());
notes.log("this is a test");

function test_var_let_visibility() {
    console.log(i);
    // var i = 0;
    for (var i = 0; i < 10; i++) {
        console.log("." + i);
    }
    console.log(i);
}

function test_arrow_functions() {
    let myFunction = () => ({age: 23});
    // var myFunction = () => { age: 23 };
    console.log(myFunction());
}

function test_timer() {
    setTimeout(notes.timeout, 5000, "default");
    console.log("Started timeout");
}

function test_notes_file() {
    notes.readfile("notes.txt");
}

function test_notes_log() {
    for (let item in [1, 2, 3, 4, 7, 5, 4, 3, 2, 1]) {
        notes.log(item);
    }
}

function test_recursion(x) {
    if (x > 0) {
        return x * test_recursion(x - 1);
    } else {
        return 1;
    }
}

var test_rec = function (x) {
    const test_recursion = arguments.callee;
    if (x > 0) {
        return x * test_recursion(x - 1);
    } else {
        return 2;
    }
};

var test_this = function (x) {
    console.log(this.name);
}();
// console.log(`Recursion of 10: ${test_recursion(10)}.`)
// console.log(`Double recursion of 10: ${test_rec(10)}.`)
