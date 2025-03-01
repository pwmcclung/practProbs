function companyBotStrategy(trainingData) {
    let count = 0;
    let score = [];
    for (let i = 0; i < trainingData.length; i++){
     if (trainingData[i][1] == 1){
       score.push(trainingData[i][0])
     }
    }
    let scoreReduced = score.reduce((a,b) => a+b,0);
    if (scoreReduced > 0){
      return scoreReduced / score.length;
    }
    return 0;
  }