function checkCashRegister(price, cash, cid) {
  const currencyUnits = {
    "PENNY": 0.01,
    "NICKEL": 0.05,
    "DIME": 0.1,
    "QUARTER": 0.25,
    "ONE": 1,
    "FIVE": 5,
    "TEN": 10,
    "TWENTY": 20,
    "ONE HUNDRED": 100
  };

  let totalCID = 0;
  for (let [unit, amount] of cid) {
    totalCID += amount;
  }
  totalCID = Math.round(totalCID * 100) / 100;

  let changeDue = cash - price;
  let change = [];

  if (changeDue > totalCID) {
    return { status: "INSUFFICIENT_FUNDS", change: [] };
  } else if (changeDue === totalCID) {
    return { status: "CLOSED", change: cid };
  } else {
    cid = cid.reverse();
    for (let [unit, amount] of cid) {
      const unitValue = currencyUnits[unit];
      let unitAmount = 0;
      while (changeDue >= unitValue && amount > 0) {
        changeDue -= unitValue;
        amount -= unitValue;
        unitAmount += unitValue;
        changeDue = Math.round(changeDue * 100) / 100;
        amount = Math.round(amount * 100) / 100;
      }
      if (unitAmount > 0) {
        change.push([unit, unitAmount]);
      }
    }
    if (changeDue > 0) {
      return { status: "INSUFFICIENT_FUNDS", change: [] };
    }
    return { status: "OPEN", change: change };
  }
}

checkCashRegister(19.5, 20, [["PENNY", 1.01], ["NICKEL", 2.05], ["DIME", 3.1], ["QUARTER", 4.25], ["ONE", 90], ["FIVE", 55], ["TEN", 20], ["TWENTY", 60], ["ONE HUNDRED", 100]]);