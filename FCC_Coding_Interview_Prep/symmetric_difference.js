function symmetricFunction(arr1, arr2) {
    const outputArray = [];
    for (let value of arr1) {
        if (!arr2.includes(value) && !outputArray.includes(value)) {
            outputArray.push(value);
        }
    }
    for (let value of arr2) {
        if (!arr1.includes(value) && !outputArray.includes(value)) {
            outputArray.push(value);
        }
    } return outputArray;
}

function sym(...args) {
    const complexArray = [...args];
    let outputArray = complexArray.reduce(symmetricFunction);
    outputArray.sort();
    return outputArray
}

