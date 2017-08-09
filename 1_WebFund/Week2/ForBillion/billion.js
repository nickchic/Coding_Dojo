var reward = 0;
var dailyAmount = 0.01;

for(var i = 0; i<30; i++){

    reward += dailyAmount;
    dailyAmount *= 2;

}

console.log("after 30 days the reward = $" + reward);

var reward2 = 0;
var dailyAmount2 = 0.01;
var j = 0;

while(true){

    reward2 += dailyAmount2;

    if(reward2 > 10000){
        console.log("it took " + j + " days to get to 10,000, reward = " + reward2);
        break;
    }

    j++;
    dailyAmount2 *= 2;

    if(j == 1000){
        //in case of an infinite loop
        console.log("took more than 1000");
        break;
    }

}

var reward3 = 0;
var dailyAmount3 = 0.01;
var k = 0;

while(true){

    reward3 += dailyAmount3;

    if(reward3 > 1000000000){
        console.log("it took " + k + " days to get to a billion, reward = $" + reward3);
        break;
    }

    k++;
    dailyAmount3 *= 2;

    if(k == 1000){
        //in case of an infinite loop
        console.log("took more than 1000");
        break;
    }

}

var reward4 = 0;
var dailyAmount4 = 0.01;
var l = 0;

while(true){

    reward4 += dailyAmount4;

    if(reward4 == Infinity){
        console.log("it took " + l + " days to get to infinity");
        break;
    }

    l++;
    dailyAmount4 *= 2;

    if(l == 10000){
        //in case of an infinite loop
        console.log("took more than 10000");
        break;
    }

}
