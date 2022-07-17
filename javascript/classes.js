// declaration

class Car{
    constructor(make,model,year){
        this.make = make,
        this.model = model,
        this.year = year
    }

    print(){
        console.log(`${this.make} ${this.model} (${this.year})`);

    }
}

let myCar = new Car('bmw','850i',2020);
console.log(myCar);
myCar.print();

class SportsCar extends Car{
    revEngine(){
        console.log('Vrooom ' + 'goes the '+ this.make);
    }
    
}

let mySportsCar = new SportsCar('Dodge','Viper',2022);
mySportsCar.print();
mySportsCar.revEngine();

// expression

/* let car = class {

} */

