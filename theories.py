# A collection of fascinating concepts and theories from physics and mathematics that I find intriguing and worth exploring.
        # Mentions: Most of these concepts were inspired by videos from Veritasium, 3Blue1Brown, and Real Engineering.


import math, cmath , random, itertools, time
from scipy.stats import norm

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

def einstein_equivalence_principle(show_explanation=True):
    """
    Provides a detailed overview of Einstein's Equivalence Principle, including its conceptual framework,
    historical development, and implications for general relativity.

    Parameters
    ----------
    show_explanation : bool
        Whether to print the theoretical and historical explanation.
    """
    if show_explanation:
        print("""\
Title: Einstein’s Equivalence Principle — The Geometrization of Gravity

## Historical Background

The Equivalence Principle has its roots in Galileo’s 17th-century observation that all objects fall at the same rate in a vacuum, regardless of their mass. Newton’s law of gravitation preserved this principle by assuming that the **gravitational mass** (how strongly gravity pulls on an object) and the **inertial mass** (how much an object resists acceleration) are equal — an unexplained coincidence in classical mechanics.

In 1907, while working in a Swiss patent office, **Albert Einstein** had what he later called "the happiest thought of my life":  
> *A person in free fall does not feel their own weight.*

From this thought experiment, Einstein formulated a revolutionary idea: **locally**, the effects of gravity are indistinguishable from those of acceleration.

---

## Types of Equivalence Principles

### 1. Weak Equivalence Principle (WEP)
> The trajectory of a freely falling test particle is independent of its internal structure or composition.

This principle has been tested to extreme precision (better than 1 part in 10¹⁵) in modern torsion balance and lunar laser ranging experiments.

### 2. Einstein Equivalence Principle (EEP)
> All local, non-gravitational experiments in a freely falling frame yield results independent of the velocity and location of the frame.

It includes:
- **WEP**
- **Local Lorentz Invariance (LLI)** — Laws of physics do not depend on the velocity of the frame.
- **Local Position Invariance (LPI)** — Laws of physics do not depend on where or when the experiment is done.

### 3. Strong Equivalence Principle (SEP)
> Extends EEP to include gravitational experiments and self-gravitating bodies.

Only general relativity fully satisfies SEP; most alternative gravity theories violate it.

---

## Einstein’s Elevator Thought Experiment

Imagine you're in a sealed elevator:

- **Case 1:** The elevator is in deep space, far from any mass, accelerating upward at 9.8 m/s².
- **Case 2:** The elevator is stationary on Earth's surface.

Inside, there's no way to tell which situation you're in without looking outside. You feel a downward "force" in both cases. A beam of light, aimed horizontally across the elevator, appears to bend downward in both.

**Conclusion:** Locally, gravity is equivalent to acceleration.

---

## Mathematical Implication

This insight leads to the conclusion that **gravity is not a force**, but a manifestation of spacetime curvature. Mathematically, in general relativity:

- Objects move along **geodesics**, the straightest possible paths in curved spacetime.
- The gravitational field is described by the **metric tensor** \( g_{\mu\nu} \), which determines distances and time intervals.
- The curvature is encoded in the **Riemann curvature tensor**, and how matter curves spacetime is governed by **Einstein’s field equations**:

\[
R_{\mu\nu} - \frac{1}{2} g_{\mu\nu} R = \frac{8\pi G}{c^4} T_{\mu\nu}
\]

---

## Physical Predictions from the Equivalence Principle

- **Gravitational time dilation**: Clocks tick slower in stronger gravitational fields (verified by GPS and gravitational redshift experiments).
- **Gravitational redshift**: Light climbing out of a gravitational well loses energy (becomes redder).
- **Light deflection by gravity**: Light bends around massive objects (confirmed by Eddington's 1919 solar eclipse expedition).
- **Perihelion precession of Mercury**: Explained precisely by general relativity.

---

## Summary

Einstein’s Equivalence Principle marks the shift from Newtonian gravity to the geometric framework of **general relativity**. It teaches us that **freely falling frames are the truest form of inertial frames** in a curved universe. Gravity, in Einstein’s view, is not a force but the shape of spacetime itself.

This principle is one of the deepest and most beautiful insights in all of physics.
""")

