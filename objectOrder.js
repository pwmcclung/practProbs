function premierLeagueStandings(teamStandings) {
    // Extract the team that finished first last season
    const firstPlaceTeam = teamStandings[1];
  
    // Create an array of the other teams
    const otherTeams = [];
    for (const position in teamStandings) {
      if (parseInt(position) !== 1) { // Ensure position is treated as a number
        otherTeams.push(teamStandings[position]);
      }
    }
  
    // Sort the other teams alphabetically
    otherTeams.sort();
  
    // Create the new standings object
    const newStandings = {
      1: firstPlaceTeam,
    };
  
    // Add the other teams to the new standings object
    for (let i = 0; i < otherTeams.length; i++) {
      newStandings[i + 2] = otherTeams[i];
    }
  
    return newStandings;
  }