function workOnStrings(a, b) {
    let newA = "";
    let newB = "";
  
    for (let char of a) {
      let count = 0;
      for (let other of a.toLowerCase()) {
        if (char.toLowerCase() === other) {
          count++;
        }
      }
  
      let tempB = "";
      for (let i = 0; i < b.length; i++) {
        if (b[i].toLowerCase() === char.toLowerCase()) {
          tempB += swapCase(b[i], count);
        } else {
          tempB += b[i];
        }
      }
      newB = tempB;
      b=newB
    }
  
      for (let char of b) {
      let count = 0;
      for (let other of b.toLowerCase()) {
        if (char.toLowerCase() === other) {
          count++;
        }
      }
  
      let tempA = "";
      for (let i = 0; i < a.length; i++) {
        if (a[i].toLowerCase() === char.toLowerCase()) {
          tempA += swapCase(a[i], count);
        } else {
          tempA += a[i];
        }
      }
      newA = tempA;
      a = newA
    }
  
  
  
  
    return newA + newB;
  }
  
  function swapCase(char, count) {
    for (let i = 0; i < count; i++) {
      if (char === char.toLowerCase()) {
        char = char.toUpperCase();
      } else {
        char = char.toLowerCase();
      }
    }
    return char;
  }