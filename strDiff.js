function findAdded(st1, st2) {
    // Count frequencies in both strings
    const freq1 = {};
    const freq2 = {};
    
    // Count frequencies in st1
    for (let num of st1) {
        freq1[num] = (freq1[num] || 0) + 1;
    }
    
    // Count frequencies in st2
    for (let num of st2) {
        freq2[num] = (freq2[num] || 0) + 1;
    }
    
    // Find numbers with higher frequency in st2
    let result = '';
    for (let num in freq2) {
        const count1 = freq1[num] || 0;
        const count2 = freq2[num];
        if (count2 > count1) {
            // Add the number (count2 - count1) times
            result += num.repeat(count2 - count1);
        }
    }
    
    // Sort the result and return
    return result.split('').sort().join('');
}