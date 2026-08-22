"""
Double Pendulum - Streamlit Version
Exact Lagrangian equations + chaos demonstration

Made by Takedownman
"""

import streamlit as st
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# -------------------------------------------------
# Page config
# -------------------------------------------------
st.set_page_config(
    page_title="Double Pendulum | Takedownman",
    page_icon="🌀",
    layout="wide"
)

st.title("Double Pendulum Chaos Simulator")
st.caption("Made by Takedownman")

st.markdown("""
This simulation uses the **exact Lagrangian equations** of a double pendulum  
and demonstrates sensitive dependence on initial conditions (chaos).
""")

# -------------------------------------------------
# Sidebar controls
# -------------------------------------------------
st.sidebar.header("Parameters")

L1 = st.sidebar.slider("Length 1 (L1)", 0.5, 2.0, 1.0, 0.1)
L2 = st.sidebar.slider("Length 2 (L2)", 0.5, 2.0, 1.0, 0.1)
m1 = st.sidebar.slider("Mass 1 (m1)", 0.5, 3.0, 1.0, 0.1)
m2 = st.sidebar.slider("Mass 2 (m2)", 0.5, 3.0, 1.0, 0.1)

theta1_0 = st.sidebar.slider("θ1 initial (degrees)", -180, 180, 120)
theta2_0 = st.sidebar.slider("θ2 initial (degrees)", -180, 180, -60)

duration = st.sidebar.slider("Simulation time (seconds)", 5, 40, 20)
perturbation = st.sidebar.slider("Perturbation (µrad)", 1, 50, 10)

g = 9.81

# -------------------------------------------------
# Physics
# -------------------------------------------------
def deriv(state, t, L1, L2, m1, m2):
    θ1, ω1, θ2, ω2 = state
    delta = θ2 - θ1
    den1 = (m1 + m2) * L1 - m2 * L1 * np.cos(delta)**2
    den2 = (L2 / L1) * den1

    ω1_dot = (
        m2 * L1 * ω2**2 * np.sin(delta) * np.cos(delta)
        + m2 * g * np.sin(θ2) * np.cos(delta)
        - (m1 + m2) * g * np.sin(θ1)
    ) / den1

    ω2_dot = (
        -m2 * L2 * ω2**2 * np.sin(delta) * np.cos(delta)
        + (m1 + m2) * g * np.sin(θ1) * np.cos(delta)
        - (m1 + m2) * g * np.sin(θ2)
    ) / den2

    return [ω1, ω1_dot, ω2, ω2_dot]


def energy(state, L1, L2, m1, m2):
    θ1, ω1, θ2, ω2 = state
    # Kinetic
    T1 = 0.5 * m1 * (L1 * ω1)**2
    T2 = 0.5 * m2 * (
        (L1 * ω1)**2 + (L2 * ω2)**2
        + 2 * L1 * L2 * ω1 * ω2 * np.cos(θ1 - θ2)
    )
    # Potential
    V1 = -m1 * g * L1 * np.cos(θ1)
    V2 = -m2 * g * (L1 * np.cos(θ1) + L2 * np.cos(θ2))
    return T1 + T2 + V1 + V2


# -------------------------------------------------
# Solve
# -------------------------------------------------
t = np.linspace(0, duration, int(duration * 40))

# Main system
state0 = [np.radians(theta1_0), 0.0, np.radians(theta2_0), 0.0]
sol1 = odeint(deriv, state0, t, args=(L1, L2, m1, m2), rtol=1e-9, atol=1e-9)

# Perturbed system (tiny difference)
state0_pert = [np.radians(theta1_0) + perturbation * 1e-6, 0.0,
               np.radians(theta2_0), 0.0]
sol2 = odeint(deriv, state0_pert, t, args=(L1, L2, m1, m2), rtol=1e-9, atol=1e-9)

# Cartesian coordinates
x1 = L1 * np.sin(sol1[:, 0])
y1 = -L1 * np.cos(sol1[:, 0])
x2 = x1 + L2 * np.sin(sol1[:, 2])
y2 = y1 - L2 * np.cos(sol1[:, 2])

x1p = L1 * np.sin(sol2[:, 0])
y1p = -L1 * np.cos(sol2[:, 0])
x2p = x1p + L2 * np.sin(sol2[:, 2])
y2p = y1p - L2 * np.cos(sol2[:, 2])

# Energy
E = np.array([energy(s, L1, L2, m1, m2) for s in sol1])
E_drift = E - E[0]

# Separation (chaos measure)
sep = np.sqrt((x2 - x2p)**2 + (y2 - y2p)**2)

# -------------------------------------------------
# Plots
# -------------------------------------------------
col1, col2 = st.columns(2)

with col1:
    st.subheader("Trajectories")
    fig1, ax1 = plt.subplots(figsize=(6, 6), facecolor="#0e1117")
    ax1.set_facecolor("#0e1117")
    ax1.plot(x2, y2, color="#4fc3f7", lw=1.2, alpha=0.9, label="System 1")
    ax1.plot(x2p, y2p, color="#ff8a65", lw=1.0, alpha=0.75, label="Perturbed")
    ax1.plot(0, 0, "o", color="white", markersize=6)
    ax1.set_xlim(-2.2, 2.2)
    ax1.set_ylim(-2.2, 2.2)
    ax1.set_aspect("equal")
    ax1.grid(True, alpha=0.15, color="white")
    ax1.tick_params(colors="white")
    ax1.legend(facecolor="#1e1e1e", labelcolor="white")
    for spine in ax1.spines.values():
        spine.set_color("#444")
    st.pyplot(fig1)

with col2:
    st.subheader("Energy Conservation")
    fig2, ax2 = plt.subplots(figsize=(6, 4), facecolor="#0e1117")
    ax2.set_facecolor("#0e1117")
    ax2.plot(t, E_drift, color="#81c784", lw=1.5)
    ax2.axhline(0, color="white", lw=0.8, alpha=0.4)
    ax2.set_xlabel("Time (s)", color="white")
    ax2.set_ylabel("Energy drift", color="white")
    ax2.tick_params(colors="white")
    ax2.grid(True, alpha=0.15, color="white")
    for spine in ax2.spines.values():
        spine.set_color("#444")
    st.pyplot(fig2)

st.subheader("Sensitive Dependence (Chaos)")
fig3, ax3 = plt.subplots(figsize=(10, 3.5), facecolor="#0e1117")
ax3.set_facecolor("#0e1117")
ax3.semilogy(t, sep + 1e-16, color="#ce93d8", lw=1.5)
ax3.set_xlabel("Time (s)", color="white")
ax3.set_ylabel("Separation (log scale)", color="white")
ax3.tick_params(colors="white")
ax3.grid(True, alpha=0.15, color="white")
for spine in ax3.spines.values():
    spine.set_color("#444")
st.pyplot(fig3)

st.markdown("---")
st.markdown("**Made by Takedownman**  \nExact Lagrangian mechanics • Energy conservation • Chaos demonstration")
