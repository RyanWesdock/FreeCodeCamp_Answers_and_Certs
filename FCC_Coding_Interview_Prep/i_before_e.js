function IBeforeExceptC(word) {
    let testRegex = /.*(cei)|(^cie)/g
    return testRegex.test(word)
}