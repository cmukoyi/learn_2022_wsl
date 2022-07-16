function sayHello(name) {
    return function(){
        console.log('Howdy ' + name); 
                    
    }
    
}

let Carl = sayHello('Carlos');
let Tadi = sayHello('Tadiwa');
Carl();
Tadi();

