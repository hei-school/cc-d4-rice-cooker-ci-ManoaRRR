[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/__xb4cFP)
# RiceCooker

The `RiceCooker` is a JavaScript class simulating the operation of a rice cooker. It allows you to set the rice type, water level, and cooking time while providing methods to start and stop cooking, as well as to check the cooking status.

## Features

setRiceType(riceType): Set the type of rice.
setWaterLevel(level): Set the water level (between 0 and 100).
setCookingTime(timeMinutes): Set the cooking time (between 0 and 60 minutes).
startCooking(): Start cooking based on the defined parameters.
stopCooking(): Stop the ongoing cooking if it is in progress.
checkCookingStatus(): Returns the current state of the rice cooker.

## Unit Tests
Unit tests are included to verify the proper functioning of the RiceCooker class. You can run them using a test framework like Mocha and Chai.

```bash
npm install mocha chai --save-dev
npx mocha path-to-your-test-file.js
