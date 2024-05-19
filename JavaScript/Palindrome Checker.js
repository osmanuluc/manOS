function palindrome(str) {
    // Step 1: Remove non-alphanumeric characters and convert to lowercase
    const cleanStr = str.replace(/[^a-zA-Z0-9]/g, '').toLowerCase();
  
    // Step 2: Compare with its reverse
    const reversedStr = cleanStr.split('').reverse().join('');
  
    // Step 3: Check if they are the same
    return cleanStr === reversedStr;
  }