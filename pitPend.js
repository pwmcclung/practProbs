function pendulum(values) {  
    let sortedVals = values.sort((a,b) => a - b);
    let ordered = [sortedVals.shift()];
    let count = 0;
    while (sortedVals.length > 0){
      let first = sortedVals.shift();
      if (count % 2 == 0){
        ordered.push(first);
      }else{
        ordered.unshift(first);
      }
      count++;
    }
  return ordered;
}