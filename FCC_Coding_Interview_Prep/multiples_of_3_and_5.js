// sum of multiples of 3 and 5.
// Javascrip doesn't seem to have a range() function like Python does
// but this can be replaced with an incrementing for loop.
function multiplesOf3and5(number) {
    let sum = 0;
    for(let i = 0; i < number; i++) {
      if (i % 3 == 0 || i % 5 == 0) {
        sum += i;
      }
    }
    return sum;
}
    
