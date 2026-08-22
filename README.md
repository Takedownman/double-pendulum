# Double Pendulum Chaos Simulator

https://double-pendulum-btfvb4smvqcutujjyysras.streamlit.app/

A clean and educational simulation of a **double pendulum** that demonstrates chaotic motion.

**Created by:** Takedownman

---

## What is a Double Pendulum?

A double pendulum consists of two pendulums attached end-to-end.

Even though the physics is completely deterministic (no randomness is involved), the motion quickly becomes **chaotic**. Extremely small differences in the starting angles grow into completely different paths over time. This is one of the most famous examples of chaos in classical physics.

This project numerically solves the equations of motion and animates the pendulum in real time so you can observe the chaotic behavior yourself.

---

## Features

- Real-time animation of a double pendulum
- Accurate physics based on Lagrangian mechanics
- Numerical integration of the equations of motion
- Adjustable starting angles, lengths, and masses
- Trail visualization to clearly show chaotic paths
- Clean, well-commented code
- Easy for beginners to run and experiment with

---

## Libraries Used

| Library       | Purpose                              |
|---------------|--------------------------------------|
| **NumPy**     | Numerical calculations and arrays    |
| **Matplotlib**| Real-time animation and plotting     |
| **SciPy**     | Optional ODE solvers                 |

These are the only external libraries required.

---

## Requirements

- Python 3.8 or newer
- The libraries listed above

---

## Installation (Beginner Friendly)

1. Make sure Python is installed. You can check by opening a terminal and running:

```bash
python --version

Install the required libraries with one command:

Bashpip install numpy matplotlib scipy
Or if the project includes a requirements.txt file:
Bashpip install -r requirements.txt

How to Run the Program

Open a terminal in the project folder.
Run the main file:

Bashpython double_pendulum.py
(If the main file has a different name such as main.py or simulate.py, use that name instead.)

A window will open showing the double pendulum in motion.
Close the window to stop the simulation.

That is all — no complicated setup is required.

Project Structure
textDouble-Pendulum/
├── double_pendulum.py     # Main simulation file
├── physics.py             # Equations of motion (optional)
├── requirements.txt
├── README.md
└── images/                # Optional saved animations or plots

Physics Explanation (Simple Version)
The double pendulum is described by four state variables:

θ₁ — angle of the first pendulum
θ₂ — angle of the second pendulum
ω₁ — angular velocity of the first pendulum
ω₂ — angular velocity of the second pendulum

Using Lagrangian mechanics, a system of differential equations is derived that describes how these angles and velocities change over time.
Because the equations are nonlinear, the system is extremely sensitive to initial conditions. This sensitivity is the origin of the chaotic behavior.
The code integrates the equations forward in time using a numerical method (typically 4th-order Runge-Kutta or SciPy’s ODE solver) and draws the positions of the two masses at every time step.

Tips for Experimenting

Change the starting angles slightly and watch how the motion diverges.
Try different lengths or masses.
Increase the simulation duration to observe long-term chaotic behavior.
Enable a trail so you can see the path traced by the lower mass.


Credits
Created by: Takedownman
This project was built as a physics and programming crossover demonstration, inspired by classical mechanics and chaos theory.

License
MIT License – free to use, modify, and learn from.

Enjoy watching the chaos unfold.
If you find this project useful, feel free to star the repository.
