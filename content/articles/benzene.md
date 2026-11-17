---
title: Benzene
summary: Benzene, C₆H₆, is the simplest aromatic hydrocarbon — a flat ring of six carbon atoms whose π electrons are delocalised around the whole ring.
categories: [Organic chemistry, Aromatic compounds]
aliases: [C6H6]
updated: 2026-11-17
infobox:
  image: /media/benzene.svg
  caption: Kekulé structure of benzene
  rows:
    Identifiers:
    CAS number: 71-43-2
    Properties:
    Chemical formula: $\ce{C6H6}$
    Molar mass: 78.11 g mol$^{-1}$
    Appearance: Colourless liquid
    Density: 0.8765 g cm$^{-3}$ (20 °C)
    Melting point: 5.5 °C
    Boiling point: 80.1 °C
    C–C bond length: 139 pm
---
**Benzene** is an organic compound with the formula $\ce{C6H6}$. Its molecule is a
planar ring of six carbon atoms, each bonded to one hydrogen atom. Benzene is the
parent compound of the **aromatic** hydrocarbons, and its unusual stability is
explained by the delocalisation of six π electrons around the ring.[^clayden]

Benzene was first isolated by Michael Faraday in 1825. Its ring structure was
proposed by August Kekulé in 1865.

## Structure

All six C–C bonds in benzene are the same length, 139 pm. This is between a typical
C–C single bond (154 pm) and a C=C double bond (134 pm). So benzene cannot be a
simple alternation of single and double bonds. The two Kekulé structures are
**resonance contributors**, and the real molecule is a hybrid of them, with a bond
order of 1.5 for every C–C bond.

### Molecular orbital description

Each carbon is $sp^2$ hybridised. The six unhybridised $2p_z$ orbitals combine to
give six π molecular orbitals. In [[Hückel theory]] their energies are

$$
E_k = \alpha + 2\beta \cos\!\left(\frac{2\pi k}{6}\right), \qquad k = 0, \pm 1, \pm 2, 3
$$

where $\alpha$ is the Coulomb integral and $\beta < 0$ is the resonance integral.
The six π electrons fill the three bonding orbitals, giving a total π energy of
$6\alpha + 8\beta$. Three isolated double bonds would give $6\alpha + 6\beta$, so
the **delocalisation energy** is $2\beta$.

Benzene fits **Hückel's rule**: a planar, cyclic, fully conjugated ring is aromatic
if it has $4n + 2$ π electrons, here with $n = 1$.

## Thermochemical evidence for stability

Hydrogenating cyclohexene releases about 120 kJ mol$^{-1}$:

$$
\ce{C6H10 + H2 -> C6H12} \qquad \Delta_r H^\circ \approx -120\ \text{kJ mol}^{-1}
$$

A hypothetical "cyclohexatriene" with three isolated double bonds should therefore
release about $3 \times 120 = 360$ kJ mol$^{-1}$. Benzene actually releases only
about 208 kJ mol$^{-1}$:

$$
\ce{C6H6 + 3H2 ->[\text{Ni}] C6H12} \qquad \Delta_r H^\circ \approx -208\ \text{kJ mol}^{-1}
$$

The difference, about 150 kJ mol$^{-1}$, is the **aromatic stabilisation energy**.

## Reactions

Because addition would destroy the aromatic π system, benzene usually undergoes
**electrophilic aromatic substitution** instead of addition:

| Reaction | Reagents | Product |
|---|---|---|
| Nitration | $\ce{HNO3}$, $\ce{H2SO4}$ | Nitrobenzene, $\ce{C6H5NO2}$ |
| Bromination | $\ce{Br2}$, $\ce{FeBr3}$ | Bromobenzene, $\ce{C6H5Br}$ |
| Friedel–Crafts alkylation | $\ce{RCl}$, $\ce{AlCl3}$ | Alkylbenzene, $\ce{C6H5R}$ |
| Sulfonation | fuming $\ce{H2SO4}$ | Benzenesulfonic acid |

For example, the overall equation for nitration is

$$
\ce{C6H6 + HNO3 ->[\ce{H2SO4}] C6H5NO2 + H2O}
$$

The electrophile is the nitronium ion, $\ce{NO2+}$, formed by
$\ce{HNO3 + 2H2SO4 <=> NO2+ + H3O+ + 2HSO4-}$.

## Safety

!!! warning "Toxicity"
    Benzene is a known human carcinogen. In teaching laboratories it is normally
    replaced by less toxic solvents such as methylbenzene ([[Toluene]]).

## See also

[^clayden]: J. Clayden, N. Greeves and S. Warren, *Organic Chemistry*, 2nd edn, Oxford University Press, 2012, ch. 7.
