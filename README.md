[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/__xb4cFP)
# RiceCooker

The `RiceCooker` is a Python class simulating the operation of a rice cooker. It allows you to set the rice type, water level, and cooking time while providing methods to start and stop cooking, as well as to check the cooking status.

## Features

- `set_rice_type(rice_type)`: Set the type of rice.
- `set_water_level(level)`: Set the water level (between 0 and 100).
- `set_cooking_time(time_minutes)`: Set the cooking time (between 0 and 60 minutes).
- `start_cooking()`: Start cooking based on the defined parameters.
- `stop_cooking()`: Stop the ongoing cooking if it is in progress.
- `check_cooking_status()`: Returns the current state of the rice cooker.

## Unit Tests

Unit tests are included to verify the proper functioning of the `RiceCooker` class. You can run them using a test framework like `unittest`.

```bash
cd python
python -m unittest test_rice_cooker.py
