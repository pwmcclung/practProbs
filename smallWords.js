function smallWordHelper(sentence){
    let arr = [];
    let sentSplit = sentence.split(' ');
    for (let x of sentSplit){
      if (x.length <=3){
        arr.push(x.toUpperCase());
      }else {
        arr.push(remover(x));
      }
    }
    return arr.join(' ');
  }
  
  function remover(word){
    let vowels = 'aeiouAEIOU'.split('');
    let splitWord = word.split('');
    let newWord = splitWord.filter((x) => !vowels.includes(x));
    return newWord.join('');
  }