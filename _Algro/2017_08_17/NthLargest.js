// 3.Array: Nth-largest
// Liam has "N" number of Green Belt stickers for excellent Python projects. Given arr and N,
// return the Nth-largest element, where (N-1) elements are larger. Return null if needed.

function nthLargest(arr, n){

    arr.sort(function(a, b){return b-a});

    return arr[n-1];

}

var x = [3,6,46,32,67,1,34]
console.log(nthLargest(x, 4));
