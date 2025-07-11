# A collection of fascinating concepts and theories from physics and mathematics that I find intriguing and worth exploring.


import math, cmath , random

def Depressed_Cubic(p=None, q=None, *, show_explanation=True):
    """
    Print Tartaglia’s method and, if p and q are provided, return a real (or complex) root
    of the depressed cubic x³ + p x = q.

    Parameters
    ----------
    p, q : float | int
        Coefficients in the equation x³ + p x = q.
    show_explanation : bool, default True
        Whether to print the historical explanation and formula.

    Returns
    -------
    root : complex | None
        One root of the cubic (None if p or q were not supplied).
    """

    if show_explanation:
        print("""\
Title: Solving the Depressed Cubic – Tartaglia’s Breakthrough

In the 16th century Niccolò Tartaglia discovered a general solution to the
depressed cubic

    x³ + p x = q.

His substitution x = u + v leads to the relations
    u v = −p/3   and   u³ + v³ = q,
from which one obtains the closed‑form root published later in Cardano’s *Ars Magna*:

        x = ∛(q/2 + Δ) + ∛(q/2 − Δ),
    where Δ = √((q/2)² + (p/3)³).

The other two roots follow by multiplying the cube‑roots by the complex cube
roots of unity.
""")

    # If no coefficients were given, just exit after printing.
    if p is None or q is None:
        return None

    # Cardano–Tartaglia formula
    Δ = cmath.sqrt((q / 2) ** 2 + (p / 3) ** 3)
    u = (q / 2 + Δ) ** (1 / 3)
    v = (q / 2 - Δ) ** (1 / 3)
    root = u + v

    # Show the numerical result
    print(f"Root for p = {p}, q = {q} :  {root}")
    return root

def Copenhagen_quantum_theory(
        *, 
        show_explanation: bool = True,
        simulate: bool = False, 
        states=None, 
        probabilities=None
    ):
    """
    Print an overview of the Copenhagen interpretation and optionally simulate
    one projective measurement collapse.

    Parameters
    ----------
    show_explanation : bool, default True
        Whether to print the historical/theoretical summary.
    simulate : bool, default False
        If True, perform a single random measurement outcome based on
        `states` and `probabilities`.
    states : list[str] | None
        Labels of basis states |ψ_i⟩.
    probabilities : list[float] | None
        Probabilities P(i) = |c_i|² for each state. Must sum to 1.

    Returns
    -------
    outcome : str | None
        The collapsed state label if a simulation is run, else None.
    """

    if show_explanation:
        print("""\
Title: The Copenhagen Interpretation of Quantum Mechanics

Initiated chiefly by Niels Bohr and Werner Heisenberg (1920s–1930s), the Copenhagen
interpretation holds that:

• The wavefunction |ψ⟩ encodes complete statistical knowledge of a system.
• Physical properties are not definite prior to measurement; they are *potentialities*.
• Measurement causes an irreversible, non‑unitary “collapse” of |ψ⟩ onto an eigenstate.
• Complementarity: mutually exclusive experimental arrangements reveal
  complementary aspects (e.g., particle vs. wave).
• Probabilities follow the Born rule: P(i) = |⟨ψ_i|ψ⟩|².
• Classical measuring devices are described by classical physics; quantum/classical
  cut is contextual but necessary.

Critics have objected to the vagueness of “collapse” and the role of the observer,
but Copenhagen remains one of the most widely taught viewpoints.
""")

    if simulate:
        if states is None or probabilities is None:
            raise ValueError("Provide both `states` and `probabilities` for simulation.")
        if abs(sum(probabilities) - 1.0) > 1e-8:
            raise ValueError("Probabilities must sum to 1.")
        outcome = random.choices(states, weights=probabilities, k=1)[0]
        print(f"Measurement result → collapsed to state: {outcome}")
        return outcome

    return None