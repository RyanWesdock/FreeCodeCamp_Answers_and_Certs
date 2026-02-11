function fiboEvenSum(n) {
    const fibArray = [0, 1];
    for (let i = 1; fibArray[i] < n; i++) {
        fibArray.push(fibArray[i] + fibArray[i - 1])
    }
    let filteredArr = fibArray.filter( (element) => (element <= n) && (element % 2 == 0));
    let fibSum = filteredArr.reduce((acc, val) => acc + val)
    return fibSum
  }

// I was not able to solve this initially, but having completed the equivalent challenge in the javascript course for odd numbers,
// this was no more difficult. I did, however, improve on that version by using .filter() and .reduce() to greatly simplify and
// clarify the code.
