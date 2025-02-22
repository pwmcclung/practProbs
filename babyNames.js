function validName(array) {
    if (!array || array.length === 0) {
      return "You must test at least one name.";
    }
  
    if (array.length === 1) {
      return "Congratulations, you can choose any name you like!";
    }
  
    for (let i = 1; i < array.length; i++) {
      const previousName = array[i - 1].trim();
      const currentName = array[i].trim();
  
      const lastLetterPrevious = previousName.split(' ').pop().split('-').pop().slice(-1).toLowerCase();
      const firstLetterCurrent = currentName.split(' ').shift().split('-').shift().slice(0, 1).toLowerCase();
      
      if (lastLetterPrevious !== firstLetterCurrent) {
        return "Back to the drawing board, your baby names are not compatible.";
      }
    }
  
    return "Congratulations, your baby names are compatible!";
  }