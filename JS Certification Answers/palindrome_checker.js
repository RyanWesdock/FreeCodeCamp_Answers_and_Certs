function palindrome(str) {
    str = str.replace('_', "")
    let testRegex = /[a-zA-z0-9]/ 
    var newString = "";
    for (let i = 0; i < str.length; i++) {
        if(testRegex.test(str[i])) {  
            newString += str[i];
        }
    }
    newString = newString.toLowerCase();
    for (let i = 0; i < newString.length; i++) {
        if (newString[i] == newString[(newString.length - 1) - i] ) {
        } else {
            return false;
        }
    } 
    return true;
}

function palindromeArray(str) {
    str = str.replace('_', "")
    let testRegex = /[a-zA-z0-9]/ 
    var newString = "";
    for (let i = 0; i < str.length; i++) {
        if(testRegex.test(str[i])) {  
            newString += str[i];
        }
    }
    newString = newString.toLowerCase()
    const arr1 = newString.split("")
    let arr2 = arr1.reverse()
    let reversedString = arr2.join("")
    if (newString == reversedString) {
        return true
    } else {
        return false
    }
}

console.log(palindrome("A man, a plan, a canal. Panama"))
console.log(palindromeArray("A man, a plan, a canal. Panama"))
