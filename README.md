Double Pendulum Chaos Simulator
A clean, educational simulation of a double pendulum that demonstrates chaotic motion.
Created by Takedownman.

What is a Double Pendulum?
A double pendulum is two pendulums attached end-to-end.
Even though the physics is completely deterministic (no randomness), the motion becomes chaotic. Tiny differences in the starting angles grow into completely different paths over time. This is one of the most famous examples of chaos in classical physics.
This project numerically solves the equations of motion and animates the pendulum in real time so you can see the chaos yourself.

Features

Real-time animation of a double pendulum
Accurate physics using Lagrangian mechanics
Numerical integration (Runge-Kutta style)
Adjustable starting angles and lengths
Trail / path visualization so you can see the chaos
Clean, well-commented code
Easy for beginners to run and experiment with


Libraries Used

























LibraryPurposeNotesNumPyMath, arrays, numerical calculationsCore scientific computing libraryMatplotlibAnimation and plottingUsed for the live pendulum animationSciPyOptional ODE solversUsed if the code uses odeint or similar
These are the only external libraries required.

Requirements

Python 3.8 or newer
The libraries listed above


Installation (Beginner Friendly)

Make sure you have Python installed.
You can check by opening a terminal and typing:Bashpython --version
Install the required libraries with one command:Bashpip install numpy matplotlib scipyOr if the project has a requirements.txt file:Bashpip install -r requirements.txt


How to Run the Program

Open a terminal in the project folder.
Run the main file:Bashpython double_pendulum.py(If the main file has a different name such as main.py or simulate.py, use that name instead.)
A window should open showing the double pendulum moving.
Close the window to stop the simulation.

That’s it — no complicated setup needed.

Project Structure (Typical)
textDouble-Pendulum/
├── double_pendulum.py     # Main simulation file
├── physics.py             # Equations of motion (optional separation)
├── requirements.txt
├── README.md
└── images/ or results/    # Optional saved animations or plots

Physics Explanation (Simple Version)
The double pendulum has four state variables:

θ₁ = angle of the first pendulum
θ₂ = angle of the second pendulum
ω₁ = angular velocity of the first pendulum
ω₂ = angular velocity of the second pendulum

Using Lagrangian mechanics (a powerful way to derive equations of motion), we get a system of differential equations that describe how these angles and velocities change over time.
Because the equations are non-linear, the motion is extremely sensitive to initial conditions — this is chaos.
The code integrates these equations forward in time using a numerical method (usually 4th-order Runge-Kutta or SciPy’s ODE solver) and draws the positions of the two masses at every step.

Tips for Experimenting

Change the starting angles (especially make them slightly different) and watch how the motion diverges.
Try different lengths or masses.
Increase the simulation time to see long-term chaotic behavior.
Turn on a trail so you can see the path the lower mass traces.


Credits
Created by: Takedownman
This project was built as a physics + programming crossover demonstration, inspired by classical mechanics and chaos theory.

License
MIT License – free to use, modify, and learn from.

Enjoy watching the chaos unfold.
If you find this project useful, feel free to star the repository.
