
// let a = 7 * undefined / "panama";
// console.log(a);

/* function beforTryCatch() {
    let obj = undefined ;
    console.log(obj.b);
    console.log('If there is an exception you\'ll nerver see this.')

    
} */

//beforTryCatch();

/* function afterTryCatch() {
    try {
        let obj = undefined ;
        console.log(obj.b);
        console.log('If there is an exception you\'ll nerver see this.')
    } catch (error) {
        console.log('I caught an exception that was thrown: ' + error.message);

    }finally{
        console.log('This will happen no matter what');
    }

    console.log('My app is running');
    
}
afterTryCatch(); */


function performCalculation(){
       if (!Object.hasOwnProperty('b')) {
        throw new Error('Object missing property');
       }
       // continue with calculation
       return 6;

}


function performOperation() {
    let obj = {};
    let value = 0;
    try {
        value = performCalculation(obj)
    } catch (error) {
        console.log(error.message);
        
    }

    if (value == 0){
        //retry logic
    }
    
}

performOperation();
