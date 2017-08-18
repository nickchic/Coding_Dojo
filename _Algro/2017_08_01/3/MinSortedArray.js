function nicksWay(x) {

    for(var i = 0; i<x.length; i++){

        if(x[i] > x[i+1]){

            return x[i+1];

        }

    }

}

var testArr = ["Gigli","Jay is cool","Mavis","Phoebe","Thurber","Anna","Celeste","Elon"];
console.log(nicksWay(testArr));


function minhsWay(arr){
	var start = 0;
	var end = arr.length;
	var mid = Math.floor((start + end ) / 2) // 4
	while (end - start != 1){
		console.log(mid)
		if(arr[mid] > arr[start]){
			start = mid// 5
		}else if(arr[mid - 1] > arr[mid]){
			break
		}else{
			end = mid
		}
		mid = Math.floor((start + end ) / 2)
	}
	console.log(mid)
}
