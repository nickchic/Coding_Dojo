var hour = 8;
var minute = 47;
var period = "PM";

var distanceToHour;
var displayHour = hour;
var timeOfDay;

if(minute == 30){

    distanceToHour = " half past ";

} else if (minute == 15) {

    distanceToHour = " quarter after ";

} else if (minute == 45) {

    distanceToHour = " quarter of ";
    displayHour++;

} else if (minute == 5) {

    distanceToHour = " five after ";

} else if (minute == 55) {

    distanceToHour = " five of ";
    displayHour++;

} else if (minute == 10) {

    distanceToHour = " ten after ";

} else if (minute == 50) {

    distanceToHour = " ten of ";
    displayHour++;

} else if (minute > 30) {

    distanceToHour = " before ";
    displayHour++;

} else if (minute < 30) {

    distanceToHour = " after ";

}

if(period == "AM"){

    timeOfDay = " in the morning.";

} else if(period == "PM"){

    if(hour >= 1 && hour < 5){
        timeOfDay = " in the afternoon.";
    } else if(hour >= 5 && hour < 8){
        timeOfDay = " in the evening.";
    } else if(hour >= 8 && hour < 12){
        timeOfDay = " at night.";
    }

} else {

    timeOfDay = ".";

}

console.log("It's" + distanceToHour + displayHour + timeOfDay);
