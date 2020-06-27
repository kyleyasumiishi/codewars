function tribonacci(signature, n) {
    if (n < 4) { return signature.slice(0, n); } 
    const seq = [...signature];
    let a = seq[0], b = seq[1], c = seq[2];
    for (let i = 0; i < n; i++) {
        seq.push(a + b + c);
        a = seq[i + 1], b = seq[i + 2], c = seq[i + 3];
    }
    return seq.slice(0, n);
}

// Tests

// console.log(tribonacci([1,1,1],1));
// console.log(tribonacci([1,1,1],10));
// console.log(tribonacci([300,200,100],0));
