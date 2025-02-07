function gracefulTipping(bill) {
    let tip = bill * 0.15;
    let total = bill + tip;
  
    if (total < 10) {
      return Math.ceil(total);
    } else if (total < 100) {
      return Math.ceil(total / 5) * 5;
    } else if (total < 1000) {
      return Math.ceil(total / 50) * 50;
    } else if (total < 10000) {
      return Math.ceil(total / 500) * 500;
    } else {
      let magnitude = Math.floor(Math.log10(total));
      let divisor = 5 * Math.pow(10, magnitude - 1);
      return Math.ceil(total / divisor) * divisor;
    }
  }