function makeChange(x) {

    var quarters = 0;
    var dimes = 0;
    var nickels = 0;
    var pennies = 0;

    if(x >= 25){

        quarters = Math.floor(x/25);
        x -= (quarters * 25);
    }

    if(x >= 10){

        dimes = Math.floor(x/10);
        x -= (dimes * 10);

    }
    if(x >= 5){

        nickels = Math.floor(x/5);
        x -= (nickels * 5);

    }
    if(x >= 1){

        pennies = x;

    }

    console.log("quarters = " + quarters);
    console.log("dimes = " + dimes);
    console.log("nickels = " + nickels);
    console.log("pennies = " + pennies);

}

makeChange(94);
makeChange(22);
makeChange(167);
makeChange(3);
