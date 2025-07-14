# A collection of fascinating concepts and theories from physics and mathematics that I find intriguing and worth exploring.
        # Mentions: Most of these concepts were inspired by videos from Veritasium, 3Blue1Brown, and Real Engineering.


import math, cmath , random, itertools, time

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

def P_vs_NP(
        *, 
        show_explanation: bool = True,
        demo: bool = False,
        instance=None,
        certificate=None
    ):
    """
    Print an overview of the P vs NP problem and optionally demonstrate that
    verifying a certificate is fast even if finding it may be slow.

    Parameters
    ----------
    show_explanation : bool
        Print the historical/theoretical summary.
    demo : bool
        If True, run a tiny Subset‑Sum search + verification.
    instance : tuple[list[int], int] | None
        A pair (numbers, target) for the demo search.
    certificate : list[int] | None
        A purported solution subset; will be verified in O(n).

    Returns
    -------
    verified : bool | None
        Whether the certificate is valid (if demo and certificate supplied).
    """

    if show_explanation:
        print("""\
Title: The P vs NP Problem – A Million Dollar Mystery

One of the most famous unsolved problems in computer science and mathematics:

    Is P = NP?

Where:
• P  = problems solvable quickly (in polynomial time)
• NP = problems where solutions can be verified quickly

Key idea: If you can quickly *check* a solution, can you also *find* one quickly?

• NP-complete problems (e.g., SAT, Subset-Sum, Traveling Salesman) are the hardest in NP.
• A polynomial-time solution to any NP-complete problem implies P = NP.

This problem was formally posed by Stephen Cook in 1971 and remains unsolved.
It is one of the seven Millennium Prize Problems—solving it earns you **$1,000,000** from the Clay Mathematics Institute.

So far, no one knows the answer.
""")

    if not demo:
        return None
    
    # Default demo instance if none given
    if instance is None:
        instance = ([3, 34, 4, 12, 5, 2], 9)   # classic small subset‑sum
    numbers, target = instance

    print(f"\nDemo — Subset‑Sum instance: numbers = {numbers}, target = {target}")

    # Brute‑force search (exponential)
    start = time.perf_counter()
    solution = None
    for r in range(len(numbers) + 1):
        for subset in itertools.combinations(numbers, r):
            if sum(subset) == target:
                solution = list(subset)
                break
        if solution is not None:
            break
    brute_time = (time.perf_counter() - start) * 1e3  # ms
    print(f"Brute‑force search found subset {solution} in {brute_time:.2f} ms")

    # Verification step (polynomial)
    if certificate is None:
        certificate = solution
        print("Using the found subset as certificate.")
    is_valid = sum(certificate) == target and all(x in numbers for x in certificate)
    print(f"Certificate {certificate} verification → {is_valid}")

    return is_valid

