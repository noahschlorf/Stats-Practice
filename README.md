# Random Variable Initialization Script

## Overview

This script is designed for statistical calculations involving random variables. It includes the initialization of variables, function definitions, statistical calculations, user interaction, error handling, and print statements for debugging.

### Random Variable Initialization

- The script initializes random variables for `x` and `y` values.
- It also sets lower and upper bounds for integration.

### Function Definition

- Defines a function `f` as a linear combination of `x` and `y`.

### Statistical Calculations

- Integration of the function `f` over `x` and `y` to find marginal distributions.
- Calculation of expected values (`E(X)`, `E(Y)`), variances (`Var(X)`, `Var(Y)`), and covariance (`Cov(X,Y)`) of `x` and `y`.
- Determination of independence between `x` and `y`.
- Calculation of the correlation coefficient between `x` and `y`.

### User Interaction

- Prompts the user to input expected values, variances, and other statistical measures.
- Compares user inputs with calculated values to provide feedback on correctness.

### Error Handling

- Includes error handling for user inputs.
- Allows users to enter 'stop' to quit the process.

### Print Statements

- Contains print statements for debugging and understanding the flow of calculations.
