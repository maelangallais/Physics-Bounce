# 🎱 Physics-Bounce

A series of physics and ray-bouncing simulations built for the **NumWorks** calculator in MicroPython, progressing from basic directional rays to parallel screen-edge bouncing, gravity physics, and arbitrary surface-angle reflection.

---

## 📂 Scripts Included

```
Physics-Bounce/
├── surface_bounce.py             # Ray bouncing against arbitrary drawn surfaces (v3)
├── gravity_bounce.py             # Gravity & energy-loss ball physics simulation
├── screen_bounce_v2_parallel.py  # Multi-ray parallel bouncing simulation (v2)
├── screen_bounce_v1.py           # Infinite single-ray screen-edge bounce (v1)
└── ray_base.py                   # Foundational ray-drawing experiment
```

---

### 1. `surface_bounce.py` *(Created October 22, 2026)*
- Simulates a ray bouncing off **arbitrary surfaces** by detecting collision pixels and estimating the surface impact angle/normal.
- **Known Limitations**: Computing reliable surface normals on a low-resolution pixel grid is tricky; this script may still contain edge-case bugs or occasional inconsistent bounce angles.

### 2. `gravity_bounce.py` *(Created May 14, 2024)*
- Interactive ball physics simulation where you configure initial velocity, gravity, mass, starting coordinates, radius, and launch angle.
- **Scale Note (`1 pixel = 1 meter`)**: Because the coordinate system maps **1 pixel to 1 meter**, the `320 × 222` screen represents a massive 320m × 222m arena. As a result, movement and falling speeds appear relatively slow due to this oversized physical scale.

### 3. `screen_bounce_v2_parallel.py` *(Created December 23, 2023)*
- Steps rays pixel-by-pixel without recomputing direction vectors each frame, allowing multiple simultaneous rays to bounce in parallel.

### 4. `screen_bounce_v1.py` *(Created December 23, 2023)*
- Infinite reflection simulation of a single ray bouncing off the four screen boundaries.

### 5. `ray_base.py` *(Created December 20, 2023)*
- The foundational experiment behind all the bounce scripts: draws directional rays of a given length from a starting point and angle.

---

## 🖥️ Requirements & Platform

- MicroPython for **NumWorks** calculators (`kandinsky`, `math`, `random`, `time`).
