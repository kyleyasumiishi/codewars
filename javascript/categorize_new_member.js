function openOrSenior(data) {
    return data.map(([age, handicap]) => age > 54 && handicap > 7 ? "Senior" : "Open");
}




// Tests

console.log(openOrSenior([[45, 12],[55,21],[19, -2],[104, 20]]));
console.log(openOrSenior([[3, 12],[55,1],[91, -2],[54, 23]]));
console.log(openOrSenior([[59, 12],[55,-1],[12, -2],[12, 12]]));
