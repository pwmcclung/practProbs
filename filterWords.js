function wantedWords(n, m, forbid_let){
    let filtered = wordList.filter((x)=> x.length == n+m);
    filtered = filtered.filter(word => !forbid_let.some(letter => word.includes(letter)));
    let arr = [];
  for (let i = 0; i < filtered.length;i++){
     arr.push(vowelChecker(filtered[i], n));
  }
  return arr.filter((x)=> x != 0);
}

function vowelChecker(word, n){
  let vowels = ['a', 'e', 'i', 'o', 'u'];
  let splitWord = word.split('');
  let count = 0;
  for (let i = 0; i < splitWord.length;i++){
    if (vowels.includes(splitWord[i] )){
      count++;
    }
  }
  if (count == n){
    return word;
  }else{
    return 0;
  }
}