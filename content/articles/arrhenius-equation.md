---
title: Arrhenius equation
summary: The Arrhenius equation, k = A exp(−Ea/RT), describes how the rate constant of a reaction depends on temperature.
categories: [Physical chemistry, Chemical kinetics]
aliases: [Activation energy]
updated: 2026-11-15
infobox:
  rows:
    Equation: $k = A\,e^{-E_\mathrm{a}/RT}$
    Proposed by: Svante Arrhenius (1889)
    Field: Chemical kinetics
---
The **Arrhenius equation** relates the rate constant $k$ of a chemical reaction to
the absolute temperature $T$:

$$
k = A \exp\!\left(-\frac{E_\mathrm{a}}{RT}\right)
$$

$A$ is the **pre-exponential factor** (or frequency factor), $E_\mathrm{a}$ is the
**activation energy**, and $R$ is the gas constant (see [[Ideal gas law]]).

## Interpretation

The factor $e^{-E_\mathrm{a}/RT}$ is the fraction of collisions with enough energy to
react, which comes from the Boltzmann distribution. $A$ reflects how often molecules
collide and whether they are correctly oriented. A higher activation energy means
the rate is *more sensitive* to temperature.

## Linear form

Taking natural logarithms gives a straight-line equation:

$$
\ln k = \ln A - \frac{E_\mathrm{a}}{R}\cdot\frac{1}{T}
$$

An **Arrhenius plot** of $\ln k$ against $1/T$ has gradient $-E_\mathrm{a}/R$ and
intercept $\ln A$.

## Two-temperature form

If rate constants $k_1$ and $k_2$ are measured at temperatures $T_1$ and $T_2$:

$$
\ln\frac{k_2}{k_1} = -\frac{E_\mathrm{a}}{R}\left(\frac{1}{T_2} - \frac{1}{T_1}\right)
$$

### Example

A reaction's rate constant doubles between 298 K and 308 K. Its activation energy is

$$
E_\mathrm{a} = \frac{R \ln 2}{\dfrac{1}{298\ \text{K}} - \dfrac{1}{308\ \text{K}}}
\approx \frac{(8.314)(0.693)}{1.09 \times 10^{-4}}\ \text{J mol}^{-1}
\approx 53\ \text{kJ mol}^{-1}
$$

This is the origin of the rule of thumb that "rates double for every 10 °C rise".

## Catalysis

A catalyst provides an alternative reaction pathway with a lower $E_\mathrm{a}$. For
example, iron catalyses the Haber process:

$$
\ce{N2(g) + 3H2(g) <=>[\ce{Fe}] 2NH3(g)}
$$

A catalyst does **not** change the position of [[Chemical equilibrium|equilibrium]].
It speeds up the forward and reverse reactions by the same factor.

## See also

- [[Transition state theory]] and the Eyring equation
