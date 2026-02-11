function checkCashRegister(price, cash, cid) {
  // Calculate Change Amount
  let change;
  change = cash - price;
  // Output Object
  let registerStatus = {status: "", change: []};

  // Calculate Value in Register
  // Step 1: flatten cid Array
  let flatCid = cid.flat();
  // Step 2: filter out numbers
  let numCid = flatCid.filter((value) => typeof(value) == "number" );
  // Step 3: Sum numbers
  let sumCid = numCid.reduce(
    (accumulator, currentValue) => accumulator + currentValue
  );
  // Step 4: Adjust for the wonky way Javascript does math
  sumCid = (Number((sumCid).toFixed(2)));

  // Turn the change due into appropriate denominations
  let denominationValues = [["PENNY", .01], ["NICKEL", .05], ["DIME", .10], ["QUARTER", .25], ["ONE", 1], ["FIVE", 5], ["TEN", 10], ["TWENTY", 20], ["ONE HUNDRED", 100]];
  denominationValues = denominationValues.reverse();    // reverse to go from high to low
  let outputArray = [];
  let change2 = 0;
  change2 += change;
  let reverseCid = [...cid].reverse()  // setting new variables to stop mutation
  let totalAmount = 0;            // We need to keep track of the total amount in the output Array to ensure we have exact change.
  for (let i = 0; i < denominationValues.length; i++) {  // using a for loop to get values of both arrays to compare
    let [cidDenomination, cidAmount] = reverseCid[i];
    let [denomination, amount] = denominationValues[i];  // breaking out values from those arrays
    let j = 0;
    while (change2 - amount >=0 && amount * j < cidAmount) {   // first condition continues subtraction, second condition ensures change actually exists.
    change2 = Number((change2 - amount).toFixed(2));
    totalAmount += amount;
    j++;
    } if (!(j == 0)) {
      outputArray.push([denomination,amount * j]);
    }
  }
  // Compare Value in Register with change.
if (sumCid < change || totalAmount < change) {
  registerStatus.status = "INSUFFICIENT_FUNDS";
  return registerStatus;
} else if (sumCid == change) {
  registerStatus.status = "CLOSED";
  registerStatus.change = cid;
  return registerStatus;
} else {
  registerStatus.status = "OPEN";
  registerStatus.change = outputArray;
  return registerStatus;
}

}

console.log(checkCashRegister(19.5, 20, [["PENNY", 0.5], ["NICKEL", 0], ["DIME", 0], ["QUARTER", 0], ["ONE", 0], ["FIVE", 0], ["TEN", 0], ["TWENTY", 0], ["ONE HUNDRED", 0]]));

