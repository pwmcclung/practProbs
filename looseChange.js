function changeCount( change ){
    let sum = 0;
    let changeSplit = change.split(' ');
    for (let i =0; i < changeSplit.length;i++){
      sum+= CHANGE[changeSplit[i]]
    }
    let strSum = sum.toFixed(2);
    if (strSum.length < 4){
      strSum+='0';
    }
    return '$' + strSum;
  }