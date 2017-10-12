function filter_range(arr, min, max){
    tempArr = []
    for(i=0;i<arr.length;i++){
        if(arr[i] > min && arr[i] < max){
            console.log("later")
        } else {
            tempArr[tempArr.length] = arr[i]
        }
    }
    return tempArr
}

console.log(filter_range([1,2,3,4,5,6,7],3,6))
