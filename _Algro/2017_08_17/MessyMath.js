// 1. messyMath
// Create a function messyMath(num) that will return the following sum: add all integers from 0
// up to the given num, except for the following special cases of our count value:
// 	1.	If current count (not num) is evenly divisible by 3, don’t add to sum; skip to the next count;
// 	2.	Otherwise, if current count is evenly divisible by 7, include it twice in sum
// instead of once;
// 	1.	Regardless of the above, if current count is exactly 1/3 of num, return -1
// immediately.
// For example, if given num is 4, return 7. If given num is 8, return 34. If given num is 15,
// return -1.


console.log(messyMath(4));
console.log(messyMath(8));
console.log(messyMath(15));

function messyMath(num){

    var x = 0;

    for(var i = 1; i <= num; i++){

        if(i == (num/3)){
            return -1;
        }

        if(i % 3 == 0){
            continue;
        }

        if(i % 7 == 0) {
            x += (i*2);
        } else {
            x += i;
        }


    }

    return x;

}
