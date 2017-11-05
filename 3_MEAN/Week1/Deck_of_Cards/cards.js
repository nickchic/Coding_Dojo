class Deck{
    constructor(){
        this._cards = [];
        this.reset();
        this.self = this;
    }

    shuffle(){
        this.reset()
        var copy = [], n = 52, i;

        // While there remain elements to shuffle…
        while (n) {

          // Pick a remaining element…
          i = Math.floor(Math.random() * n--);

          // And move it to the new array.
          copy.push(this._cards.splice(i, 1)[0]);
        }

        this._cards = copy;
        return this.self;
    }

    reset(){
        this._cards = []
        for(var i = 0; i < 52; i++){
            this._cards[i] = i+1;
        }
        return this.self
    }

    deal(player){
        let card = this.cards[this.cards.length-1];
        this.cards.pop();
        player.add_to_hand(card);
        return card;
    }

    get cards(){
        return this._cards;
    }
    set cards(cards){
        this._cards = cards;
    }

}

class Player{
    constructor(name){
        this._name = name;
        this._hand = []
    }

    get hand(){
        return this._hand;
    }

    add_to_hand(card){
        this._hand.push(card);
    }

    discard(x){
        if(x <= this._hand.length){
            this._hand.splice(x-1, 1)
        } else {
            console.log("Out of range")
        }
    }

}

var x = new Deck;
var nick = new Player('Nick')

console.log("Shuffled Cards " + x.shuffle().cards);
console.log("1st Card Dealt " + x.deal(nick));
console.log("2nd Card Dealt " + x.deal(nick));
console.log("Cards Left " + x.cards);
console.log("Nick's Hand " + nick.hand);
