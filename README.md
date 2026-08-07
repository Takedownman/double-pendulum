# Double Pendulum

High-accuracy simulation of a chaotic double pendulum using the exact Lagrangian equations of motion.

This project demonstrates deterministic chaos and sensitive dependence on initial conditions by integrating two nearly identical systems side-by-side (differing by only 10 µrad).

**Made by Takedownman**

---

### Features

- Exact Lagrangian equations of motion
- Dual trajectory comparison (10 micro-radian perturbation)
- Energy conservation diagnostic
- Exponential divergence visualization
- Clean dark academic-style animation
- High-quality MP4 output

---

### Core Equations

The system is derived from the Lagrangian \(\mathcal{L} = T - V\). The equations of motion are integrated as a first-order system:

```python
def deriv(y, t, L1, L2, m1, m2):
    θ1, ω1, θ2, ω2 = y
    c = np.cos(θ1 - θ2)
    s = np.sin(θ1 - θ2)
    den = m1 + m2 * s**2

    ω1dot = (m2*g*np.sin(θ2)*c
             - m2*s*(L1*ω1**2*c + L2*ω2**2)
             - (m1+m2)*g*np.sin(θ1)) / (L1 * den)

    ω2dot = ((m1+m2)*(L1*ω1**2*s - g*np.sin(θ2)
                      + g*np.sin(θ1)*c)
             + m2*L2*ω2**2*s*c) / (L2 * den)

    return [ω1, ω1dot, ω2, ω2dot]

---

### Requirements

```bash
pip install numpy scipy matplotlib
