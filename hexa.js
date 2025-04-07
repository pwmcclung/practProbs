String.prototype.hexNumber = function() {
    if (!this) {
      return false;
    }
  
    // Regular expression for hexadecimal numbers (with or without 0x prefix)
    const hexPattern = /^(0[xX])?[0-9a-fA-F]+$/;
  
    return hexPattern.test(this);
  };