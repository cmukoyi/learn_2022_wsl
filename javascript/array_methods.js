
let names = ['david','eddie','alex','john','mike'];
let others = ['tupac','amaru','shakur','carlos','mukoyi'];

let lost = [4,6,8,19,17,56,89,90]
let tupac = [1,1,2,2,3,5,13,21,34,55]

var combine = lost.concat(tupac);
//console.log(combine);



//console.log(tupac.join('~'));

//push pop - add elements or remove

/* console.log(lost.shift());
console.log(lost); */

// lost.unshift(11,23,45);
// console.log(lost);

// console.log(names);
// console.log(names.reverse());
// console.log(names.sort());

/* console.log(others.indexOf('amaru'))


console.log(combine);
console.log(combine.lastIndexOf(1)); */


/* var filtered = combine.filter((x) => {if (x <= 15) return x; });
console.log(filtered); */

//itenary
//names.forEach((names) => console.log(`howdy ${names}` ));


/* console.log(filtered.every((num) => num < 10));
console.log(filtered.every((num) => num < 16)); */

console.log(tupac.some((num) => num > 150 ));