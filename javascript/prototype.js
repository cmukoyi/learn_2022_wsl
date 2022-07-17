
let originalCar = {
    make:'bmw',
    model:'780i',
    year:2020

};

let newCar = Object.create(originalCar);

console.log(newCar.make);
newCar.make = 'Audi';

console.log(newCar.whatever);

console.log(Object.getPrototypeOf(newCar));

let myPrototype = Object.getPrototypeOf(newCar);
console.log(myPrototype.make);

originalCar.doors = 4;
console.log(newCar.doors);


console.log(originalCar.hasOwnProperty('doors'))
console.log(newCar.hasOwnProperty('make'))
console.log(newCar.make);