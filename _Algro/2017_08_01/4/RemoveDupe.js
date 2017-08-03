function removeDupes(x) {

    var newArr = [];

    for(var i = 0; i<x.length; i++){

        var test = true;

        for(var j = i; j>-1; j--){

            console.log("i = " + i + " j = " + j);

            if(i != j && x[i] == x[j]){

                console.log("match!");
                test = false;

            }

        }

        if(test){

            newArr.push(x[i]);

        }

    }

    return(newArr);

}

function removeDupesInside(x) {

    for(var i = 0; i<x.length; i++){

        var test = true;

        for(var j = i; j>-1; j--){

            console.log("i = " + i + " j = " + j);

            if(i != j && x[i] == x[j]){

                console.log("match!");
                test = false;

            }

        }

        if(!test){

            x.splice(i,1);
            i--;

        }

    }

    return(x);

}

function removeDupesOneLoop(x) {

    for(var i = x.length-1; i>0; i--){

        if(x.indexOf(x[i]) != i){

            x.splice(i,1);

        }

    }

    return(x);

}

var arr = [1,2,1,3,4,2];

var arr2 = [1,2,1,6,4,6,5,5,5,2,8,8,8,8,8,8,10];

//console.log("removeDupes2 = " + removeDupes(arr2));
//console.log("removeDupesInside = " + removeDupesInside(arr));
//console.log("removeDupesInside 2 = " + removeDupesInside(arr2));
console.log("removeDupesOneLoop = " + removeDupesOneLoop(arr));
console.log("removeDupesOneLoop2 = " + removeDupesOneLoop(arr2));
