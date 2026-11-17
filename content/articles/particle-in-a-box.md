---
title: Particle in a box
summary: The particle in a box is the simplest quantum-mechanical model with quantised energy levels, used in chemistry to model π electrons in conjugated molecules.
categories: [Physical chemistry, Quantum chemistry]
aliases: [Infinite square well]
updated: 2026-11-14
infobox:
  rows:
    Energy levels: $E_n = \dfrac{n^2 h^2}{8 m L^2}$
    Quantum number: $n = 1, 2, 3, \ldots$
    Zero-point energy: $\dfrac{h^2}{8mL^2}$
    Field: Quantum chemistry
---
The **particle in a box** (or *infinite square well*) describes a particle of mass $m$
that can move freely between two impenetrable walls a distance $L$ apart. It is the
simplest system that shows **quantisation** of energy.

## Solving the Schrödinger equation

Inside the box the potential energy is zero, so the time-independent Schrödinger
equation is

$$
-\frac{\hbar^2}{2m}\frac{\mathrm{d}^2\psi}{\mathrm{d}x^2} = E\psi, \qquad 0 < x < L
$$

The boundary conditions are $\psi(0) = \psi(L) = 0$. The normalised solutions are

$$
\psi_n(x) = \sqrt{\frac{2}{L}}\,\sin\!\left(\frac{n\pi x}{L}\right), \qquad n = 1, 2, 3, \ldots
$$

with energies

$$
E_n = \frac{n^2 h^2}{8 m L^2}
$$

### Key features

- The energy cannot be zero. The lowest level, $E_1$, is the **zero-point energy**.
- The gaps between levels grow with $n$: $E_{n+1} - E_n = (2n+1)\,h^2/8mL^2$.
- The gaps shrink as $L$ or $m$ increases, which is why quantisation is not noticed
  for large objects.
- $\psi_n$ has $n - 1$ **nodes** inside the box.

## Application: conjugated molecules

In the **free-electron model**, the π electrons of a linear conjugated molecule are
treated as particles in a box as long as the conjugated chain. With $N$ π electrons
filling levels in pairs, the highest occupied level is $n = N/2$. The lowest-energy
absorption is then

$$
\Delta E = E_{N/2+1} - E_{N/2} = \frac{(N+1)\,h^2}{8 m_\mathrm{e} L^2},
\qquad
\lambda = \frac{hc}{\Delta E} = \frac{8 m_\mathrm{e} c L^2}{h\,(N+1)}
$$

So longer conjugated chains absorb at longer wavelengths. This explains why highly
conjugated molecules such as β-carotene are coloured. Ring systems like
[[benzene]] are better described by [[Hückel theory]].

## See also

- [[Schrödinger equation]]
- [[Quantum harmonic oscillator]]
