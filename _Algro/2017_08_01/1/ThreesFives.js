threesFives();
betterThreesFives(100,4000000);

function threesFives() {

    var sum = 0;

    for(var i = 100; i <= 4000000; i++){

        if(i%5 == 0 && i%3 == 0){

        } else if(i%5 == 0 || i%3 == 0){

            sum += i;

        }

    }

    console.log("sum = " + sum);

}

function betterThreesFives(x,y) {

    var sum = 0;

    for(var i = x; i <= y; i++){

        if(i%5 == 0 && i%3 == 0){

        } else if(i%5 == 0 || i%3 == 0){

            sum += i;

        }

    }

    console.log("sum = " + sum);

}
