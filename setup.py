from setuptools import setup, find_packages

def read_readme():
    try:
        with open("README.md", "r", encoding="utf-8") as fh:
            return fh.read()
    except FileNotFoundError:
        return "A comprehensive physics library providing constants, equations, and formulas."

def read_requirements():
    try:
        with open("requirements.txt", "r", encoding="utf-8") as f:
            return [
                line.strip() for line in f
                if line.strip() and not line.startswith("#")
            ]
    except FileNotFoundError:
        return ["numpy>=1.19.0", "scipy>=1.7.0", "matplotlib>=3.3.0"]

setup(
    name="fphysics",
    version="1.0",
    author="Shakee",
    description="A comprehensive physics library providing constants, equations, and formulas",
    long_description=read_readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/n0sync/fphysics",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Science/Research",
        "Intended Audience :: Education",
        "Topic :: Scientific/Engineering :: Physics",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
    install_requires=read_requirements(),
    include_package_data=True,
    keywords=[
        "physics", "science", "constants", "equations", "mechanics",
        "quantum", "thermodynamics", "electromagnetism", "optics",
        "waves", "cosmology", "astrophysics", "biophysics",
        "plasma physics", "heat transfer", "laws of physics",
        "kinematics", "dynamics", "energy", "momentum",
        "scientific computing", "numerical methods", "STEM"
    ],
)
