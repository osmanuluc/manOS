function rot13(str) {
    return str.replace(/[A-Z]/g, function(char) {
      // Get the Unicode code of the character
      let code = char.charCodeAt(0);
  
      // A = 65, Z = 90
      if (code >= 65 && code <= 90) {
        // Shift the character code by 13 places
        code = code - 13 < 65 ? code + 13 : code - 13;
      }
  
      // Convert the Unicode code back to a character
      return String.fromCharCode(code);
    });
  }
  
  rot13("SERR PBQR PNZC");