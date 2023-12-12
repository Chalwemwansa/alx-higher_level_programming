#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let num = 0;
  for (const occur of list) {
    if (occur === searchElement) {
      num += 1;
    }
  }
  return num;
};
