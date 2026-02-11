function canMakeWord(word) {
    word = word.toUpperCase();
    const blockArr =[["B", "O"], ["X", "K"], ["D", "Q"], ["C", "P"], ["N", "A"], 
               ["G", "T"], ["R", "E"], ["T", "G"], ["Q", "D"], ["F", "S"], ["J", "W"],
                ["H", "U"], ["V", "I"], ["A", "N"], ["O", "B"], ["E", "R"], ["S", "F"],
                ["L", "Y"], ["P", "C"], ["Z", "M"]];
    const newArr =[];
    for (let i = 0; i < word.length; i++){
        for (let arr of blockArr) {
             if (arr.includes(word.slice(i, i+1)) && !(newArr.includes(arr))) {
                newArr.push(arr);
                // break ensures loop stops once it adds a new value to the array
                break
             } 
        }
    // since each block represents a letter, the array of blocks needs to be the same length;
    // too short and it required duplicates that could not be provided (it can't be longer).
    } return newArr.length == word.length ? true : false
}

console.log(canMakeWord("snootz"));
