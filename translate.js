function tongues(code) {
    let vowels = {'a' :'e','i':'o', 'y':'u', 'e' :'a','o':'i', 'u':'y'};
    let vowelsCap = {'A':'E', 'I':'O', 'Y':'U', 'E':'A', 'O':'I', 'U':'Y'};
    let cons = {'b':'p', 'k':'v', 'x':'j', 'z':'q', 'n':'t', 'h':'s', 'd':'r', 'c':'l', 'w':'m', 'g':'f', 'p':'b', 'v':'k', 'j':'x', 'q':'z', 't':'n', 's':'h', 'r':'d', 'l':'c', 'm':'w', 'f':'g'};
    let consCap = {'B':'P','K':'V', 'X':'J','Z':'Q', 'N':'T', 'H':'S', 'D':'R', 'C':'L', 'W':'M', 'G':'F', 'P':'B', 'V':'K', 'J':'X', 'Q':'Z', 'T':'N', 'S':'H', 'R':'D', 'L':'C', 'M':'W', 'F':'G'};
      
    let codeSplit = code.split('');
    let newCode = [];
    for (let i = 0; i < codeSplit.length;i++){
      if (vowels[codeSplit[i]]){
        newCode.push(vowels[codeSplit[i]]);
      }else if (vowelsCap[codeSplit[i]]){
        newCode.push(vowelsCap[codeSplit[i]]);
      }else if (cons[codeSplit[i]]){
        newCode.push(cons[codeSplit[i]]);
      }else if (consCap[codeSplit[i]]){
        newCode.push(consCap[codeSplit[i]]);
      }else {
        newCode.push(codeSplit[i]);
      }
    }
      return newCode.join('');
    }