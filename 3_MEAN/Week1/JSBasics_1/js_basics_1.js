window.onload = function() {

    //1
    var x = [];
    console.log(x);
    x.push('coding');
    x.push('dojo');
    x.push('rocks');
    x.pop();
    console.log(x);
    document.getElementById("1").innerHTML = x;

    //2
    const y = [];
    console.log(y);
    y.push(88);
    document.getElementById("2").innerHTML = "Y already had 88 in it even though I logged it before I pushed it y = " + y;

    //3
    var z = [9, 10, 6, 5, -1, 20, 13, 2];

    for(var i = 0; i < z.length; i++){
        console.log(z[i]);
    }
    for(var i = 0; i < z.length-1; i++){
        console.log(z[i]);
    }
    document.getElementById("3").innerHTML = "for(var i = 0; i < z.length-1; i++){<br/>console.log(z[i]);<br/>}"

    //4
    var names = ['Kadie', 'Joe', 'Fritz', 'Pierre', 'Alphonso']
    for(var i = 0; i < names.length; i++){
        console.log(names[i]);
    }
    for(var i = 0; i < names.length; i++){
        if(names[i].length == 5){
            console.log(names[i]);
        }
    }
    document.getElementById("4").innerHTML = "for(var i = 0; i < names.length; i++){<br/>if(names[i].length == 5){<br/>console.log(names[i]);<br/>}<br/>}"

    //5
    function yell(string){
        console.log(string.toUpperCase())
    }
    yell('hello')
    document.getElementById("5").innerHTML = "you can look at W3 Schools ;)"
}
