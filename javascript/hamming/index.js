// Define your Hamming class here.
// `npm test` to ensure the unit tests pass and
// your code meets all of the conditions.
// You may use ES6 or ES5 to solve.

function Hamming() { }

Hamming.prototype.compute = function(s1, s2) {
    if(s1.length != s2.length) throw 'DNA strands must be of equal length.';
    var num = 0;
    for (x = 0; x < s1.length; x++) {
      if (s1[x] != s2[x]) {
        num++;
      }
    }
    return num;
  };

module.exports = Hamming;


