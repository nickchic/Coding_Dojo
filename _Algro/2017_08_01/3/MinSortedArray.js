function findMinInSortedRotated(x) {

    for(var i = 0; i<x.length; i++){

        if(x[i] > x[i+1]){

            return x[i+1];

        }

    }

}

var testArr = ["Gigli","Jay is cool","Mavis","Phoebe","Thurber","Anna","Celeste","Elon"];
console.log(findMinInSortedRotated(testArr));
