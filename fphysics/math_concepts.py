# A collection of fascinating math theories that I find intriguing and worth exploring.
# Mentions: Most of these concepts were inspired by videos from Veritasium, 3Blue1Brown.

import math
import cmath
import random
import itertools
import time
import numpy as np
from scipy.stats import norm


def taylor_series(*, show_explanation=True):
    """
    Explains the Taylor Series, how it approximates functions using polynomials,
    why it's fundamental to calculus and analysis, how it's computed, and some real-world applications.
    
    Parameters
    ----------
    show_explanation : bool, default True
        Whether to print the theoretical explanation.
    """
    if show_explanation:
        print("""\
Title: Taylor Series — Approximating the Universe with Polynomials
–––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
1. What Is the Taylor Series?
–––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
Imagine you have a complex function — like sin(x), e^x, or ln(x) — and you want to:
> "Approximate it using simple polynomials near a specific point."

The **Taylor Series** answers this question by expressing any smooth function as:
> An **infinite sum** of polynomial terms based on the function's derivatives.

It converts complicated functions into **manageable polynomial approximations**.
–––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
2. Why Is This Revolutionary?
Taylor series unlock the **polynomial structure** hidden in complex functions:
✓ Calculate transcendental functions (sin, cos, e^x, ln)  
✓ Solve differential equations analytically  
✓ Enable numerical computation in calculators  
✓ Power machine learning algorithms  
✓ Approximate physics models near equilibrium

> Complex functions often look intimidating.  
> Taylor series reveal their **polynomial DNA**.
–––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
3. The Core Insight: Local Linearity
Every smooth function is "locally linear" when zoomed in enough.
Taylor series extends this idea:
- **0th order**: Function value (constant approximation)
- **1st order**: Add slope (linear approximation)  
- **2nd order**: Add curvature (quadratic approximation)
- **nth order**: Add higher-order "wiggle" corrections

Each term captures more **subtle behavior** of the function.
–––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
4. The Mathematical Formula
For a function f(x) expanded around point a:
\[
f(x) = f(a) + f'(a)(x-a) + \frac{f''(a)}{2!}(x-a)^2 + \frac{f'''(a)}{3!}(x-a)^3 + ...
\]

Or more compactly:
\[
f(x) = \sum_{n=0}^{∞} \frac{f^{(n)}(a)}{n!}(x-a)^n
\]

When a = 0, it's called a **Maclaurin Series**.
–––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
5. Famous Examples That Changed Mathematics
**Exponential Function:**
e^x = 1 + x + x²/2! + x³/3! + x⁴/4! + ...

**Sine Function:**
sin(x) = x - x³/3! + x⁵/5! - x⁷/7! + ...

**Natural Logarithm:**
ln(1+x) = x - x²/2 + x³/3 - x⁴/4 + ... (for |x| < 1)

These infinite sums converge to exact function values!
–––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
6. The Power of Approximation
In practice, we truncate after a few terms:
- **Linear approximation**: f(x) ≈ f(a) + f'(a)(x-a)
- **Quadratic approximation**: Add the (x-a)² term
- **Higher orders**: More accuracy near point a

The trade-off: **More terms = Better accuracy = More computation**
–––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
7. Real-World Applications
✓ Calculator algorithms (computing sin, cos, exp)  
✓ Physics: Small oscillation approximations  
✓ Engineering: Linearizing nonlinear systems  
✓ Computer graphics: Efficient function evaluation  
✓ Machine learning: Gradient descent optimization  
✓ Numerical analysis: Error estimation  
✓ Economics: Marginal analysis and elasticity

Every time you press sin(x) on a calculator, you're using Taylor series!
–––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
8. Convergence: When Does It Work?
Taylor series don't always converge everywhere:
- **Radius of convergence**: How far from point a the series works
- **Analytic functions**: Have convergent Taylor series
- **Singularities**: Points where the series breaks down

Understanding convergence is crucial for reliable approximation.
–––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
9. Summary: Taylor Series = Mathematical DNA
- Taylor series reveal the **polynomial essence** of any smooth function  
- They bridge the gap between **complex analysis and simple arithmetic**  
- Enable computation of transcendental functions  
- Form the foundation of **numerical analysis and approximation theory**

> "Every function has a story told in derivatives."  
> "Taylor series translate that story into polynomial language."

"The Taylor series is not just a mathematical curiosity; 
 it is the foundation of how we compute in the modern world."
                                                    ~Mathematical Heritage
""")


def pi_collision_problem(*, show_explanation=True):
    """
    Explains the Pi Collision Problem, how colliding blocks can compute digits of π,
    why this works through conservation laws and geometry, and the beautiful mathematics behind it.
    
    Parameters
    ----------
    show_explanation : bool, default True
        Whether to print the theoretical explanation.
    """
    if show_explanation:
        print("""\
Title: The Pi Collision Problem — Computing π Through Bouncing Blocks
–––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
1. What Is the Pi Collision Problem?
–––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
Imagine this bizarre scenario:
> Two blocks slide on a frictionless surface. One block (mass m) approaches another 
> block (mass M) that's initially at rest near a wall. All collisions are perfectly elastic.

The **Pi Collision Problem** reveals this stunning fact:
> The **total number of collisions** gives you the digits of π!

When M = 100^(n-1) × m, you get exactly **n digits of π** in the collision count.
–––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
2. The Setup: A Physics Thought Experiment
**Components:**
- Small block (mass m) moving right with initial velocity v₀
- Large block (mass M = 100^(n-1) × m) initially at rest  
- Immovable wall on the right
- All collisions are perfectly elastic (no energy loss)

**The Process:**
1. Small block hits large block → both start moving right
2. Large block hits wall → bounces back left  
3. Blocks collide again... and again... and again...
4. Eventually, small block bounces left faster than large block
5. **Count the total collisions!**
–––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
3. The Miraculous Results
For different mass ratios:
- M = m (ratio 1:1) → **3 collisions** → π ≈ 3.14...
- M = 100m (ratio 100:1) → **31 collisions** → π ≈ 3.14...
- M = 10,000m (ratio 10⁴:1) → **314 collisions** → π ≈ 3.14...
- M = 1,000,000m (ratio 10⁶:1) → **3141 collisions** → π ≈ 3.14...

**Pattern:** Mass ratio of 100^(n-1) gives **first n digits of π**!
–––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
4. Why Does This Work? The Deep Mathematics
This isn't magic — it's beautiful geometry disguised as physics:

**Conservation Laws:**
- Energy: ½mv₁² + ½Mv₂² = constant
- Momentum: mv₁ + Mv₂ = constant

**The Key Insight:**
These conservation equations define an **ellipse** in velocity space (v₁, v₂).
Each collision corresponds to a **reflection** across a specific line.

**Geometric Connection:**
The collision angles in velocity space are related to **arctan(√(m/M))**.
When M >> m, this approaches **arctan(1/√(100^(n-1))) ≈ π/(2√(100^(n-1)))**
–––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
5. The Phase Space Perspective
**Brilliant Insight:** Map the problem to 2D phase space!

**Coordinates:** (√m × v₁, √M × v₂)
- This makes the energy constraint a **perfect circle**!
- Collisions become **reflections** across specific axes
- The number of reflections = arc length / angle step

**The Connection to π:**
- Quarter circle arc length = πR/2
- Angular step size ≈ π/(2√(M/m)) for large M/m
- Number of steps = (πR/2) / (π/(2√(M/m))) = √(M/m)
- When M/m = 100^(n-1), collisions ≈ 10^(n-1) × π
–––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
6. Mathematical Elegance: From Physics to Geometry
**The Transformation:**
Classical mechanics → Conservation laws → Ellipse geometry → Circular reflections → π

**Why This Is Profound:**
- Connects **Newtonian mechanics** with **pure geometry**
- Shows π hiding in **dynamical systems**  
- Demonstrates how **coordinate transforms** reveal hidden structure
- Links **discrete collisions** to **continuous circular motion**
–––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
7. Computational Aspects
**As a π Algorithm:**
- Theoretically exact for infinite precision
- Practically inefficient (need exponentially large mass ratios)
- Mainly of theoretical and pedagogical interest

**Complexity:** O(10^n) collisions to get n digits of π
**Comparison:** Much slower than modern π algorithms, but infinitely more beautiful!
–––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
8. Educational Impact and Wonder
This problem showcases:
✓ **Conservation laws** in action  
✓ **Coordinate transformations** revealing hidden structure  
✓ **Dynamical systems** and phase space analysis  
✓ Connection between **discrete and continuous** mathematics  
✓ **Geometric interpretation** of physical processes  
✓ Why π appears in **unexpected places**

**The Pedagogical Beauty:**
Students see advanced mathematical concepts through a simple, intuitive setup.
–––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
9. Summary: π Emerges from Collisions
- **Physical setup**: Two blocks and a wall with elastic collisions
- **Mathematical reality**: Circle geometry in disguise  
- **Deep connection**: Classical mechanics ↔ Pure geometry ↔ Number theory
- **Educational value**: Makes advanced concepts tangible and memorable

> "Who would have thought that counting bouncing blocks  
>  could reveal the geometry of circles?"

> "Sometimes the most profound mathematics hides behind  
>  the simplest physical setups."

"The most beautiful thing we can experience is the mysterious."
                                                    ~Albert Einstein
""")

