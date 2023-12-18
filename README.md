[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/__xb4cFP)
# Multi-Language RiceCooker Project

This project provides a simple `RiceCooker` class implemented in different programming languages, including Python, PHP, and JavaScript. The `RiceCooker` class simulates the operation of a rice cooker and allows users to set various parameters for cooking rice.

## Versions

- [Python Version](./python/): Implementation in Python.
- [PHP Version](./php/): Implementation in PHP.
- [JavaScript Version](./javascript/): Implementation in JavaScript.

Choose the version that suits your project needs and language preference.

## Description

The `RiceCooker` class provides the following features:

- **Set Rice Type:** `setRiceType(riceType)` - Set the type of rice.
- **Set Water Level:** `setWaterLevel(level)` - Set the water level (between 0 and 100).
- **Set Cooking Time:** `setCookingTime(timeMinutes)` - Set the cooking time (between 0 and 60 minutes).
- **Start Cooking:** `startCooking()` - Start cooking based on the defined parameters.
- **Stop Cooking:** `stopCooking()` - Stop the ongoing cooking if it is in progress.
- **Check Cooking Status:** `checkCookingStatus()` - Returns the current state of the rice cooker.

## Usage

Below is an example of how to use the `RiceCooker` class in the JavaScript version:

```javascript
const RiceCooker = require('./javascript/RiceCooker');

// Create an instance of the rice cooker
const riceCooker = new RiceCooker();

try {
    // Configure rice cooker parameters
    riceCooker.setRiceType('white rice');
    riceCooker.setWaterLevel(50);
    riceCooker.setCookingTime(0.5);

    // Start cooking
    riceCooker.startCooking();

    // Check cooking status
    console.log(riceCooker.checkCookingStatus());

    // Stop cooking
    riceCooker.stopCooking();
} catch (error) {
    console.error(`Error: ${error.message}`);
}
