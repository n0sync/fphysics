# fphysics — A Comprehensive Physics Library in Python

**fphysics** is a Python library that offers an extensive collection of physical constants, equations, and formulas.  

## Key Features

### Constants Database
Includes essential physical constants — SI base units, quantum constants, astronomical parameters, and more.

### Modular Formula Collections
Separate modules for mechanics, thermodynamics, electromagnetism, atomic physics, nuclear physics, relativity, statistical mechanics, and beyond.

### Unit Conversion 
Convert seamlessly between SI, CGS, and natural units.

### Built for Learning 
Perfect for integration into scientific calculators, simulations and teaching aids.

## Installation
Install directly from PyPI:

```bash
pip install fphysics
```

## Quick Start
```python
import fphysics as fp
from fphysics.relativity.general import schwarzschild_radius
from fphysics.thermodynamics.heat_engines import carnot_efficiency

# Access fundamental constants
print(fp.constants.SPEED_OF_LIGHT)   

# Calculate Schwarzschild radius
print(schwarzschild_radius(10))

#Calulate the Carnot Efficiency
print(carnot_efficiency(500, 300))
```

## Contributing

I welcome all contributions — from adding new formulas to refining documentation.

1. **Fork** the repository
2. **Create** a feature branch
3. **Submit** a pull request
4. **Report** issues or suggest enhancements

## Links

**PyPI**: https://pypi.org/project/fphysics

## License

MIT License - see [LICENSE](LICENSE) file for details.