def hermite_polynomials(*, show_explanation=True):
    """
    Explains Hermite Polynomials, how they emerge from quantum mechanics and probability theory,
    their orthogonality properties, generating functions, and applications across mathematics and physics.
    
    Parameters
    ----------
    show_explanation : bool, default True
        Whether to print the theoretical explanation.
    """
    if show_explanation:
        print("""\
Title: Hermite Polynomials — The Mathematical DNA of Quantum Mechanics
–––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
1. What Are Hermite Polynomials?
–––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
Hermite polynomials are a special family of orthogonal polynomials that naturally emerge when:
> "You study the quantum harmonic oscillator or Gaussian probability distributions."

**Definition (Physicist's Version):**
H_n(x) = (-1)^n e^(x²) d^n/dx^n [e^(-x²)]

**Definition (Probabilist's Version):**
He_n(x) = (-1)^n e^(x²/2) d^n/dx^n [e^(-x²/2)]

They form the **eigenfunctions** of nature's most fundamental oscillating systems.
–––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
2. The First Few Hermite Polynomials
**Physicist's Hermite Polynomials H_n(x):**
- H₀(x) = 1
- H₁(x) = 2x  
- H₂(x) = 4x² - 2
- H₃(x) = 8x³ - 12x
- H₄(x) = 16x⁴ - 48x² + 12
- H₅(x) = 32x⁵ - 160x³ + 120x

**Pattern:** Each polynomial has **definite parity** (even/odd) and **increasing degree**.
–––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
3. Why Are They Revolutionary?
Hermite polynomials unlock the **wave function structure** of quantum systems:
✓ **Quantum harmonic oscillator** eigenstates  
✓ **Gaussian random processes** in probability  
✓ **Signal processing** and Fourier analysis  
✓ **Numerical integration** (Gauss-Hermite quadrature)  
✓ **Polynomial chaos** expansions in uncertainty quantification  
✓ **Heat equation** solutions on infinite domains

> They are nature's chosen basis for **oscillatory phenomena**.
–––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
4. Orthogonality: The Core Mathematical Property
**Weighted Orthogonality Relation:**
∫_{-∞}^{∞} H_m(x) H_n(x) e^(-x²) dx = √π 2^n n! δ_{mn}

**What This Means:**
- Different Hermite polynomials are **orthogonal** with Gaussian weight
- They form a **complete basis** for functions in L²(ℝ, e^(-x²) dx)
- Any "reasonable" function can be expanded as a **Hermite series**

**Normalized Hermite Functions:**
ψ_n(x) = (1/√(2^n n! √π)) H_n(x) e^(-x²/2)
–––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
5. The Quantum Connection: Harmonic Oscillator
**Schrödinger Equation for Harmonic Oscillator:**
[-ℏ²/(2m) d²/dx² + (1/2)mω²x²] ψ(x) = E ψ(x)

**Miracle:** The solutions are exactly **Hermite functions**!
- **Energy levels:** E_n = ℏω(n + 1/2)  
- **Wave functions:** ψ_n(x) ∝ H_n(√(mω/ℏ)x) exp(-mωx²/(2ℏ))

**Physical Meaning:**
- n = 0: **Ground state** (minimum energy, Gaussian shape)
- n > 0: **Excited states** with n **nodes** (zero crossings)
- Higher n: More **oscillatory** behavior
–––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
6. Generating Functions and Recursion
**Exponential Generating Function:**
e^(2xt - t²) = Σ_{n=0}^{∞} H_n(x) t^n/n!

**This single function encodes ALL Hermite polynomials!**

**Recurrence Relations:**
- H_{n+1}(x) = 2x H_n(x) - 2n H_{n-1}(x)
- H'_n(x) = 2n H_{n-1}(x)
- (d/dx - 2x) H_n(x) = -2n H_{n-1}(x)

These relations enable **efficient computation** and reveal **algebraic structure**.
–––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
7. The Hermite Conjugate Connection
**For Complex Functions and Matrices:**

**Hermite Conjugate** of a matrix A: A† = (A*)^T
- **Hermitian matrices:** A† = A (self-adjoint)
- **Unitary matrices:** A†A = I
- **Normal matrices:** AA† = A†A

**Connection to Hermite Polynomials:**
In quantum mechanics, **Hermitian operators** (like position x̂, momentum p̂) have:
- **Real eigenvalues** (observable quantities)
- **Orthogonal eigenfunctions** (often Hermite functions)
- **Complete basis sets** for the Hilbert space

The name "Hermite" honors Charles Hermite's work on **both** concepts!
–––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
8. Applications Across Science
**Quantum Mechanics:**
- Harmonic oscillator states
- Coherent state decompositions  
- Path integral formulations

**Probability Theory:**
- Gaussian chaos expansions
- Wiener-Hermite expansions of random processes
- Polynomial chaos methods in uncertainty quantification

**Signal Processing:**
- Hermite-Gaussian beams in optics
- Time-frequency analysis
- Wavelet transforms

**Numerical Analysis:**
- Gauss-Hermite quadrature rules
- Spectral methods for PDEs
- Approximation theory
–––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
9. Computational Aspects
**Three Ways to Compute H_n(x):**
1. **Rodrigues' formula:** H_n(x) = (-1)^n e^(x²) d^n/dx^n [e^(-x²)]
2. **Recurrence relation:** H_{n+1} = 2x H_n - 2n H_{n-1}  
3. **Generating function:** Expand e^(2xt - t²)

**Numerical Stability:** Recurrence relation is most stable for computation.
**Applications:** Essential for quantum chemistry, spectral methods, and Monte Carlo simulations.
–––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
10. Summary: Hermite Polynomials = Nature's Oscillation Language
- **Origin:** Emerge naturally from Gaussian distributions and quantum mechanics
- **Structure:** Orthogonal polynomials with exponential weight function  
- **Applications:** Quantum physics, probability theory, signal processing
- **Beauty:** Connect **discrete polynomial algebra** with **continuous quantum mechanics**

> "Hermite polynomials are the musical notes of quantum mechanics —  
>  each eigenstate plays a different harmonic in nature's symphony."

> "In the language of mathematics, oscillation speaks Hermite."

"The Hermite polynomials embody the deep connection between  
 the discrete and the continuous, the algebraic and the analytic."
                                                    ~Mathematical Legacy
""")

