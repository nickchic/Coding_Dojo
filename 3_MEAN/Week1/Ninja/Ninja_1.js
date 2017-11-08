function Ninja(name){
    this.name = name;
    var health = 100;
    var speed = 3;
    var strength = 3;
    var self = this;

    this.sayName = function(){
        console.log("Hi, I am " + this.name);
        return self;
    }

    this.showStats = function(){
        console.log("Name: " + this.name + " health: " + health + " strength: " + strength + " speed: " + speed);
        return self;
    }

    this.drinkSake = function(){
        strength += 10;
        return self;
    }
}

var ninja1 = new Ninja("Hyabusa");
ninja1.sayName();
// -> "My ninja name is Hyabusa!"
ninja1.showStats();
// -> "Name: Hayabusa, Health: 100, Speed: 3, Strength: 3"
ninja1.drinkSake().showStats();
