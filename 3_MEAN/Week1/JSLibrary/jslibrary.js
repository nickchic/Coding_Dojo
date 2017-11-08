var _ = {
   map: function(array, iteratee) {
     for(let i = 0; i < array.length; i++){
         array[i] = iteratee(array[i]);
     };
     return array;
   },
   reduce: function(array, iteratee, memo) {
       for(let i = 0; i < array.length; i++){
           memo = iteratee(memo, array[i]);
       };
       return memo;
   },
   find: function(array, predicate) {
       for(let i = 0; i < array.length; i++){
           if(predicate(array[i])){
               return array[i];
           }
       };
   },
   filter: function(array, predicate) {
       let newArray = [];
       for(let i = 0; i < array.length; i++){
           if(predicate(array[i])){
               newArray.push(array[i]);
           }
       };
       return newArray;
   },
   reject: function(array, predicate) {
       let newArray = [];
       for(let i = 0; i < array.length; i++){
           if(!predicate(array[i])){
               newArray.push(array[i]);
           }
       };
       return newArray;
   }
 }
// you just created a library with 5 methods!

console.log(_.map([1, 2, 3], function(num){ return num * 3; }));
console.log(_.reduce([1, 2, 3, 4, 5], function(memo, num){ return memo + num; }, 0));
console.log(_.find([1, 2, 3, 4, 5, 6], function(num){ return num % 2 == 0; }));
console.log(_.filter([1, 2, 3, 4, 5, 6], function(num){ return num % 2 == 0; }));
console.log(_.reject([1, 2, 3, 4, 5, 6], function(num){ return num % 2 == 0; }));
