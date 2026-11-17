---
title: Ideal gas law
summary: The ideal gas law, pV = nRT, relates the pressure, volume, amount and temperature of an ideal gas.
categories: [Physical chemistry, Gases]
aliases: [pV = nRT, PV=nRT, Ideal gas equation]
updated: 2026-11-17
infobox:
  rows:
    Equation: $pV = nRT$
    Gas constant: $R = 8.314\,462\,618\ \text{J K}^{-1}\,\text{mol}^{-1}$
    Valid when: Low pressure, high temperature
    Field: Physical chemistry
---
The **ideal gas law** is the equation of state of a hypothetical *ideal gas*. Real
gases follow it closely at low pressure and high temperature:

$$
pV = nRT
$$

Here $p$ is the pressure, $V$ the volume, $n$ the amount of gas in moles, $T$ the
thermodynamic temperature, and $R$ the **molar gas constant**.[^atkins]

## The gas constant

$R$ is the product of the Avogadro constant and the Boltzmann constant:

$$
R = N_\mathrm{A} k_\mathrm{B} = 8.314\,462\,618\ldots\ \mathrm{J\,K^{-1}\,mol^{-1}}
$$

Since the 2019 redefinition of the SI base units, both $N_\mathrm{A}$ and
$k_\mathrm{B}$ have exact defined values, so $R$ is exact as well.[^codata]

## Earlier gas laws

The ideal gas law combines three earlier empirical laws:

| Law | Held constant | Relationship |
|---|---|---|
| Boyle's law | $n$, $T$ | $pV = \text{constant}$ |
| Charles's law | $n$, $p$ | $V \propto T$ |
| Avogadro's principle | $p$, $T$ | $V \propto n$ |

For a fixed amount of gas, the **combined gas law** follows directly:

$$
\frac{p_1 V_1}{T_1} = \frac{p_2 V_2}{T_2}
$$

## Worked example

What volume does 1.00 mol of an ideal gas occupy at 298.15 K and 100 kPa?

$$
V = \frac{nRT}{p}
  = \frac{(1.00\ \text{mol})(8.314\ \text{J K}^{-1}\text{mol}^{-1})(298.15\ \text{K})}{1.00 \times 10^{5}\ \text{Pa}}
  = 2.48 \times 10^{-2}\ \text{m}^3
$$

That is 24.8 dm³, the molar volume at standard ambient temperature and pressure (SATP).

## Real gases

Real molecules attract one another and take up space, so real gases deviate from
ideal behaviour. The **van der Waals equation** corrects for both effects:

$$
\left(p + \frac{a n^2}{V^2}\right)(V - nb) = nRT
$$

The parameter $a$ accounts for attractive forces, and $b$ for the volume excluded by
the molecules themselves. The deviation is measured by the compression factor
$Z = pV_\mathrm{m}/RT$, which equals 1 for an ideal gas.

## See also

- [[Chemical equilibrium]]: $K_p$ and $K_c$ are related through the ideal gas law
- [[Kinetic theory of gases]]

[^atkins]: P. Atkins, J. de Paula and J. Keeler, *Atkins' Physical Chemistry*, 12th edn, Oxford University Press, 2022, Topic 1A.
[^codata]: NIST, *CODATA Recommended Values of the Fundamental Physical Constants*, "molar gas constant".
