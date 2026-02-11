// Write a function which takes a ROT13 encoded string as input and returns a decoded string.
function rot13(str) {
  let alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ".split("");
  let punctArray = [" ", ",", "!", "?", "."]
  let decodedStr = "";
  var decodedIndex = 0;
  for(let index in str) {
    if (punctArray.includes(str[index])) {
      decodedStr += str[index];
    }
    if ((alphabet.indexOf(str[index])) <= 12 && (alphabet.indexOf(str[index])) >= 0) {
      decodedIndex = (alphabet.indexOf(str[index])) + 13;
      decodedStr += alphabet[decodedIndex];
    } else if ((alphabet.indexOf(str[index])) >= 13 && (alphabet.indexOf(str[index])) <= 25) {
      decodedIndex = (alphabet.indexOf(str[index])) - 13;
      decodedStr += alphabet[decodedIndex];
    } 
  } 
    return decodedStr;
  }
  
console.log(rot13("SERR PBQR PNZC!"));
