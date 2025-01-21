function randomCase(x) {
  
    let result = "";
     for (let i = 0; i < x.length; i++) {
       const char = x[i];
       if (/[a-zA-Z]/.test(char)) {
         if (Math.random() < 0.5) {
           result += char.toUpperCase();
         } else {
           result += char.toLowerCase();
         }
       } else {
         result += char;
       }
     }
     return result;
   }