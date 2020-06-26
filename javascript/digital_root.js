function digital_root(n) {
    if (n <= 9) { return n };
    const digitsArray = n.toString().split("");
    const sumOfDigits = digitsArray.reduce((acc, digit) => {
        return acc + parseInt(digit, 10);
    }, 0);
    return digital_root(sumOfDigits);
}

// Tests

console.log(digital_root(16) === 7);
console.log(digital_root(456) === 6);

// Modulo 9 Arithmetic
// for (let i = 1; i <= 400; i++) {
//     const digitsArray = i.toString().split("");
//     const sumOfDigits = digitsArray.reduce((acc, digit) => {
//         return acc + parseInt(digit, 10);
//     }, 0);
//     console.log(sumOfDigits);
// }

// for (let i = 1; i <= 400; i++) {
//     console.log(i % 9);
// }

// console.log(digital_root(9));