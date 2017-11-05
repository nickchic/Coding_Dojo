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
        console.log("Name: " + this.name + ", health: " + health + ", strength: " + strength + ", speed: " + speed);
        return self;
    }

    this.drinkSake = function(){
        strength += 10;
        return self;
    }

    this.punch = function(otherNinja){
        if(otherNinja.isNinja){
            otherNinja.hit(5);
            console.log(this.name + " punched " + otherNinja.name + " and lost 5 health")
            return self;
        }
        console.log("You just punched something thats not a Ninja, weirdo")
        return null;
    }

    this.kick = function(otherNinja){
        if(otherNinja.isNinja){
            otherNinja.hit(15);
            console.log(this.name + " kicked " + otherNinja.name + " and lost 15 health")
            return self;
        }
        console.log("You just kicked something thats not a Ninja, weirdo")
        return null;
    }

    this.hit = function(num){
        health -= num;
        return self;
    }

}

Ninja.prototype.isNinja = true;

var blue_ninja = new Ninja("Goemon");
var red_ninja = new Ninja("Bill Gates");
red_ninja.punch(blue_ninja);
blue_ninja.showStats()
