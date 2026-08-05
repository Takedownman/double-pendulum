# Double Pendulum

A high-quality double pendulum simulation that demonstrates deterministic chaos and sensitive dependence on initial conditions.

Built using the exact Lagrangian equations of motion, with energy conservation tracking and a side-by-side comparison of two nearly identical systems.

**Made by Takedownman**

---

### What this project shows

This simulation integrates the full nonlinear equations of a double pendulum and visualizes how a tiny difference in starting angle (10 micro-radians) grows into completely different trajectories.  

It also tracks total energy over time to confirm the numerical integration remains faithful to the underlying physics.

**Key features:**
- Exact Lagrangian equations of motion
- Two pendulums started with a 10 µrad difference
- Real-time visualization of chaotic divergence
- Energy conservation diagnostic
- Clean dark academic-style plots
- High-quality animation output

---

### Requirements

```bash
pip install numpy scipy matplotlib