def prisoners_dilemma(show_explanation=True, show_table=True):
    """
    Print a detailed explanation of the Prisoner’s Dilemma, including the game setup,
    payoff matrix, and strategic implications in game theory.

    Parameters
    ----------
    show_explanation : bool, default True
        Whether to print the background and theoretical explanation.
    show_table : bool, default True
        Whether to print the payoff matrix of the game.
    """
    
    if show_explanation:
        print("""\
Title: The Prisoner’s Dilemma – A Game Theory Classic

The Prisoner's Dilemma is a foundational problem in game theory that illustrates how 
individual rational choices can lead to a collectively suboptimal outcome.

--- Setup ---

Two individuals, Alice and Bob, are arrested for a serious crime. Prosecutors separate them 
and offer each the same deal:

• If one testifies (defects) and the other remains silent (cooperates), the defector goes free,
  and the cooperator gets 5 years in prison.

• If both testify (defect), both receive 3 years in prison.

• If both remain silent (cooperate), both serve only 1 year due to lack of evidence.

Each prisoner must choose without knowing what the other will do. The dilemma lies in the fact
that no matter what the other does, betrayal offers a better personal outcome.

--- Core Insight ---

• Mutual cooperation yields a better outcome than mutual defection.
• Yet, rational self-interest pushes both to defect.
• Hence, mutual defection is a **Nash Equilibrium** — a stable state where no one can benefit 
  from changing their decision alone.

This contradiction between collective benefit and individual rationality makes the dilemma a 
central theme in understanding real-world issues like trust, competition, and strategy.

""")
    
    if show_table:
        print("""\
--- Payoff Matrix ---

        | Bob Cooperates | Bob Defects
------------------------------------------
Alice Cooperates | (−1, −1)       | (−5,  0)
Alice Defects    | ( 0, −5)       | (−3, −3)

Each pair (A, B) = (Years for Alice, Years for Bob)
""")

        print("""\
--- Implications and Applications ---

• **Arms Races:** Countries build weapons even though disarmament would benefit all.
• **Climate Change:** Nations hesitate to reduce emissions unless others do the same.
• **Cartel Pricing:** Firms may lower prices to gain market share, even when collusion yields more profit.
• **Evolutionary Biology:** Cooperation and altruism in species can be studied using repeated dilemmas.

--- Iterated Prisoner’s Dilemma ---

When the game is played repeatedly, strategies like **Tit for Tat** (cooperate first, then copy the opponent) can
emerge, rewarding cooperation and punishing betrayal — encouraging trust over time.

--- Theoretical Notes ---

• **Nash Equilibrium:** Mutual defection is stable; no unilateral change improves outcome.
• **Pareto Inefficient:** Mutual cooperation is better for both, yet unstable without trust.
• **Zero-Sum Misconception:** The dilemma is not zero-sum — both players can win or lose together.

This game beautifully models the tension between short-term incentives and long-term cooperation.
""")
            
def noethers_theorem(show_explanation=True):
    """
    Print an explanation of Noether’s Theorem and its profound connection
    between symmetries and conserved quantities in physics.

    Parameters
    ----------
    show_explanation : bool, default True
        Whether to print the theoretical background and significance.
    """
    if show_explanation:
        print("""\
Title: Noether’s Theorem — The Deep Link Between Symmetry and Conservation

Developed by Emmy Noether in 1915 and published in 1918, Noether’s Theorem is one of the most profound results in theoretical physics and mathematics.

--- Core Idea ---

**Every differentiable symmetry of the action of a physical system corresponds to a conservation law.**

In simpler terms:
- If a system’s laws don’t change under a continuous transformation (a symmetry),
- Then something measurable remains **conserved**.

--- Examples of Symmetry ↔ Conservation ---

1. **Time Translation Symmetry**  
   → Laws don’t change over time  
   → ⟹ **Energy is conserved**

2. **Spatial Translation Symmetry**  
   → Laws don’t depend on location in space  
   → ⟹ **Linear momentum is conserved**

3. **Rotational Symmetry**  
   → Laws remain unchanged under spatial rotation  
   → ⟹ **Angular momentum is conserved**

--- The Mathematics (Simplified) ---

In Lagrangian mechanics, the *action* \( S \) is the integral over time of the Lagrangian \( L = T - V \) (kinetic - potential energy):

\[S = \int L(q, \dot{q}, t)\, dt\]

Noether showed that if the action \( S \) is invariant under a continuous transformation of the coordinates \( q(t) \), then there exists a conserved quantity \( Q \) along the solutions of the Euler–Lagrange equations.

This deep connection is central to all of modern theoretical physics — classical mechanics, quantum mechanics, general relativity, and quantum field theory.

--- Legacy and Importance ---

• Noether’s Theorem is considered a cornerstone of **modern physics**.
• It provides a **mathematical foundation** for why conservation laws hold.
• It bridges **symmetry (geometry)** with **dynamics (physics)**.
• It is essential in **Lagrangian** and **Hamiltonian** formulations.

Albert Einstein himself called Emmy Noether a **mathematical genius** and praised the theorem’s beauty and power.

""")

