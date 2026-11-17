---
title: Chemical equilibrium
summary: Chemical equilibrium is the state in which the forward and reverse rates of a reversible reaction are equal, so concentrations no longer change.
categories: [Physical chemistry]
aliases: [Equilibrium constant, Le Chatelier's principle]
updated: 2026-11-16
---
**Chemical equilibrium** is the state of a reversible reaction in which the forward
and reverse reactions happen at the same rate. The composition of the mixture then
stops changing. The equilibrium is *dynamic*: both reactions keep going.

## Equilibrium constant

For a general reaction

$$
\ce{aA + bB <=> cC + dD}
$$

the equilibrium constant in terms of concentrations is

$$
K_c = \frac{[\mathrm{C}]^c\,[\mathrm{D}]^d}{[\mathrm{A}]^a\,[\mathrm{B}]^b}
$$

For gases, partial pressures give $K_p$. Using the [[Ideal gas law]], the two are
related by

$$
K_p = K_c\,(RT)^{\Delta n}
$$

where $\Delta n$ is the change in the number of moles of gas, $(c + d) - (a + b)$.

## Thermodynamics

The standard Gibbs energy of reaction determines the equilibrium constant:[^atkins]

$$
\Delta_r G^\circ = -RT \ln K
$$

If $\Delta_r G^\circ < 0$, then $K > 1$ and products are favoured at equilibrium.
The temperature dependence of $K$ is given by the **van 't Hoff equation**:

$$
\frac{\mathrm{d}\ln K}{\mathrm{d}T} = \frac{\Delta_r H^\circ}{RT^2}
$$

## Le Chatelier's principle

When a system at equilibrium is disturbed, the equilibrium shifts to partly oppose
the change. In the Haber process,

$$
\ce{N2(g) + 3H2(g) <=> 2NH3(g)} \qquad \Delta_r H^\circ = -92\ \text{kJ mol}^{-1}
$$

- **Higher pressure** shifts the equilibrium to the right (4 mol of gas → 2 mol of gas).
- **Higher temperature** shifts it to the left, because the forward reaction is exothermic.
- **Removing** $\ce{NH3}$ shifts it to the right.

Only a change of temperature changes the value of $K$. A catalyst changes only how
fast equilibrium is reached (see [[Arrhenius equation]]).

[^atkins]: P. Atkins, J. de Paula and J. Keeler, *Atkins' Physical Chemistry*, 12th edn, Oxford University Press, 2022, Topic 6A.
