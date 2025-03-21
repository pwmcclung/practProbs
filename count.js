function countZeros(n) {
    let count = 0;
    let start = 1;
    let arr = [];
    while (start < n){
      start += 1;
      if (start.toString().includes('0')){
        arr.push(start);
      }
    }
    let arrJoined =  arr.join('');
    let arrSplit = arrJoined.split('');
    let onlyZs = arrSplit.filter((x)=>x =='0');
    return onlyZs.length;
  }