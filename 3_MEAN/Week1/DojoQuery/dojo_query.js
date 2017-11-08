function $Dojo(id){

    let obj = document.getElementById(id);

    obj.hover = function(func){
        obj.addEventListener('mouseover', func);
    }

    obj.click = function(func){
        obj.addEventListener('click', func);
    }

    return obj;
};

$( document ).ready(function() {
    $Dojo('button_one').hover(function(){console.log("one")});
    $Dojo('button_two').click(function(){console.log("two")});
});
