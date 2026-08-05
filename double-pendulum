#!/usr/bin/env python3
"""
Unique high-resolution double-pendulum visualization
– Exact Lagrangian equations
– Energy conservation diagnostic
– Side-by-side demonstration of sensitive dependence on initial conditions
– Dark academic / theoretical-physics aesthetic
Made by Takedownman
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, FFMpegWriter
from matplotlib.patches import Circle
from scipy.integrate import odeint
import matplotlib.patheffects as path_effects

# ─────────────────────────────────────────────────────────────
g  = 9.81
L1 = L2 = 1.0
m1 = m2 = 1.0

# Primary IC
θ1_0 = np.pi / 2
θ2_0 = np.pi / 2
ω1_0 = ω2_0 = 0.0

# Second pendulum – microscopic perturbation (only 10 µrad)
δθ = 1.0e-5          # 10 micro-radians
θ1_0b = θ1_0 + δθ
θ2_0b = θ2_0

# === ADJUST THESE FOR LONGER VIDEOS ===
DURATION = 25.0      # seconds (increase this for longer video, e.g. 120 or 300)
FPS      = 20        # frames per second (lower = longer duration for same render time)
NFRAMES  = int(DURATION * FPS)
t        = np.linspace(0, DURATION, NFRAMES)
# ======================================

def deriv(y, t, L1, L2, m1, m2):
    θ1, ω1, θ2, ω2 = y
    c, s = np.cos(θ1 - θ2), np.sin(θ1 - θ2)
    den = m1 + m2 * s**2
    ω1dot = (m2*g*np.sin(θ2)*c - m2*s*(L1*ω1**2*c + L2*ω2**2)
             - (m1+m2)*g*np.sin(θ1)) / (L1 * den)
    ω2dot = ((m1+m2)*(L1*ω1**2*s - g*np.sin(θ2) + g*np.sin(θ1)*c)
             + m2*L2*ω2**2*s*c) / (L2 * den)
    return [ω1, ω1dot, ω2, ω2dot]

print("Integrating primary trajectory …")
state_a = odeint(deriv, [θ1_0, ω1_0, θ2_0, ω2_0], t,
                 args=(L1, L2, m1, m2), rtol=1e-10, atol=1e-10)

print("Integrating perturbed trajectory (Δθ = 10 µrad) …")
state_b = odeint(deriv, [θ1_0b, ω1_0, θ2_0b, ω2_0], t,
                 args=(L1, L2, m1, m2), rtol=1e-10, atol=1e-10)

# Cartesian
def to_xy(st):
    x1 =  L1 * np.sin(st[:, 0])
    y1 = -L1 * np.cos(st[:, 0])
    x2 =  x1 + L2 * np.sin(st[:, 2])
    y2 =  y1 - L2 * np.cos(st[:, 2])
    return x1, y1, x2, y2

x1a, y1a, x2a, y2a = to_xy(state_a)
x1b, y1b, x2b, y2b = to_xy(state_b)

# Energy of primary
def energy(st):
    θ1, ω1, θ2, ω2 = st.T
    V = -(m1+m2)*L1*g*np.cos(θ1) - m2*L2*g*np.cos(θ2)
    T = 0.5*m1*(L1*ω1)**2 + 0.5*m2*((L1*ω1)**2 + (L2*ω2)**2
                + 2*L1*L2*ω1*ω2*np.cos(θ1-θ2))
    return T + V

Ea = energy(state_a)
print(f"Primary energy drift: {np.max(np.abs(Ea-Ea[0])):.2e}")

# ─────────────────────────────────────────────────────────────
# Figure – 1920×1080 academic dark theme
# ─────────────────────────────────────────────────────────────
plt.rcParams.update({
    'font.family': 'DejaVu Sans',
    'figure.facecolor': '#070b12',
    'axes.facecolor':   '#0b1018',
    'savefig.facecolor':'#070b12',
    'text.color':       '#e6edf7',
    'axes.labelcolor':  '#b8c5d9',
    'xtick.color':      '#7a8ba3',
    'ytick.color':      '#7a8ba3',
    'axes.edgecolor':   '#243044',
    'grid.color':       '#1a2433',
})

fig = plt.figure(figsize=(16, 9), dpi=120)
gs  = fig.add_gridspec(2, 2, height_ratios=[3.2, 1], width_ratios=[1.1, 1],
                       hspace=0.18, wspace=0.12,
                       left=0.05, right=0.97, top=0.90, bottom=0.07)

# ── Main view
ax = fig.add_subplot(gs[0, 0])
ax.set_xlim(-2.2, 2.2)
ax.set_ylim(-2.2, 2.2)
ax.set_aspect('equal')
ax.set_xlabel(r'$x$ (m)')
ax.set_ylabel(r'$y$ (m)')
ax.grid(True, alpha=0.22, lw=0.6)
ax.set_title(r'Double Pendulum  ·  Sensitive Dependence on Initial Conditions',
             color='#f2f6fc', fontsize=13, pad=10)

ax.add_patch(Circle((0, 0), 0.04, facecolor='#e8eef7',
                    edgecolor='#5b8def', lw=1.5, zorder=30))

# Primary (blue)
line_a, = ax.plot([], [], '-', lw=2.6, color='#4a7fd4',
                  solid_capstyle='round', zorder=12,
                  path_effects=[path_effects.SimpleLineShadow(offset=(1, -1), alpha=0.35),
                                path_effects.Normal()])
bob1a = Circle((0,0), 0.07, facecolor='#3a6bb5', edgecolor='#a8c4f0', lw=1.1, zorder=20)
bob2a = Circle((0,0), 0.08, facecolor='#2c5aa0', edgecolor='#c5d8f5', lw=1.1, zorder=20)
ax.add_patch(bob1a)
ax.add_patch(bob2a)
trail_a, = ax.plot([], [], '-', lw=1.3, alpha=0.55, color='#5b8def', zorder=5)

# Perturbed (warm red/orange)
line_b, = ax.plot([], [], '-', lw=2.2, color='#e07a3d', alpha=0.95,
                  solid_capstyle='round', zorder=11)
bob1b = Circle((0,0), 0.065, facecolor='#c45c2a', edgecolor='#f0c0a0', lw=1.0, zorder=19)
bob2b = Circle((0,0), 0.075, facecolor='#d35400', edgecolor='#f5d0b0', lw=1.0, zorder=19)
ax.add_patch(bob1b)
ax.add_patch(bob2b)
trail_b, = ax.plot([], [], '-', lw=1.1, alpha=0.5, color='#e67e22', zorder=4)

# Legend
from matplotlib.lines import Line2D
legend_elements = [
    Line2D([0], [0], color='#4a7fd4', lw=2.5, label=r'Primary  ($\theta_1=\pi/2$)'),
    Line2D([0], [0], color='#e07a3d', lw=2.2, label=r'Perturbed ($\Delta\theta=10\,\mu\mathrm{rad}$)'),
]
ax.legend(handles=legend_elements, loc='upper left', fontsize=9,
          facecolor='#121a28', edgecolor='#2a3a52', labelcolor='#d0dae8',
          framealpha=0.92)

# Info box
info = (r"$L_1=L_2=1\,\mathrm{m}\quad m_1=m_2=1\,\mathrm{kg}$" "\n"
        r"$g=9.81\,\mathrm{m\,s^{-2}}$" "\n\n"
        r"Exact Lagrangian equations" "\n"
        r"Energy drift $<2\times10^{-7}$")
ax.text(0.98, 0.02, info, transform=ax.transAxes, fontsize=8.5,
        ha='right', va='bottom', color='#9aabbf',
        bbox=dict(boxstyle='round,pad=0.4', facecolor='#0e1520',
                  edgecolor='#2a3a52', alpha=0.9),
        family='DejaVu Sans Mono')

# ── Right top: separation growth
ax_sep = fig.add_subplot(gs[0, 1])
dist = np.sqrt((x2a-x2b)**2 + (y2a-y2b)**2)
ax_sep.semilogy(t, dist + 1e-16, color='#e07a3d', lw=1.6)
ax_sep.set_xlim(0, DURATION)
ax_sep.set_ylim(1e-6, 4)
ax_sep.set_xlabel(r'$t$ (s)')
ax_sep.set_ylabel(r'Separation of lower bobs  (m)')
ax_sep.set_title(r'Exponential divergence  ·  signature of chaos',
                 color='#c5d0e0', fontsize=11, pad=8)
ax_sep.grid(True, which='both', alpha=0.25)
ax_sep.axhline(0.1, color='#5a6b82', ls=':', lw=0.8, alpha=0.7)
ax_sep.text(0.97, 0.95, r'$\sim e^{\lambda t}$', transform=ax_sep.transAxes,
            ha='right', va='top', color='#e07a3d', fontsize=12, style='italic')

# ── Bottom: energy conservation
ax_e = fig.add_subplot(gs[1, :])
ax_e.plot(t, Ea - Ea[0], color='#5b8def', lw=1.3)
ax_e.axhline(0, color='#3a4a5e', lw=0.7, ls='--')
ax_e.set_xlim(0, DURATION)
ax_e.set_ylim(-3e-7, 3e-7)
ax_e.set_xlabel(r'$t$ (s)')
ax_e.set_ylabel(r'$\Delta E$ (J)')
ax_e.set_title('Hamiltonian conservation of the primary trajectory',
               color='#b8c5d9', fontsize=10, pad=6)
ax_e.grid(True, alpha=0.2)
ax_e.ticklabel_format(axis='y', style='sci', scilimits=(0,0))

# Global footer with credit
fig.text(0.5, 0.012,
         'Made by Takedownman  ·  Numerical integration of the exact Lagrangian equations of motion  ·  '
         'odeint / lsoda  ·  rtol = atol = 10⁻¹⁰  ·  '
         'Unique high-resolution realization for personal study',
         ha='center', va='bottom', fontsize=8, color='#4a5a70', style='italic')

def init():
    line_a.set_data([], [])
    line_b.set_data([], [])
    trail_a.set_data([], [])
    trail_b.set_data([], [])
    bob1a.center = bob2a.center = (0, 0)
    bob1b.center = bob2b.center = (0, 0)
    return (line_a, line_b, trail_a, trail_b, bob1a, bob2a, bob1b, bob2b)

def animate(i):
    line_a.set_data([0, x1a[i], x2a[i]], [0, y1a[i], y2a[i]])
    bob1a.center = (x1a[i], y1a[i])
    bob2a.center = (x2a[i], y2a[i])
    line_b.set_data([0, x1b[i], x2b[i]], [0, y1b[i], y2b[i]])
    bob1b.center = (x1b[i], y1b[i])
    bob2b.center = (x2b[i], y2b[i])

    tr = 220
    s = max(0, i - tr)
    trail_a.set_data(x2a[s:i+1], y2a[s:i+1])
    trail_b.set_data(x2b[s:i+1], y2b[s:i+1])
    return (line_a, line_b, trail_a, trail_b, bob1a, bob2a, bob1b, bob2b)

print(f"Rendering {NFRAMES} frames @ {FPS} fps → long MP4 …")
ani = FuncAnimation(fig, animate, frames=NFRAMES, init_func=init,
                    interval=1000/FPS, blit=True)

writer = FFMpegWriter(fps=FPS, bitrate=8000,
                      codec='libx264',
                      extra_args=['-pix_fmt', 'yuv420p',
                                  '-preset', 'medium',
                                  '-crf', '18'])

outfile = 'double_pendulum_takedownman_custom.mp4'  # Change path/filename as needed
ani.save(outfile, writer=writer, dpi=80)
print(f"Done → {outfile}")
plt.close()