def double_slit_experiment(*, show_explanation=True, simulate=False):
    """
    Explain the double-slit experiment and the effect of observation on interference patterns.
    
    Parameters
    ----------
    show_explanation : bool, default True
        Whether to print the historical and theoretical explanation.
    simulate : bool, default False
        If True, simulate simplified outcomes with and without measurement.
    
    Returns
    -------
    pattern : str | None
        A string description of the observed pattern if simulate=True, else None.
    """
    if show_explanation:
        print("""\
Title: The Double-Slit Experiment — Observation Alters Reality

The double-slit experiment, first performed by Thomas Young in 1801 with light and later repeated with electrons, 
is a cornerstone of quantum mechanics.

––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
1. Setup
––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
• A particle source emits electrons (or photons) one at a time.
• A barrier with two narrow slits lets the particles pass through.
• A detection screen records where each particle lands.

––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
2. Without Observation
––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
• No detectors are placed at the slits.
• The particles behave like waves, passing through **both slits simultaneously**.
• Result: An **interference pattern** builds up on the screen — even with single particles.

––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
3. With Observation (Measurement)
––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
• Detectors are placed at the slits to observe which path the particle takes.
• The wavefunction collapses — each particle is forced to choose a definite path.
• Result: The interference pattern **disappears**, and two classical bands appear.

––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
4. Interpretation
––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
• Observation **changes the outcome** — not passively, but fundamentally.
• The act of measurement collapses the wavefunction into a definite state.
• This illustrates the **quantum measurement problem** and challenges classical intuition.

As Feynman said:
> "This is the only mystery of quantum mechanics."

""")

    if simulate:
        observed = random.choice([True, False])
        if observed:
            pattern = "Two distinct bands — classical particle behavior due to wavefunction collapse."
        else:
            pattern = "Interference pattern — wave-like superposition across both slits."
        print(f"Simulated outcome (observation={'Yes' if observed else 'No'}): {pattern}")
        return pattern

    return None

def axiom_of_choice(*, show_explanation=True, show_paradox=True):
    """
    Explain the Axiom of Choice and its philosophical and mathematical consequences,
    including the Banach–Tarski paradox.

    Parameters
    ----------
    show_explanation : bool, default True
        Whether to print the full explanation and implications.
    show_paradox : bool, default True
        Whether to include the Banach–Tarski paradox as an illustration.

    Returns
    -------
    result : str | None
        A summary of the paradox if shown, else None.
    """
    if show_explanation:
        print("""\
Title: The Axiom of Choice — Choosing Without a Rule

Imagine an infinite number of non-empty boxes, each with at least one object inside. 
You’re asked to pick one object from each box. But there’s a catch — no rule or pattern is given. 
The Axiom of Choice says you can still make those selections, even if there’s no way to describe how.

––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
1. Formal Statement
––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
The axiom states:

> For any collection of non-empty sets, there exists a function that selects exactly 
> one element from each set — even if the collection is infinite and unstructured.

It’s not about how to choose, just that a complete set of choices exists.

––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
2. Why It's Useful
––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
This principle allows us to:
• Prove that every vector space has a basis — even infinite-dimensional ones.
• Show that any set can be well-ordered (every subset has a least element).
• Derive key results in analysis, algebra, and topology — like Tychonoff’s Theorem.

But its power comes with strange consequences.

––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
3. A Paradoxical Consequence
––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
""")

    if show_paradox:
        print("""\
There’s a result known as the **Banach–Tarski paradox**. Here's what it says:

• You can take a solid sphere.
• Split it into just five pieces.
• Move and rotate those pieces — no stretching, no duplicating.
• Reassemble them into **two identical copies** of the original sphere.

This doesn’t break conservation of volume — because the pieces themselves are 
non-measurable in the traditional sense. They only exist because the axiom 
guarantees their selection — not because they can be constructed or seen.

It's a result that stretches the boundary between abstract mathematics and physical reality.

––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
4. Controversy and Choice
––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
• The axiom is **non-constructive** — it asserts existence without providing a method.
• It’s **independent** of standard set theory:
    ◦ You can accept it and get a rich, complete theory.
    ◦ You can reject it and get a more grounded, constructive approach.

Both worlds are internally consistent — but they lead to very different mathematics.

So we’re left with a strange philosophical choice:
> Do we allow principles that grant infinite power, even if they create outcomes
> we can’t visualize, build, or ever observe?

Mathematics says yes — but it also warns: use with care.
""")
        return "Banach–Tarski paradox: A sphere can be split and reassembled into two identical spheres."

    return None

