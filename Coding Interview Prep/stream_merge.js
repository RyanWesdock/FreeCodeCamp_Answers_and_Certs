// Approach One

function mergeLists(lists) {
    let flatList = [...lists];
    let flatterList = [];
    for (let i = 0; i < flatList.length; i++) {
        for (let j = 0; j < flatList[i].length; j++) {
            flatterList.push(flatList[i][j])
        }
    }
    flatterList.sort((a, b) => (a - b))
    return flatterList
}

console.log(mergeLists([[1, 3, 5, 9, 10], [2, 4, 6, 7, 8]]))

// Approach Two

function mergeLists2(lists) {
    let flatList = [...lists].flat()
    flatList.sort((a,b) => (a - b))
    return flatList
}

console.log(mergeLists2([[1, 3, 5, 9, 10], [2, 4, 6, 7, 8]]))