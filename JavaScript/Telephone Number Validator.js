function telephoneCheck(str) {
    // Regular expression for validating US phone numbers
    var regex = /^(1\s?)?(\(\d{3}\)|\d{3})[\s\-]?\d{3}[\s\-]?\d{4}$/;
    
    // Test the string against the regular expression
    return regex.test(str);
  }
  
  telephoneCheck("555-555-5555");