class Ninja{

    constructor(name){
        this.name = name;
        this._health = 100;
        this._speed = 3;
        this._strength = 3;
    }
     get health(){
         return this._health;
     }
     get speed(){
         return this._speed;
     }
     get strength(){
         return this._strength;
     }
     get self(){
         return this;
     }

    sayName(){
        console.log("Hi, I am " + this.name);
        return this.self;
    }

    showStats(){
        console.log("Name: " + this.name + " health: " + this._health + " strength: " + this._strength + " speed: " + this._speed);
        return this.self;
    }

    drinkSake(){
        this._strength += 10;
        return this.self;
    }
}

class Sensei extends Ninja {

    constructor(name){
        super(name);
        this._health = 200;
        this._speed = 10;
        this._strength = 10;
        this._wisdom = 10;
    }

    get wisdom(){
        return _wisdom;
    }

    speakWisdom(){
        console.log("A few moments to learn, a lifetime to master.")
    }

}

var ninja1 = new Ninja("Hyabusa");
ninja1.sayName();
// -> "My ninja name is Hyabusa!"
ninja1.showStats();
// -> "Name: Hayabusa, Health: 100, Speed: 3, Strength: 3"
ninja1.drinkSake().showStats();

let super_sensei = new Sensei("Master Splinter");
super_sensei.speakWisdom();
// -> "What one programmer can do in one month, two programmers can do in two months."
super_sensei.showStats();
