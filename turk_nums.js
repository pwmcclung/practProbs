const getTurkishNumber = (num) => {
    let singlesMap = {1: 'bir',2:'iki', 3:'üç', 4:'dört',5:'beş',6:'altı',7:'yedi',8:'sekiz',9:'dokuz',0:'sıfır'};
    let multTensMap = {10:'on',20:'yirmi',30:'otuz',40:'kırk',50:'elli',60:'altmış',70:'yetmiş',80:'seksen',90:'doksan'};
     if (Number(num) < 10){
       return singlesMap[Number(num)];
     }else{
       let numSplit = String(num).split('');
       if (numSplit[1] == '0'){
         return multTensMap[num];
       }else{
         let newNum = num - Number(numSplit[1]);
         return `${multTensMap[newNum]} ${singlesMap[Number(numSplit[1])]}`;
       }
     }
   }