// function that returns the smallest positive integer whose square ends in the digits 269,696.

function babbage(babbageNum, endDigits) {
    let check = true
    let x = Math.ceil(Math.sqrt(endDigits))
    let regexTest = /^\d*269696$/
    while (check) {
        if (regexTest.test((x ** 2).toString())) {
            check = false
        } else {
            x++
        }
    }
    return x;
  }

console.log(babbage(99736, 269696))
