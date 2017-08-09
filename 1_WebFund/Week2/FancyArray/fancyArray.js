var arr = [ "James", "Jill", "Jane", "Jack" ];

function printFancyArray(array, symbol, reversed){

    if(!reversed){

        console.log("reversed");

        for(var i = array.length-1; i >= 0; i--){

            console.log(i + " " + symbol + " " + array[i]);

        }

    } else {

        console.log("regular");

        for(var i = 0; i < array.length; i++){

            console.log(i + " " + symbol + " " + array[i]);

        }

    }

}

printFancyArray(arr, "=", false);

printFancyArray(arr, ">>>", true);
