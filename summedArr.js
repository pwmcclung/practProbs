function sum(...arr) {
    const callback = typeof arr[arr.length - 1] === 'function' ? arr.pop() : null;
    const arrays = arr;
  
    let maxLength = 0;
    for (const array of arrays) {
      maxLength = Math.max(maxLength, array.length);
    }
  
    let totalSum = 0;
    for (let i = 0; i < maxLength; i++) {
      const values = [];
      for (const array of arrays) {
        values.push(array[i] === undefined ? 0 : array[i]);
      }
  
      let result;
      if (callback) {
        result = callback(...values);
      } else {
        result = values.reduce((a, b) => a + b, 0);
      }
      totalSum += result;
    }
  
    return totalSum;
  }