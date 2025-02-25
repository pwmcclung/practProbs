function travelDistance(avgSpeed, travelTime) {
    const travelTimeHours = travelTime / 60;
    const distanceNauticalMiles = avgSpeed * travelTimeHours;
    const distanceKilometers = distanceNauticalMiles * 1.852;
    return distanceKilometers;
 }
 