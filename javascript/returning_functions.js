// do not declare variables in global scope not good practice

function one() {
  return console.log('one')
}

// let value = one();
// console.log(value)
// console.log(one())

// let value = one;
// //console.log(typeof one)
// value();


function two() {
    return function () {
        console.log('two')
    }
    
}

// let myFunction = two();
// myFunction();
//(two())(); //function invocation



function three(){
    return function(){
        return 'three';
    }
}

console.log(three()());