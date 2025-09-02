# A collection of fascinating math theories that I find intriguing and worth exploring.
# Mentions: Most of these concepts were inspired by videos from Veritasium, 3Blue1Brown.



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