def goldbach_conjecture(*, show_explanation=True, demo=False, n=None):
    """
    Print an overview of Goldbach's Conjectures and optionally demonstrate the conjecture for a given number.

    Parameters
    ----------
    show_explanation : bool, default True
        Whether to print the historical/theoretical summary.
    demo : bool, default False
        If True, check the conjecture for the given number n.
    n : int | None
        An even number > 2 (for strong) or odd number > 5 (for weak), to verify the conjecture.

    Returns
    -------
    result : list[tuple[int, int]] or list[tuple[int, int, int]] | None
        A list of prime pairs or triplets satisfying the conjecture, or None if demo=False.
    """

    if show_explanation:
        print("""\
Title: Goldbach’s Conjectures – A Timeless Enigma in Number Theory

Proposed in 1742 by Christian Goldbach in correspondence with Euler, the conjectures are:

• **Strong Goldbach Conjecture**: Every even integer greater than 2 is the sum of two prime numbers.
    → Example: 28 = 11 + 17

• **Weak Goldbach Conjecture**: Every odd integer greater than 5 is the sum of three primes.
    → Example: 29 = 7 + 11 + 11

Euler considered the strong version a special case of the weak one.
Though tested up to very large numbers, both remain unproven in general.

• The weak conjecture was **proven in 2013** by Harald Helfgott.
• The strong conjecture is still **open** — but no counterexample has ever been found.
""")

    if not demo or n is None:
        return None

    def is_prime(k):
        if k < 2:
            return False
        for i in range(2, int(k ** 0.5) + 1):
            if k % i == 0:
                return False
        return True

    results = []

    if n % 2 == 0:
        # Strong Goldbach demo (even number > 2)
        for a in range(2, n // 2 + 1):
            b = n - a
            if is_prime(a) and is_prime(b):
                results.append((a, b))
        print(f"Strong Goldbach pairs for {n}: {results}")
    else:
        # Weak Goldbach demo (odd number > 5)
        for a in range(2, n - 4):
            if not is_prime(a): continue
            for b in range(a, n - a - 1):
                c = n - a - b
                if c >= b and is_prime(b) and is_prime(c):
                    results.append((a, b, c))
                        
        print(f"Weak Goldbach triplets for {n}: {results}")

    return results if results else None

def Principle_of_Least_Action(*, show_explanation=True):
    """
    Print a full explanation of the Principle of Least Action,
    including its historical development, derivative, and classical interpretation.
    """

    if show_explanation:
        print("""\
Title: The Principle of Least Action – A Unifying Law of Motion

Nature, in all its complexity, seems to follow a very simple rule:
    "Of all possible paths a system could take, the one actually taken is the one
     that makes the action stationary (usually minimal)."

–––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
1. The Action Integral and Lagrangian Mechanics
–––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––

The **action** S is defined as:

        S = ∫ L dt        (from t₁ to t₂)

where L is the **Lagrangian**:

        L = T - V

        • T: kinetic energy
        • V: potential energy

This formulation, developed by **Euler** and **Lagrange**, leads to:

    ◾ Euler–Lagrange Equation:

        d/dt (∂L/∂𝑞̇) − ∂L/∂q = 0

This differential equation is the **variational derivative** of the action.
It’s equivalent to **Newton’s Second Law**, but more general and powerful.

▶ Example:
    A particle of mass m in a potential V(q):

        L = (1/2)m𝑞̇² − V(q)

    Applying the Euler–Lagrange equation:

        d/dt (m𝑞̇) = −dV/dq   ⟶   m𝑞̈ = −∇V

This recovers Newton’s familiar form: **F = ma**.

–––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
2. Maupertuis' Principle – The Older Formulation
–––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––

Pierre-Louis **Maupertuis** proposed an earlier version (c. 1744), sometimes called:

    “The Principle of Least Path” or “Least Action in the kinetic form”

He defined action as:

        S = ∫ p · ds  = ∫ m·v · ds

    ◾ Here:
        • p is momentum (mv)
        • ds is an infinitesimal segment of the path
        • This applies to conservative systems where energy is constant

▶ In scalar form (for 1D or arc length ds):

        S = ∫ m·v·ds

This approach focuses on the geometry of the path, rather than time evolution.

–––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
3. Comparison & Derivatives
–––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––

Both formulations lead to the **same equations of motion**:

    ▸ Lagrangian mechanics uses time as the key variable:
        δS = 0 → Euler–Lagrange differential equation (time-dependent)

    ▸ Maupertuis' approach is energy-conserving and “geometrical”:
        It focuses on space paths with fixed total energy.

▶ Derivative of the Lagrangian action gives:
    
        δS = 0  ⇨  d/dt (∂L/∂𝑞̇) − ∂L/∂q = 0

This is a **functional derivative** — it finds functions (paths q(t)) that make
the integral minimal, not just numbers.

–––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
4. Why It’s Deep
–––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––

✓ It unifies **Newtonian mechanics**, **Hamiltonian mechanics**, **quantum mechanics** (Feynman path integrals), and **general relativity**.

✓ It allows reformulating physical laws in terms of optimization.

✓ It’s the foundation for modern theoretical physics.

In short: **Nature acts economically.** Forces aren’t “causing” motion — instead,
the actual trajectory is the one that balances all trade-offs in the action.

As Feynman said:
> “Nature doesn’t sit there and calculate what force to apply. Instead, every path is tried, and the one with stationary action is the one we see.”
""")
