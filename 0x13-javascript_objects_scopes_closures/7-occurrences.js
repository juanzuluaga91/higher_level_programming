#!/usr/bin/node
exports.nbOccurences = function (list, finder) {
  let oc = 0;
  for (let index = 0; index in list; index++) {
    if (list[index] === finder) {
      oc++;
    }
  }
  return oc;
};
