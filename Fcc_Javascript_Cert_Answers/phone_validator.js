function telephoneCheck(str) {
    let testRegex = /^1?[\s?|\-?]\d{10}$/
    let testRegexPara = /^1?\s?(\(\d{3}\)\s?|\-?\d{3}\-|\d{3}\s?)\d{3}(\s?|-?)\d{4}$/
    if(testRegex.test(str) || testRegexPara.test(str)) {
        return true;
    }
    return false;
  }
  
console.log(telephoneCheck("5555555555"));
