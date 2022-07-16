let car = {
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

car.print_description();
var new_year = car.year;
console.log(car.year);
//console.log(car['year']); - not best

//attactch property to existing object
var another_car = {};
another_car.whatever = 'Carlos';
console.log(another_car.whatever);

//chain properties
var a = {
    my_property: {b: 'hi'}
};
console.log(a.my_property.b)

//object grapgh 
var c ={
    myProperty: [
        {d:'this'},
        {e: 'My example'},
        {f: 'Test'},
        {g: 'Test'}
    ]
}

