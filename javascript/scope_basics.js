let a = 'first';

function scopeTest() 
{
    console.log(a);
    a = 'changed'

    // let b = 'second';
    console.log(a);
       
}
scopeTest();

