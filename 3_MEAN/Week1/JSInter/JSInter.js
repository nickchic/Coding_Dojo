function starString(x, y=null){
    var letter = '*'
    if(y != null){
        letter = y;
    }
    var str = '';
    for(var i = 0; i < x; i++){
        str += letter
    }
    return str;
}

function drawStars(arr){
    for(var i = 0; i < arr.length; i++){
        if(arr[i].constructor === String){
            console.log(starString(arr[i].length,arr[i].charAt(0)))
        } else {
            console.log(starString(arr[i]))
        }

    }
}

drawStars([2,4,7,'nick'])