def Depressed_Cubic(p=None, q=None, *, show_explanation=True):
    """
    Print the depressed cubic theory and, if p and q are provided, return a real (or complex) root
    of the depressed cubic x³ + px + q = 0.
    
    Parameters
    ----------
    p, q : float | int
        Coefficients in the equation x³ + px + q = 0.
    show_explanation : bool, default True
        Whether to print the theoretical explanation and formula.
        
    Returns
    -------
    root : complex | None
        One root of the cubic (None if p or q were not supplied).
    """
    if show_explanation:
        print("""\
Title: The Depressed Cubic — Unlocking the Secrets of Cubic Equations
–––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
1. What Is a Depressed Cubic?
–––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
A **depressed cubic** is a cubic equation with the quadratic term removed:
    x³ + px + q = 0

The term "depressed" means **"pressed down"** — the x² coefficient has been eliminated.

**Why This Form Matters:**
- **Simplifies** the general cubic ax³ + bx² + cx + d = 0
- **Reveals** the essential structure hidden in cubic equations  
- **Enables** systematic solution methods like Cardano's formula
- **Connects** algebra to beautiful geometric transformations

–––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
2. From General to Depressed: The Transformation
–––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
**Starting Point:** General cubic equation
    ax³ + bx² + cx + d = 0

**Step 1:** Normalize (divide by a)
    x³ + (b/a)x² + (c/a)x + (d/a) = 0

**Step 2:** Substitute x = t - b/(3a) to eliminate the x² term
**Result:** The depressed cubic
    t³ + pt + q = 0

**Mathematical Magic:** This substitution **always works** for any cubic!

–––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
3. Cardano's Formula: The Cubic Solution
–––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
For the depressed cubic x³ + px + q = 0:

In the 16th century, building on Tartaglia's work, Cardano published the
closed‑form solution in his *Ars Magna*:

        x = ∛(-q/2 + Δ) + ∛(-q/2 - Δ),
    where Δ = √((q/2)² + (p/3)³).

**The Discriminant:**
    Δ² = (q/2)² + (p/3)³

**Three Cases Based on the Discriminant:**
- **Δ² > 0:** One real root, two complex conjugate roots
- **Δ² = 0:** Multiple real roots (at least two equal)  
- **Δ² < 0:** Three distinct real roots (**Casus irreducibilis**)

–––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
4. The Casus Irreducibilis: When Reality Gets Complex
–––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
**The Paradox:**
When Δ² < 0, we have **three real roots**, but Cardano's formula involves:
> **Complex numbers** to express **real solutions**!

**Historical Impact:** This paradox drove the development of **complex number theory**!

The other two roots can be found by multiplying the cube‑roots by the 
complex cube roots of unity ω = e^(2πi/3).

–––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
5. Applications and Mathematical Beauty
–––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
**Applications:**
✓ **Optimization**: Critical points of cubic functions
✓ **Physics**: Equations of state, phase transitions  
✓ **Engineering**: Stress analysis, fluid dynamics
✓ **Computer Graphics**: Bézier curves and spline interpolation

**Mathematical Elegance:**
The depressed cubic reveals that **complexity often hides simplicity** — 
by removing one term, we unlock the entire structure of cubic equations.

> "Sometimes, mathematical depression is exactly what we need  
>  to see clearly through the algebraic complexity."

"In algebra, as in life, sometimes we must remove the unnecessary  
 to discover the essential."
                                                    ~Algebraic Wisdom
""")
    
    # If no coefficients were given, just exit after printing.
    if p is None or q is None:
        return None
    
    # Cardano's formula
    Δ = cmath.sqrt((q / 2) ** 2 + (p / 3) ** 3)
    u = (-q / 2 + Δ) ** (1 / 3)
    v = (-q / 2 - Δ) ** (1 / 3)
    root = u + v
    
    # Show the numerical result
    print(f"Root for p = {p}, q = {q} :  {root}")
    return root


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
Title: Goldbach's Conjectures – A Timeless Enigma in Number Theory
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

    if n < 2:
        primes = set()
    else:
        sieve = [True] * (n + 1)
        sieve[0] = sieve[1] = False
        for i in range(2, int(n ** 0.5) + 1):
            if sieve[i]:
                for j in range(i * i, n + 1, i):
                    sieve[j] = False
        primes = {i for i in range(2, n + 1) if sieve[i]}
    results = []
    
    if n % 2 == 0:
        # Strong Goldbach demo (even number > 2)
        for a in range(2, n // 2 + 1):
            b = n - a
            if a in primes and b in primes:
                results.append((a, b))
        print(f"Strong Goldbach pairs for {n}: {results}")
    else:
        # Weak Goldbach demo (odd number > 5)
        prime_list = sorted(primes)
        for a in prime_list:
            if a >= n - 4:
                break
            for b in prime_list:
                if b < a or a + b >= n - 1:
                    continue
                c = n - a - b
                if c >= b and c in primes:
                    results.append((a, b, c))
                        
        print(f"Weak Goldbach triplets for {n}: {results}")
    return results if results else None


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
        # Calculate d1 and d2
        d1 = (math.log(S / K) + (r + sigma ** 2 / 2) * T) / (sigma * math.sqrt(T))
        d2 = d1 - sigma * math.sqrt(T)
        
        # Calculate call option price using Black-Scholes formula
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

def p_adics(*, show_explanation=True, simulate=False, p=10, digits=10):
    """
    Explain the concept of p-adic numbers and optionally simulate a p-adic expansion.
    Parameters
    ----------
    show_explanation : bool, default True
        Whether to print the theoretical and intuitive background.
    simulate : bool, default False
        If True, demonstrate p-adic expansion of a sample number.
    p : int, default 10
        Base prime (or 10 for decimal-like behavior); must be ≥ 2.
    digits : int, default 10
        Number of digits to show in the p-adic expansion (right-to-left).
    Returns
    -------
    expansion : list[int] | None
        The list of digits in the p-adic expansion, or None if simulate=False.
    """
    if show_explanation:
        print(f"""\
Title: p-adic Numbers — A Different Notion of Distance and Expansion
p-adics are a surprising alternative to the real numbers. While real numbers are built
around powers of 1/10 or 1/2, **p-adics are built from powers of a fixed base p, but going
in the opposite direction**.
–––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
1. What Makes p-adics Different?
–––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
• In real numbers:
  1.9999... = 2.0000...
• In p-adics:
  9999...9 (with infinite 9s to the left) may *not* equal a finite integer.
  Instead, infinite-left expansions are **normal** and meaningful!
• The "distance" between numbers is defined using **divisibility** by p.
  Two numbers are "close" if their difference is divisible by a high power of p.
–––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
2. p-adic Expansion (for integers)
–––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
Any integer has a **p-adic expansion** like:
    x = a₀ + a₁·p + a₂·p² + a₃·p³ + ...
Where aᵢ ∈ (0, 1, ..., p−1)
For example:
• In base 10 (10-adics), the number −1 is represented as 9 + 9·10 + 9·10² + ...
• In 2-adics, −1 becomes 1 + 2 + 4 + 8 + 16 + ... (an infinite sum)
–––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
3. Why It Matters
–––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
• p-adics are **complete number systems**, just like reals — but with totally different geometry.
• They are crucial in **number theory**, **modular arithmetic**, and **algebraic geometry**.
• They help solve congruences that are hard in the real world but easy in p-adics.
""")
    if not simulate:
        return None
    
    number = -1
    expansion = []
    n = number
    for _ in range(digits):
        r = n % p
        expansion.append(r)
        n = (n - r) // p
    
    print(f"\n{p}-adic expansion of {number} (up to {digits} digits):")
    print(" + ".join(f"{d}·{p}^{i}" for i, d in enumerate(expansion)))
    return expansion

def law_of_large_numbers(*, show_explanation=True):
    """
    Explains the Law of Large Numbers — a foundational principle in probability theory that describes how the average
    of results from a random process converges to the expected value as the number of trials increases.

    Parameters
    ----------
    show_explanation : bool, default True
        Whether to print the theoretical explanation.
    """
    if show_explanation:
        print("""\
Title: The Law of Large Numbers — Predictability in the Long Run

–––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
1. What Is the Law of Large Numbers?
–––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––

It’s a fundamental concept in probability:

> As the number of trials of a random experiment increases, the **sample average** gets closer to the **true average** (expected value).

Mathematically:
        lim (n→∞) (1/n) Σ Xᵢ = μ

✓ Xᵢ: individual outcomes  
✓ μ: the expected value  
✓ n: number of trials

–––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
2. Intuition: Coin Tosses and Casinos

Flip a fair coin:
- Head = 1, Tail = 0  
- Expected value = 0.5

✓ 10 flips? Could be 7 heads → 0.7 average  
✓ 10,000 flips? Much closer to 0.5  
✓ 1,000,000 flips? Almost certainly around 0.5

> “Randomness rules in the short run — but in the long run, patterns emerge.”

–––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
3. Why Does It Matter?

✓ It bridges **probability** and **reality**  
✓ Justifies **statistics** — estimating population parameters from samples  
✓ Validates **insurance**, **gambling odds**, and **machine learning** models  
✓ Shows why **rare events** still follow predictable long-term behavior

> “The universe has noise, but also rhythm — the law of large numbers listens to the rhythm.”

–––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
4. Strong vs Weak Law

✓ **Weak Law**: Convergence in probability  
✓ **Strong Law**: Convergence almost surely (with probability 1)

Both mean: as you take more samples, the average will almost certainly settle around the expected value.

–––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
5. Real-World Applications

✓ **Quality control**: Sample enough products to estimate overall defect rate  
✓ **Polls**: More people surveyed = more accurate predictions  
✓ **Finance**: Stock returns fluctuate, but long-term averages guide strategy  
✓ **A/B testing**: Confirms whether version A or B performs better over many users

–––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
6. Summary: Randomness with Rules

- Short-term results can be noisy and misleading  
- Long-term averages reveal the **true nature** of the process  
- A law that brings **order to chance**  
- Essential for science, statistics, and sense-making in uncertainty

> “In the chaos of randomness, the law of large numbers is a quiet promise of predictability.”

"It tells us: the more you observe, the closer you get to the truth."
""")


def markov_chain(*, show_explanation=True):
    """
    Explains the concept of Markov Chains — a mathematical system that undergoes transitions from one state to another
    based on certain probabilities. Focuses on core ideas, properties, and real-world applications.

    Parameters
    ----------
    show_explanation : bool, default True
        Whether to print the theoretical explanation.
    """
    if show_explanation:
        print("""\
Title: Markov Chains — State Transitions and Long-Term Behavior

–––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
1. What Is a Markov Chain?
–––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––

A **Markov Chain** is a mathematical model for systems that move between a finite set of states with fixed probabilities.

The defining feature:
> The **next state depends only on the current state**, not the history of previous states.

This is known as the **Markov property** or **memorylessness**.

–––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
2. Structure of a Markov Chain

✓ A **set of states** (e.g., Sunny, Cloudy, Rainy)  
✓ A **transition matrix** defining probabilities of moving between states  
✓ An **initial state distribution** (optional for simulations)

Example transition matrix:

         Sunny   Cloudy   Rainy
Sunny     0.6      0.3     0.1
Cloudy    0.2      0.5     0.3
Rainy     0.1      0.4     0.5

Each row represents the probabilities of transitioning **from** a given state.

–––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
3. Types of Markov Chains

- **Discrete-time Markov Chain**: State changes at fixed time steps  
- **Continuous-time Markov Chain**: Transitions occur continuously over time  
- **Finite vs Infinite Chains**: Based on whether the number of states is limited or not

–––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
4. Steady State and Long-Term Behavior

Many Markov Chains converge to a **steady-state distribution**:  
→ A probability vector that doesn’t change after further transitions.

This steady state shows the **long-run proportion of time** the system spends in each state.

Conditions for a steady state:
✓ The chain is **irreducible** (all states communicate)  
✓ The chain is **aperiodic** (not trapped in a cycle)

–––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
5. Real-World Applications

✓ **Weather prediction**  
✓ **Board games** (e.g., Monopoly, Snake and Ladders)  
✓ **Google PageRank** — ranking web pages as a Markov process  
✓ **Queueing systems** — like customers arriving at a service desk  
✓ **Speech recognition**, **natural language processing**, and **genetic sequencing**

–––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
6. Summary: Random Transitions, Predictable Patterns

- Markov Chains model state transitions with **fixed probabilities**  
- They obey the **memoryless property** — the next state depends only on the current one  
- Many chains settle into a **predictable steady-state distribution**  
- A powerful tool in understanding **stochastic (random) systems**

> “Markov Chains describe systems that evolve randomly — but predictably — over time.”
""")


def basel_problem(show_explanation=True):
    """
    Explains the Basel problem and how Euler solved it by summing the reciprocal of squares.
    """
    if show_explanation:
        print("""\
Title: The Basel Problem – The Sum of Reciprocal Squares

–––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
1. The Problem

The Basel problem asks for the exact sum of the infinite series:

    1 + 1/4 + 1/9 + 1/16 + 1/25 + ... = ∑(1/n²) for n=1 to ∞

This is the sum of the reciprocals of the perfect squares. Mathematicians tried for decades to find the precise value of this sum — they knew it converged but didn’t know *to what*.

–––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
2. Historical Background

The problem was first posed by Pietro Mengoli in 1644 and remained unsolved for nearly a century. It earned its name from the hometown of the Bernoulli family (Basel, Switzerland), several of whom tried and failed to solve it. Even Jakob Bernoulli couldn’t crack it.

–––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
3. Euler’s Breakthrough

In 1734, the 28-year-old **Leonhard Euler** shocked the mathematical world by solving it. He found:

    ∑(1/n²) = π² / 6

This was a stunning result — it linked an **infinite sum of rational numbers** to **π**, which emerges from geometry and circles. No one expected such a connection.

–––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
4. How Did He Do It?

Euler cleverly considered the expansion of the sine function:

    sin(x)/x = (1 - x²/π²)(1 - x²/4π²)(1 - x²/9π²) ...

This is known as the infinite product representation of sine. He compared this to the standard power series expansion:

    sin(x)/x = 1 - x²/6 + x⁴/120 - ...

By matching the coefficients of x² in both expansions, he was able to deduce the sum of 1/n² must be π²/6.

–––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
5. Modern Significance

Euler’s result launched a whole new area of mathematics involving the Riemann zeta function:

    ζ(s) = ∑(1/nˢ) for s > 1

The Basel problem is just the case when s = 2:

    ζ(2) = π²/6

It turns out that ζ(4) = π⁴/90, ζ(6) = π⁶/945, and so on — the even zeta values are deeply tied to powers of π.

The odd values like ζ(3), however, are still mysterious and not known to be rational or irrational in general.

–––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
6. Conclusion

The Basel problem is a beautiful illustration of the unexpected harmony in mathematics — linking geometry, infinite series, and complex analysis. Euler’s bold insight remains one of the most elegant results in the history of math.

> “It is amazing that the sum of simple fractions adds up to a number involving π — the very symbol of circles.” – Inspired by Euler's genius
""")


def riemann_zeta_function():
    """
    Explains the Riemann Zeta Function — a complex function deeply connected to the distribution
    of prime numbers. Includes its definition, key properties, and mathematical significance.
    """
    print("""\
Title: The Riemann Zeta Function — Gateway to Prime Numbers

––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
The **Riemann Zeta Function** is a function of a complex variable, defined initially for
real numbers greater than 1 as:

        ζ(s) = 1 + 1/2^s + 1/3^s + 1/4^s + ...

This infinite series converges when the real part of **s** is greater than 1.  
It can be analytically continued to other values of **s**, except **s = 1**, where it diverges.

––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
Euler’s Connection to Prime Numbers

Leonhard Euler discovered that the zeta function encodes prime numbers through the identity:

        ζ(s) = ∏ (1 / (1 - p^(-s)))     (product over all primes p)

This shows a profound link between the zeta function and the **distribution of primes**.

––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
Extension to Complex Numbers

Bernhard Riemann extended ζ(s) to complex values and studied its properties in the 19th century.  
He discovered that the function has **trivial zeros** at negative even integers:

        ζ(-2) = ζ(-4) = ζ(-6) = ... = 0

The real mystery lies in the **non-trivial zeros** — the values of **s** for which ζ(s) = 0  
in the critical strip where 0 < Re(s) < 1.

––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
The Riemann Hypothesis

The famous unsolved conjecture proposes:

> "All non-trivial zeros of the zeta function lie on the line Re(s) = 1/2."

If true, this would imply **very precise control over the distribution of prime numbers**.  
It is one of the **Millennium Prize Problems** with a $1 million reward for proof.

––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
Applications

✓ Prime number theorem  
✓ Cryptography and randomness  
✓ Quantum chaos  
✓ Analytic number theory  
✓ Fractal dimensions and statistical mechanics

––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
Conclusion

The Riemann Zeta Function sits at the intersection of analysis, number theory, and complex systems.  
Understanding its behavior is like holding the key to the secrets of prime numbers — the atoms of arithmetic.

> “The zeta function is not just a function — it's a deep window into the fabric of mathematics.”
""")


def dirichlets_theorem():
    """
    Explains Dirichlet's Theorem on Arithmetic Progressions — a foundational result in number theory
    showing that primes are evenly distributed among suitable arithmetic sequences.
    """
    print("""\
Title: Dirichlet’s Theorem — Primes in Arithmetic Progressions

––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
Dirichlet’s Theorem states that for any two **positive coprime integers** a and d (i.e., gcd(a, d) = 1),  
the arithmetic sequence:

        a, a + d, a + 2d, a + 3d, ...

contains **infinitely many prime numbers**.

For example:
✓ The sequence 5, 10, 15, 20, 25, ... (with a = 5, d = 5) has only one prime: 5  
✗ But the sequence 5, 10, 15, 20, ... is not valid because gcd(5, 5) ≠ 1.

Now consider:
✓ 3, 7, 11, 15, 19, 23, ... (a = 3, d = 4), with gcd(3, 4) = 1  
This contains infinitely many primes: 3, 7, 11, 19, 23, 31, ...

––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
Key Condition: Coprimality

The requirement **gcd(a, d) = 1** is essential.  
If a and d share a common factor, then every number in the sequence is divisible by that factor  
— making it impossible to have infinitely many primes.

––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
Importance and Impact

Dirichlet proved this theorem using **Dirichlet L-functions** and **characters modulo n**,  
which laid the groundwork for **analytic number theory**.

✓ Generalizes the idea that primes don’t just “cluster randomly” — they **distribute evenly** across valid progressions  
✓ Helps understand the **density of primes** in specific modular classes  
✓ Key to advanced results like **Chebotarev’s theorem** and **modular forms**

––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
Conclusion

Dirichlet's Theorem is a gateway into the structured world of prime numbers and modular arithmetic.  
It shows that even within the rigid structure of arithmetic progressions, primes are **guaranteed** to appear infinitely often — as long as the starting conditions are right.

> “Primes may be elusive, but Dirichlet showed they are not random — they follow rules, even in patterns.”
""")

def types_of_infinity():
    """
    Explains the concept of different types of infinity in mathematics,
    including countable and uncountable infinities, with examples.
    """
    print("""\
Title: Different Types of Infinity — Countable and Uncountable

–––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
Infinity in mathematics is not a single concept — there are **multiple sizes** or **types** of infinity. These arise especially in set theory, pioneered by **Georg Cantor**.

1. Countable Infinity:
–––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
A set is *countably infinite* if its elements can be put in one-to-one correspondence with the natural numbers.

Examples:
✓ Natural numbers: 1, 2, 3, ...
✓ Even numbers: 2, 4, 6, ...
✓ Rational numbers (fractions): Though dense, they are still countable.

→ All these sets have the same "size" of infinity, denoted **ℵ₀ (aleph-null)**.

2. Uncountable Infinity:
–––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
Some sets are so large that they **cannot** be matched with natural numbers.

Examples:
✓ Real numbers between 0 and 1  
✓ Points on a line  
✓ Irrational numbers (like π, √2)

→ These have a **larger cardinality** than ℵ₀, called the **cardinality of the continuum** and denoted **𝑐**.

Cantor's Diagonal Argument:
Cantor proved that the real numbers are **uncountable** using a clever diagonalization argument — constructing a number not in any assumed complete list.

3. Infinity Hierarchy:
–––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
Infinity isn't just "countable" vs "uncountable". There's a **whole hierarchy** of infinities:

✓ ℵ₀ < ℵ₁ < ℵ₂ < ...  
Each new ℵ represents a strictly larger kind of infinity.

Whether **𝑐 = ℵ₁** is known as the **Continuum Hypothesis**, one of the most famous problems in mathematics — it’s **independent** of standard set theory (ZFC).

–––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
Conclusion:
Infinity is not a single idea, but a landscape of different sizes. From the infinity of counting numbers to the uncountable infinity of real numbers, and even beyond, mathematics treats infinity with precision.

> “Some infinities are bigger than others.” — Cantor's legacy in set theory
""")



def Kronecker_delta(
        i: int,
        j: int,
        show_explanation: bool = True
    ) -> int:
    """
    Compute the Kronecker delta δ_ij.

    Definition
    ----------
    δ_ij = 1 if i == j
         = 0 if i != j

    It acts like the discrete version of the Dirac delta:
    - In linear algebra, it represents the identity matrix entries.
    - In summations, it "picks out" terms where indices match.
    - In computer science, it's useful as an equality check written in math notation.

    Parameters
    ----------
    i : int
        First index
    j : int
        Second index
    show_explanation : bool
        If True, print an explanation.

    Returns
    -------
    delta : int
        1 if i == j else 0
    """

    if show_explanation:
        print("""\
Title: Kronecker Delta δ_ij

The Kronecker delta is a simple function of two integers i and j:

    δ_ij = { 1  if i = j
             0  if i ≠ j }

It is widely used in mathematics, physics, and computer science:

1. **Identity Matrix**:
   δ_ij is exactly the (i, j) entry of the identity matrix.

2. **Summation Selector**:
   In sums, it 'selects' terms when indices match:
       Σ a_j δ_ij = a_i

3. **Computer Science Analogy**:
   Equivalent to an equality check:
       δ_ij = int(i == j)
""")

    return 1 if i == j else 0

def Plancherel_theorem(
        f: np.ndarray,
        show_explanation: bool = True
    ) -> tuple[float, float]:
    """
    Demonstrate Plancherel's theorem using the Discrete Fourier Transform (DFT).

    Plancherel's theorem (continuous form):
        ∫ |f(x)|^2 dx = ∫ |F(k)|^2 dk
    where F(k) is the Fourier transform of f(x).

    In the discrete case (via FFT), it states that the energy (L2 norm) of a
    sequence is preserved under the Fourier transform (up to a normalization).

    Parameters
    ----------
    f : np.ndarray
        Discrete signal (1D array).
    show_explanation : bool
        If True, print an overview of the theorem.

    Returns
    -------
    time_energy : float
        Energy of the signal in the time domain.
    freq_energy : float
        Energy of the signal in the frequency domain.
    """

    if show_explanation:
        print("""\
Title: Plancherel's Theorem

Plancherel's theorem is a fundamental result in Fourier analysis:

    The total energy of a signal is preserved
    between the time domain and the frequency domain.

In math form:
    ∫ |f(x)|^2 dx = ∫ |F(k)|^2 dk

Where:
• f(x)  = function in time/space domain
• F(k)  = Fourier transform of f(x)
• |.|^2 = squared magnitude (energy density)

Interpretation:
- Energy in a signal is invariant under Fourier transform.
- This makes Fourier analysis a powerful tool in physics,
  signal processing, and quantum mechanics.
""")

    # Compute time-domain energy
    time_energy = np.sum(np.abs(f)**2)

    # Compute frequency-domain energy (via FFT)
    F = np.fft.fft(f)
    freq_energy = np.sum(np.abs(F)**2) / len(f)  # normalization for discrete case

    return time_energy, freq_energy

def godel_incompleteness_theorem(*, show_explanation=True, demo=False):
    """
    Display an overview of Gödel's Incompleteness Theorems and optionally give an illustrative analogy.

    Parameters
    ----------
    show_explanation : bool, default True
        Whether to print the detailed historical and conceptual explanation.
    demo : bool, default False
        If True, show a metaphorical example illustrating the core idea.

    Returns
    -------
    None
        This function prints the explanation and optional analogy but returns nothing.
    """
    if show_explanation:
        print("""\
Title: Gödel's Incompleteness Theorems – Limits of Formal Mathematical Systems

In 1931, Austrian logician **Kurt Gödel** published two groundbreaking theorems 
that forever changed mathematics, logic, and philosophy.

The First Incompleteness Theorem:
    In any *consistent* formal system (rich enough to include arithmetic), 
    there are true statements that **cannot** be proven within the system.

    ➜ Meaning: No matter how powerful your axioms are, there will always be truths
      they cannot reach.

The Second Incompleteness Theorem:
    Such a system cannot prove its **own consistency** from within.

    ➜ Meaning: If you want to prove the system's consistency, you need to step 
      outside the system — but then that new system faces the same problem.

Philosophical Consequences:
    • Mathematics is not a closed, complete universe — it has unavoidable "blind spots".
    • Hilbert's dream of a fully complete, self-contained math (the 'Hilbert Program') failed.
    • Truth and provability are not the same thing.

Gödel achieved this by encoding statements about logic *within* logic itself —
creating a statement that, in effect, says: "This statement is not provable."
If it were provable, it would be false — a paradox — so it must be true, yet unprovable.
""")

    if demo:
        print("""\
Analogy: The Librarian's Impossible Catalogue

Imagine a huge library with a perfect catalogue listing *every book it contains*.
One day, someone writes a book titled:
    "This book is not listed in the library's catalogue."

Case 1: The catalogue lists it → contradiction (it says it's not listed, but it is).
Case 2: The catalogue does not list it → contradiction (then it *should* be listed).

This mirrors Gödel's construction: a statement that truthfully asserts its own
unprovability inside the system.

Conclusion: Every powerful enough system of rules will have truths it cannot capture.
""")

def Hilbert_Program(*, show_explanation=True):
    """
    Explain David Hilbert's three foundational goals for mathematics and how they were ultimately
    shown to be unattainable.

    Parameters
    ----------
    show_explanation : bool, default True
        Whether to print the full historical and conceptual explanation.
    """

    if show_explanation:
        print("""\
Title: Hilbert's Program and Its Collapse

David Hilbert (1862–1943) envisioned placing all of mathematics on a perfectly solid foundation.
His program, outlined in the early 20th century, had three central goals:

1. Consistency:
   The axioms must not produce contradictions. No statement should be both provable and disprovable.

2. Completeness:
   Every true statement expressible in the system's language should be provable from its axioms.

3. Decidability (Entscheidungsproblem):
   There should exist a finite mechanical procedure (algorithm) to decide the truth or falsehood
   of any statement in the system.

---------------------------------------------------
How It Was Challenged and Eventually Debunked
---------------------------------------------------

1. Gödel's First Incompleteness Theorem (1931):
   - Kurt Gödel proved that in any consistent formal system capable of expressing basic arithmetic,
     there exist true statements that cannot be proven within the system.
   - This shattered the goal of **completeness**: no matter how many axioms you add, there will
     always be unprovable truths.

2. Gödel's Second Incompleteness Theorem (1931):
   - He further showed that such a system cannot prove its own consistency (unless it is inconsistent).
   - This undermined Hilbert’s dream of proving **consistency** purely from within the system.

3. The Entscheidungsproblem and Computability (1936):
   - Alonzo Church and Alan Turing independently proved there is no general algorithm
     to decide the truth of every mathematical statement.
   - This resolved Hilbert’s **decidability** goal in the negative, showing that mathematics
     is not fully mechanizable.

4. Aftermath:
   - Hilbert’s optimism (“Wir müssen wissen, wir werden wissen” — “We must know, we will know”)
     inspired decades of research, but the dream of a perfect, complete, and decidable
     foundation for mathematics was proven impossible.
   - Modern mathematics instead embraces axiomatic systems knowing they are incomplete,
     using separate consistency proofs relative to stronger systems, and accepting the limits
     of algorithmic decision-making.

Summary:
    - Goal 1 (Consistency): Cannot be proven internally if the system is strong enough.
    - Goal 2 (Completeness): Impossible — there will always be undecidable truths.
    - Goal 3 (Decidability): Impossible — no universal decision algorithm exists.
""")


def buffons_needle():
    """
    Buffon's Needle — Estimating π Using Probability

    Buffon's Needle is a famous probability problem proposed by Georges-Louis Leclerc, Comte de Buffon in the 18th century.
    It provides a surprising way to estimate the value of π using a simple physical experiment involving dropping a needle 
    onto a plane ruled with parallel lines.

    -------------------------------------
    The Setup:
    -------------------------------------
    - You have a floor with parallel lines spaced `d` units apart.
    - You randomly drop a needle of length `l` (where l <= d) onto the floor.
    - You observe whether the needle crosses a line or not.

    -------------------------------------
    The Probability:
    -------------------------------------
    The probability `P` that the needle crosses a line is:

        P = (2 * l) / (π * d)

    Rearranging the formula gives an approximation of π:

        π ≈ (2 * l * N) / (d * H)

    Where:
    - `N` is the total number of needle drops
    - `H` is the number of times the needle crosses a line

    -------------------------------------
    Why It Works:
    -------------------------------------
    The probability comes from integrating over all possible orientations and positions of the needle. The result is 
    directly tied to π because the probability involves averaging over angles (from trigonometric terms like sin(θ)), 
    and circular functions always bring π into play.

    -------------------------------------
    A Monte Carlo Simulation Approach:
    -------------------------------------
    Buffon's Needle is one of the earliest known problems to use random sampling to estimate a constant — a technique 
    central to Monte Carlo simulations.

    -------------------------------------
    Example Application:
    -------------------------------------
    Suppose:
    - Needle length `l = 1 unit`
    - Line spacing `d = 2 units`
    - 1000 needle drops
    - Needle crosses a line 318 times

    Then:
        π ≈ (2 * 1 * 1000) / (2 * 318) = 1000 / 318 ≈ 3.144

    -------------------------------------
    Key Insights:
    -------------------------------------
    - This problem beautifully links geometry, probability, and the value of π.
    - It's an example of **geometric probability** — where randomness is connected to shape and measurement.
    - Demonstrates how **randomness can lead to accurate constants** if averaged over enough trials.
    """
    pass

def eigenfunctions_eigenvalues(*, show_explanation=True):
    """
    Explains eigenfunctions and eigenvalues, their mathematical foundation,
    physical significance in quantum mechanics, and applications across science and engineering.
    
    Parameters
    ----------
    show_explanation : bool, default True
        Whether to print the theoretical explanation.
    """
    if show_explanation:
        print("""\
Title: Eigenfunctions & Eigenvalues — The Hidden Architecture of Physical Systems
–––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
1. What Are Eigenfunctions and Eigenvalues?
–––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
Eigenfunctions are special functions that, when operated upon by a linear operator,
return themselves multiplied by a constant:

**The Eigenvalue Equation:**
L̂ψ(x) = λψ(x)

Where:
- L̂ = Linear operator (differential, integral, matrix)
- ψ(x) = Eigenfunction (the special function)
- λ = Eigenvalue (the scaling constant)

> "Eigenfunctions are the natural modes of a system — the patterns that maintain 
>  their shape under the system's fundamental operation."
–––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
2. The Physical Intuition
Think of eigenfunctions as the **natural resonance patterns** of a system:

**Vibrating String Example:**
- **Operator:** d²/dx² (second derivative)
- **Eigenfunctions:** sin(nπx/L) (standing wave patterns)
- **Eigenvalues:** -(nπ/L)² (frequency-related constants)

**What This Means:**
Each eigenfunction represents a **pure mode** where the entire system oscillates
in a single, well-defined pattern. The eigenvalue tells us the **characteristic
frequency** or **energy** of that mode.
–––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
3. Quantum Mechanical Foundation
**Time-Independent Schrödinger Equation:**
Ĥψ(x) = Eψ(x)

Where:
- Ĥ = Hamiltonian operator (total energy operator)
- ψ(x) = Wave function (probability amplitude)
- E = Energy eigenvalue

**Physical Interpretation:**
- **Eigenfunctions ψ_n(x):** Allowed quantum states
- **Eigenvalues E_n:** Allowed energy levels
- **Quantization:** Only discrete energies are possible

**The Miracle:**
Nature chooses these **special functions** as the building blocks of reality!
–––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
4. Classic Examples Across Physics

**Particle in a Box:**
- **Operator:** -ℏ²/(2m) d²/dx²
- **Eigenfunctions:** ψ_n(x) = √(2/L) sin(nπx/L)
- **Eigenvalues:** E_n = n²π²ℏ²/(2mL²)
- **Physics:** Electron confined in a quantum well

**Harmonic Oscillator:**
- **Operator:** -ℏ²/(2m) d²/dx² + (1/2)mω²x²
- **Eigenfunctions:** ψ_n(x) ∝ H_n(√(mω/ℏ)x) e^(-mωx²/(2ℏ))
- **Eigenvalues:** E_n = ℏω(n + 1/2)
- **Physics:** Molecular vibrations, quantum field theory

**Hydrogen Atom:**
- **Operator:** -ℏ²/(2m)∇² - ke²/r
- **Eigenfunctions:** ψ_nlm(r,θ,φ) = R_nl(r)Y_l^m(θ,φ)
- **Eigenvalues:** E_n = -13.6 eV/n²
- **Physics:** Atomic orbitals, electron clouds
–––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
5. Mathematical Properties of Eigenfunctions

**Orthogonality:**
∫ ψ_m*(x) ψ_n(x) dx = δ_mn

**Completeness:**
Any function can be expanded as: f(x) = Σ_n c_n ψ_n(x)

**Normalization:**
∫ |ψ_n(x)|² dx = 1

**What This Means:**
- Different eigenstates are **perpendicular** in function space
- Eigenfunctions form a **complete basis** set
- You can build **any function** from eigenfunction combinations
- They provide the **natural coordinate system** for the problem
–––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
6. The Superposition Principle
**General Solution:**
Ψ(x,t) = Σ_n c_n ψ_n(x) e^(-iE_n t/ℏ)

**Physical Meaning:**
- **c_n:** Probability amplitudes for each eigenstate
- **|c_n|²:** Probability of measuring eigenvalue E_n
- **Time Evolution:** Each eigenstate oscillates with its own frequency

**Quantum Coherence:**
When multiple eigenstates are present, they can **interfere** constructively
or destructively, creating **quantum superposition** effects.
–––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
7. Computational Methods

**Matrix Diagonalization:**
For finite systems: Hc = λc (matrix eigenvalue problem)

**Shooting Methods:**
For differential equations with boundary conditions

**Variational Methods:**
Approximate eigenfunctions by minimizing energy functionals

**Perturbation Theory:**
Find corrections to known eigenvalues/eigenfunctions

**Numerical Integration:**
Solve eigenvalue ODEs/PDEs using finite difference/element methods
–––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
8. Applications Beyond Quantum Mechanics

**Engineering Vibrations:**
- **Bridge modes:** Eigenfrequencies prevent resonance disasters
- **Mechanical systems:** Normal modes of oscillation
- **Structural analysis:** Finding natural frequencies

**Signal Processing:**
- **Fourier modes:** e^(iωt) are eigenfunctions of d/dt
- **Principal Component Analysis:** Eigenvectors of covariance matrices
- **Image compression:** Using eigenfunction bases

**Heat Transfer:**
- **Separation of variables:** Spatial eigenfunctions × time evolution
- **Cooling patterns:** Temperature profiles follow eigenfunction shapes

**Chemical Bonding:**
- **Molecular orbitals:** Linear combinations of atomic eigenfunctions
- **Band theory:** Electronic eigenstates in crystals
–––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
9. The Deep Connection: Symmetry and Degeneracy

**Symmetry Principle:**
Systems with **symmetry** often have **degenerate eigenvalues**
(multiple eigenfunctions with the same eigenvalue)

**Examples:**
- **Spherical symmetry:** Hydrogen atom has degenerate l,m states
- **Translation symmetry:** Plane waves in free space
- **Rotation symmetry:** Angular momentum eigenstates

**Group Theory Connection:**
Eigenfunction **transformation properties** reflect the system's **symmetry group**.
This deep connection explains why certain patterns appear repeatedly in nature.
–––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
10. Eigenvalues as Nature's Selection Rules

**Energy Quantization:**
Only eigenvalue energies are **allowed** — all others are **forbidden**

**Selection Rules:**
Transitions between eigenstates follow **strict quantum rules**:
- Conservation laws determine allowed transitions
- Symmetry constrains which states can mix
- Eigenfunction overlap determines transition probabilities

**Physical Reality:**
- **Atomic spectra:** Only certain photon energies are emitted/absorbed
- **Molecular bonds:** Only specific vibrational/rotational states exist  
- **Solid state:** Electronic bands determine conductivity

> "Eigenvalues are nature's way of saying: 'These are the only options available.'"
–––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
11. The Measurement Connection

**Born Rule:**
|⟨ψ_n|Ψ⟩|² = Probability of measuring eigenvalue λ_n

**Measurement Process:**
1. **Before:** System in superposition Ψ = Σ c_n ψ_n
2. **Measurement:** Operator L̂ is applied
3. **After:** System **collapses** to eigenstate ψ_n with probability |c_n|²

**Fundamental Insight:**
**Eigenfunctions are the states of definite measurement outcomes.**
All other states are **probabilistic mixtures** of these fundamental states.
–––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
12. Summary: Eigenfunctions as Nature's Fundamental Language

**Mathematical Elegance:**
- Transform complex differential equations into simple algebraic relations
- Provide natural coordinate systems for physical problems
- Reveal hidden symmetries and conservation laws

**Physical Significance:**
- Define the **allowed states** of quantum systems
- Determine **measurable quantities** and their probabilities  
- Explain **quantization** phenomena across all scales

**Universal Applicability:**
- Quantum mechanics → Wave mechanics → Classical vibrations
- Same mathematical framework applies from atoms to bridges
- Connect **discrete mathematics** (eigenvalues) with **continuous physics**

> "Eigenfunctions are the alphabet with which nature writes the book of physics —
>  every physical system speaks this fundamental mathematical language."

> "In the symphony of the universe, eigenfunctions are the pure notes,
>  and eigenvalues are their frequencies."

"To understand eigenfunctions is to glimpse the mathematical DNA
 that underlies all of physical reality."
                                                    ~Mathematical Physics Legacy
""")



def schwarz_inequality(*, show_explanation=True):
    """
    Explains the Cauchy-Schwarz Inequality — a fundamental result in linear algebra and analysis
    that relates the inner product of two vectors to the product of their norms.
    
    Parameters
    ----------
    show_explanation : bool, default True
        Whether to print the theoretical explanation.
    """
    if show_explanation:
        print("""\
Title: Cauchy-Schwarz Inequality — A Cornerstone of Inner Product Spaces
–––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
1. What Is the Cauchy-Schwarz Inequality?
–––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
The **Cauchy-Schwarz Inequality** (also known as the **Schwarz Inequality**) states:
> For any two vectors u and v in an inner product space:
  |⟨u, v⟩| ≤ ||u|| · ||v||

Where:
✓ ⟨u, v⟩ is the **inner product** (dot product in Euclidean space)
✓ ||u|| and ||v|| are the **norms** (lengths) of the vectors
✓ Equality holds **if and only if** u and v are linearly dependent (one is a scalar multiple of the other)

This inequality bounds how large the inner product can be relative to the vectors' magnitudes.

–––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
2. Geometric Interpretation
–––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
In Euclidean space, the inner product can be written as:
  ⟨u, v⟩ = ||u|| · ||v|| · cos(θ)

where θ is the angle between the vectors.

Since |cos(θ)| ≤ 1, we get:
  |⟨u, v⟩| = ||u|| · ||v|| · |cos(θ)| ≤ ||u|| · ||v||

**Key insight**: The inequality states that the projection of one vector onto another
cannot exceed the product of their lengths.

–––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
3. Forms of the Inequality
–––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
**Euclidean Space (ℝⁿ):**
  |u₁v₁ + u₂v₂ + ... + uₙvₙ| ≤ √(u₁² + u₂² + ... + uₙ²) · √(v₁² + v₂² + ... + vₙ²)

**Integral Form (L² space):**
  |∫ f(x)g(x) dx| ≤ √(∫ f²(x) dx) · √(∫ g²(x) dx)

**Probabilistic Form:**
  |E[XY]| ≤ √(E[X²]) · √(E[Y²])
  
This generalizes to any inner product space with an appropriate definition of inner product.

–––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
4. Why Is It Important?
–––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
The Cauchy-Schwarz Inequality is foundational because:

✓ **Proves the triangle inequality** — enables definition of distance metrics
✓ **Establishes convergence properties** in analysis and functional analysis
✓ **Derives correlation bounds** in probability and statistics
✓ **Underpins optimization theory** and numerical methods
✓ **Used in quantum mechanics** — through the uncertainty principle

It's one of the most widely used inequalities in mathematics.

–––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
5. Proof Sketch (Algebraic Approach)
–––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
Consider the squared norm of (u - tv) for any scalar t:
  ||u - tv||² ≥ 0

Expanding:
  ⟨u - tv, u - tv⟩ = ||u||² - 2t⟨u, v⟩ + t²||v||² ≥ 0

This is a quadratic in t that's always non-negative. For this to hold, the discriminant must satisfy:
  4⟨u, v⟩² - 4||u||²||v||² ≤ 0

Simplifying gives:
  |⟨u, v⟩|² ≤ ||u||² · ||v||²

Taking square roots yields the Cauchy-Schwarz Inequality.

–––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
6. Applications Across Mathematics
–––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
✓ **Linear Algebra**: Proving orthogonality properties and matrix inequalities
✓ **Statistics**: Bounding correlation coefficients (|ρ| ≤ 1)
✓ **Signal Processing**: Establishing energy bounds and filter properties
✓ **Machine Learning**: Kernel methods, feature space analysis
✓ **Optimization**: Convex analysis and duality theory
✓ **Physics**: Heisenberg uncertainty principle, wave mechanics

–––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
7. Related Inequalities
–––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
The Cauchy-Schwarz Inequality belongs to a family of important inequalities:

→ **Triangle Inequality**: ||u + v|| ≤ ||u|| + ||v|| (follows from Cauchy-Schwarz)
→ **Hölder's Inequality**: A generalization to Lᵖ spaces
→ **Minkowski's Inequality**: Another generalization for norms

–––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
8. Summary: A Universal Bound
–––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
- The Cauchy-Schwarz Inequality bounds the **inner product by the product of norms**
- It holds in **any inner product space** — Euclidean, function spaces, probability spaces
- Equality occurs **only when vectors are linearly dependent**
- It's a **fundamental tool** across pure and applied mathematics
- Enables rigorous definitions of **angles, distances, and correlations**

> "The Cauchy-Schwarz Inequality reveals the geometric constraint that inner products 
  can never exceed what the vectors' magnitudes allow."
""")
