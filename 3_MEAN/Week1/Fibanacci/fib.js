function fib() {
  let num_1 = 0;
  let num_2 = 1;
  let total = 0;
  function nacci() {
      total = num_1 + num_2;
      num_2 = num_1;
      num_1 = total;
      console.log(total);
  }
  return nacci
}
var fibCounter = fib();
fibCounter() // should console.log "1"
fibCounter() // should console.log "1"
fibCounter() // should console.log "2"
fibCounter() // should console.log "3"
fibCounter() // should console.log "5"
fibCounter() // should console.log "8"
