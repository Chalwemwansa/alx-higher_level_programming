#!/usr/bin/node

exports.esrever = function (list) {
  const iteration = Math.floor(list.length / 2);
  const max = list.length - 1;
  for (let i = 0; i < iteration; i++) {
    const temp = list[i];
    list[i] = list[max - i];
    list[max - i] = temp;
  }
  return list;
};
