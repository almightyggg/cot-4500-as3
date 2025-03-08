# cot-4500-as3
# Numerical Methods for ODEs

## Repository: cot-4500-as3

### Description
This repository contains Python implementations of numerical methods for solving ordinary differential equations (ODEs). The implemented methods include:

- **Euler Method**: A simple first-order numerical procedure for solving initial value problems.
- **Runge-Kutta Method (RK4)**: A higher-order method that provides better accuracy.

### Problem Statement
The differential equation given is:

\[ f'(t) = t - y^2 \]

with the following conditions:
- **Initial Condition**: \( f(0) = 1 \)
- **Range**: \( 0 < t < 2 \)
- **Iterations**: 10

The goal is to approximate the value of \( f(2) \) using both numerical methods.

### Files
- `numerical_methods.py`: Contains the implementation of Euler and Runge-Kutta methods.
- `README.md`: Provides an overview of the project.
- `requirements.txt`: Lists required dependencies (only NumPy is included if needed).

### Installation & Usage
To ensure all dependencies are installed, run:
```bash
pip install -r requirements.txt
```

To execute the program, use the following command:
```bash
python numerical_methods.py
```

### Expected Output
```
Euler Method Result: 1.2446380979332121
Runge-Kutta Method Result: 1.251316587879806
```

### Dependencies
- Python 3.x
- NumPy (optional but recommended for further extensions)

### License
This project is for educational purposes only and is released under the MIT License.
