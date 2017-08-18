// 4. String.split
// String.split(separator,limit) - split string into an array of substrings, returning array.
// Separator specifies where to divide substrings and is not included in any substring. If "" is
// specified, split the string on every character. Limit is optional and indicates number of
// splits; additional post-limit items should be discarded. Note: existing string is unaffected.

// String.prototype.split = function (seperator, limit) {
//
//     var arr = [];
//
//     arr[0] = this.slice(0,seperator);
//     arr[1] = this.slice(seperator,limit);
//
//     return arr;
//
// };

String.prototype.split = function (seperator, limit) {

    var arr = ["",""];

    for(var i=0; i < seperator; i++){
        arr[0] += this[i];
    }

    if(limit != undefined){
        for(var i=seperator; i < limit; i++){
            arr[1] += this[i];
        }
    } else {
        for(var i=seperator; i < this.length; i++){
            arr[1] += this[i];
        }
    }



    return arr;

};

var str = "nick chic is the best";

console.log(str.split(10));
console.log(str.split(5,9));
