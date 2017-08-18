// 2. Skyline Heights
// Lovely Burbank has a breathtaking view of the Los Angeles skyline. Let’s say you are given
// an array with heights of consecutive buildings, starting closest to you and extending away.Array [-1,7,3] would represent three buildings: first is actually out of view below street level,
// behind it is second at 7 stories high, third is 3 stories high (hidden behind the 7-story). You
// are situated at street level. Return array containing heights of buildings you can see, in order. Given [-1,1,1,7,3] return [1,7]. Given [0,4] return [4]. As always with challenges, do
// not use built-in array functions such as unshift().

function skyline(arr){

    var returnArr = [];
    var biggest = 0;

    if(arr[0] > 0){
        returnArr.push(arr[0]);
    }

    for(var i = 1; i < arr.length; i++){
        if(arr[i] < 0){
            continue;
        }
        if(arr[i] > biggest){
            biggest = arr[i];
            returnArr.push(arr[i]);
        }
    }

    return returnArr;

}

var x = [-1,1,1,7,3];
var y = [0,4];
var z = [0,4,1,7,5,5,7,7,8,1,1,1];

console.log(skyline(x));
console.log(skyline(y));
console.log(skyline(z));
