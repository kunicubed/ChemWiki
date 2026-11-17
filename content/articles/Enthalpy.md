---
title: Enthalpy
summary: Enthalpy is the sum of a thermodynamic system's internal energy and the product of its pressure and volume. It encompasses all forms of the system's energy.
categories: [Physical Chemistry, Thermodynamics]
updated: 2026-11-17
---

**Enthalpy** is defined as the sum of the internal energy and the product of pressure and volume of a thermodynamic system. The internal energy is a measure of the energy of a thermodynamic system usually in the abscence of effects from external fields and excludes kinetic energy, while the PV term describes the pressure-volume work being done in the system. It is important, when considering enthalpy, to consider what **energy actually is**. Energy is the capacity of a system to do work, therefore enthalpy is a measure of all the different ways a system can and does do work.

$$
H = U + PV
$$

The unit of measurement for enthalpy according to International system of units is the Joule. 

Enthalpy is an extensive property, which means that it is proportional to the size of a system. Therefore, enthalpy of a system made of multiple systems can also be expressed as a sum of the enthalpies of the individual systems. At a constant pressure with no additional work,

## Theory

The idea of enthalpy is largely governed by this equation

$$
dH = dq, \qquad \Delta H = q_p
$$
Proof:

Consider $H + dH = (U+dU) + (p + dp)(V + dV) = U + dU + pV + pdV + Vdp + dpdV$ where the last term can be ignored as it is the product of two infinitessimaly small terms. Therefore, if we make the change U + pV = H we obtain

$$
H + dH = H + dU + pdV + Vdp
$$


$$
dH = dU + pdV + Vdp
$$

$dU = dw + dq$ - the change in internal energy is equal to the change in work plus the change in heat energy. Therefore, if we substitute in dU 

$$
dH = dw + dq + pdV + Vdp    
$$

Pressure volume work can be expressed as the loss of energy due to the pressure volume work done on the surroundings, which is equal to $-pdV$

Therefore, $dH = dq + Vdp$ which at constant p $dH = dq$

At a constant pressure, consider the relationship between increase in enthalpy and increase in temperature. The slope of a tangent to an enthalpy-temperature plot is called a *heat capacity at constant temperature* and can be mathematically expressed as:

$$
C_p = \frac{\partial H}{\partial T}_p
$$

The heat capacity is an extensive property: this is simple to understand if you imagine if the system doubles in mass, then there is double the amount of stuff that can gain energy, therefore increasing the heat capacity by double. The heat capacity can relate enthalpy change to a change in temperature, $dH = C_p dT$. The molar heat capactity $C_{p,m}$ is the heat capacity per mole of material, which is an intensive property (since if you double the mass, you still have the same heat capacity per mole.) Because heat capacity varies with temperature, a quadratic expression for the heat capacity per mole can be expressed as:

$$
C_{p,m} = a + bT + \frac{c}{T^2}
$$

These polynomials are computed by fitting a curve in that form to real experimental heat capacity with respect to temperature. The coefficients here can be looked up in data booklets.

Different enthalpy changes correspond to different types of reaction. 

Enthalpy of reaction is the enthalpy change when one mole of substance reacts completely. 
Enthalpy of formation ($\Delta H_f$) is the enthalpy change when one mole of a compound is formed from its elements 
Enthalpy of combustion is the enthalpy change when one mole of substance burns completely in oxygen

## Practical elements

Enthalpy cannot be simply measured, since its very hard to get enough information about a system to definitively know how much internal energy there is and the PV work done. Therefore, we can only consider the enthalpy change, $\Delta H$. A **calorimeter** can study the temperature change that accompanies a physical or chemical change occuring at constant pressure. A calorimeter for studying processes at constant pressure is called an *isobaric calorimeter*, while for a combustion reaction an *adiabatic flame calorimeter* may be used. Newer, more modern technologies such as the *differential scanning calorimeter* may also be used. 

## Applications

