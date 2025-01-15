function seven(m) {
    let steps = 0;
    while (m > 99) {
      const y = m % 10;
      const x = Math.floor(m / 10);
      m = x - 2 * y;
      steps++;
    }
    return [m, steps];
  }