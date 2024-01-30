#!/usr/bin/node
const request = require('request');

const url = process.argv[2];

request(url, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const todos = JSON.parse(body);
    const userTasks = {};
    for (const task of todos) {
      if (task.completed) {
        if (userTasks[task.userId]) {
          userTasks[task.userId] += 1;
        } else {
          userTasks[task.userId] = 1;
        }
      }
    }
    console.log(userTasks);
  }
});
