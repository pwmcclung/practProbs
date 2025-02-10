function heggeleggleggo(word){
    let cons = 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ'.split('');
    let arr = [];
    let wordArr = word.split('');
    for (let i = 0; i < wordArr.length;i++){
      let item = word[i];
      if (cons.includes(item)){
        arr.push(item+'egg');
      }else{
        arr.push(item);
      }
    }
    return arr.join('');
  }