function zero_negativity(arr){
    for(var i = 0; i < arr.length; i++){
        if(arr[i] < 0){
            return false;
        }
    }
    return true;
}

function is_even(num){
    if(num % 2 == 0){
        return true;
    } else {
        return false;
    }
}

function how_many_even(arr){
    var x = 0;
    for(var i = 0; i < arr.length; i++){
        if(is_even(arr[i])){
            x++;
        }
    }
    return x;
}

function create_dummy_array(num){
    var x = []
    for(var i = 0; i < num; i++){
        x.push(Math.ceil(Math.random()*9))
    }
    return x;
}

function random_choice(arr){
    return arr[Math.floor(Math.random()*arr.length)]
}
