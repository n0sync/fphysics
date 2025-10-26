# fphysics — A Comprehensive Physics Library in Python

**fphysics** (short for fun-physics) is a pure Python library that offers an extensive collection of physical constants, equations, and formulas.  
It's built as a one-stop toolkit for students, researchers, educators, and developers covering everything from classical mechanics to cutting-edge quantum theory.

## Key Features

### Extensive Constants Database
Includes essential physical constants — SI base units, quantum constants, astronomical parameters, and more.

### Modular & Well-Organized Formula Collections
Separate modules for mechanics, thermodynamics, electromagnetism, atomic physics, nuclear physics, relativity, statistical mechanics, and beyond.

### Unit Conversion Made Easy
Convert seamlessly between SI, CGS, and natural units.

### Built for Learning & Research
Perfect for integration into scientific calculators, simulations, teaching aids, or advanced research codebases.

## Installation
Install directly from PyPI:

```bash
pip install fphysics
```

## Quick Start
```python
import fphysics as fp
from fphysics.relativity.general import schwarzschild_radius
from fphysics import physics_concepts

# Access fundamental constants
print(fp.constants.speed_of_light)   # 299792458 m/s

# Calculate Schwarzschild radius
print(schwarzschild_radius(10))

# Access physics concepts and explanations
print(physics_concepts.P_vs_NP())
```

## Contributing

We welcome all contributions — from adding new formulas to refining documentation.

1. **Fork** the repository
2. **Create** a feature branch
3. **Submit** a pull request
4. **Report** issues or suggest enhancements

## Links

**PyPI**: https://pypi.org/project/fphysics

## License

MIT License - see [LICENSE](LICENSE) file for details.
