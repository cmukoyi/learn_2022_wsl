/* var car = {
    make: 'BMW',
    model: '850i Schitzer',
    year: 2022,
    get_price: function(){
        //perform some calculation
        return 5000;
    },
    print_description: function(){
        console.log(this.make + ' ' + this.model)
    }

}
 */

/* function first() {
    return this;
}

console.log(first() === global);  */
/* 
function second() {
    'use strict';
    return this;
    
}
console.log(second() === global);
console.log(second() === undefined); */

/* let myObject = {value: 'My Object'};

// value is set on the global object
globalThis.value = 'Global object';

function third() {
    return this.value;
}
//console.log(third());

// bind to initial value

console.log(third.call(myObject)); */

function fifth() {
    console.log(this.firstName + ' '+ this.lastName)
}

let customer1 = {
    firstName:'Carlos',
    lastName:'Mukoyi',
    print:fifth


}

let customer2 = {
    firstName:'Tadiwa',
    lastName:'Mukoyi',
    print:fifth

}
customer1.print();
customer2.print();