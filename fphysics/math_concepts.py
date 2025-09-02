# A collection of fascinating math theories that I find intriguing and worth exploring.
# Mentions: Most of these concepts were inspired by videos from Veritasium, 3Blue1Brown.

import cmath



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
