function slot(quarters, happy){

while(quarters > 0){

    quarters -= bet;

    if(Math.floor((Math.random() * 100)) == 1){

        //win!
        quarters += (Math.floor((Math.random() * 50) + 50));
        console.log("You won!!, Quarters = " + quarters);
        if(happy)

    } else {

        console.log("You lost, Quarters = " + quarters);

    }


}

}

slot(25,3);
