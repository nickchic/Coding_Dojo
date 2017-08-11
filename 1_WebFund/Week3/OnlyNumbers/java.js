function onlyNumbers(array){

    var newArray = [];

    for(var i = 0; i < array.length; i++){

            if(typeof array[i] === "number"){

                newArray.push(array[i]);

            }

    }

    return newArray;

}

function onlyNumbersNoReturn(array){

    for(var i = 0; i < array.length; i++){

            if(typeof array[i] !== "number"){

                array.splice(i,1);

            }

    }

}


var test = [2, "Jawn", 4, true, 12, "nick"];

console.log(onlyNumbers(test));

onlyNumbersNoReturn(test);

console.log(test);
