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
