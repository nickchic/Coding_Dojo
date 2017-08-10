function slot(quarters, happy){

    while(quarters > 0){

        quarters -= 1;

        var roll = Math.floor((Math.random() * 100));

        console.log("roll = " + roll);

        if(roll == 1){

            var winnings = Math.floor((Math.random() * 50) + 50)
            quarters += winnings;
            console.log("You won " + winnings + "!!, Total quarters = " + quarters);

        } else {

            console.log("You lost, Quarters = " + quarters);

        }

        if(quarters >= happy){
            console.log("I am leaving with " + quarters + " in my pocket! Gambling can be addicting");
            break;
        }


    }

}

slot(25,100);