def black_scholes_merton(*, show_explanation=True, show_example=False, S=100, K=100, T=1, r=0.05, sigma=0.2):
    """
    Explain the Black-Scholes-Merton equation for option pricing, and optionally compute
    the theoretical price of a European call option.

    Parameters
    ----------
    show_explanation : bool, default True
        Whether to print the theoretical background.
    show_example : bool, default False
        If True, compute and display a sample call option price using given parameters.
    S : float
        Current price of the underlying asset.
    K : float
        Strike price of the option.
    T : float
        Time to expiration (in years).
    r : float
        Risk-free interest rate (annualized).
    sigma : float
        Volatility of the underlying asset (standard deviation of returns).

    Returns
    -------
    call_price : float | None
        Price of the European call option if show_example=True, else None.
    """
    if show_explanation:
        print("""\
Title: Black–Scholes–Merton Equation – Pricing the Value of Risk

In the 1970s, Fischer Black, Myron Scholes, and Robert Merton introduced a groundbreaking
model that transformed financial markets forever. Their equation gives a theoretical estimate
for the price of a **European option** — a financial contract that grants the right, but not
the obligation, to buy (or sell) an asset at a specified price and time.

––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
1. The Core Idea
––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
The value of an option should reflect:
• The current price of the underlying asset (S),
• The strike price (K),
• Time remaining (T),
• Volatility of the asset (σ),
• And the risk-free interest rate (r).

To avoid arbitrage (riskless profit), the price must follow a differential equation:

    ∂V/∂t + (1/2)·σ²·S²·∂²V/∂S² + r·S·∂V/∂S − r·V = 0

Where:
- V = value of the option,
- S = asset price,
- t = time.

––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
2. The Solution (for a European Call Option)
––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
The closed-form solution for a European call is:

    C = S·N(d₁) − K·e^(−rT)·N(d₂)

Where:
    d₁ = [ln(S/K) + (r + σ²/2)·T] / (σ·√T)
    d₂ = d₁ − σ·√T
    N(x) = Cumulative distribution function of the standard normal distribution

This formula prices the call using the concept of **no-arbitrage** and the idea of constructing 
a "replicating portfolio" — a mix of stock and cash that behaves exactly like the option.

––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
3. Assumptions Behind the Model
––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
• No transaction costs or taxes
• Continuous trading
• Constant volatility and interest rate
• Log-normal price distribution
• The asset pays no dividends

Real markets aren't perfect — but the Black-Scholes-Merton model works surprisingly well as a baseline.

––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
4. Impact and Insight
––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
This equation turned finance into a precise science — earning Scholes and Merton the 1997 Nobel Prize 
in Economics (Black had passed away).

It shifted thinking from speculative pricing to **quantitative risk management** — and launched an 
entire industry of derivatives and mathematical finance.

Its deeper message:
> Even in a world full of randomness, it's possible to construct formulas that tame uncertainty — 
> if your assumptions are tight enough.

""")

    if show_example:
            
        d1 = (math.log(S / K) + (r + sigma ** 2 / 2) * T) / (sigma * math.sqrt(T))
        d2 = d1 - sigma * math.sqrt(T)
        call_price = S * norm.cdf(d1) - K * math.exp(-r * T) * norm.cdf(d2)

        print(f"\nSample Calculation — European Call Option Price:")
        print(f"Underlying Price (S): {S}")
        print(f"Strike Price (K):     {K}")
        print(f"Time to Expiry (T):   {T} year(s)")
        print(f"Risk-Free Rate (r):   {r}")
        print(f"Volatility (σ):       {sigma}")
        print(f"\nComputed Call Option Price: {call_price:.4f}")
        return call_price

    return None
