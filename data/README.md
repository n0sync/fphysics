# Data directory

This directory stores project datasets and reference files used by pysics. It is organized into the following subfolders:

- materials/  
  Material property databases, such as density, elastic constants, thermal properties, optical constants, etc. Use open, citation-friendly formats (CSV, JSON, YAML). Include source and units in file headers/metadata.

- spectra/  
  Spectroscopic data (e.g., absorption/emission spectra, reflectance, Raman/IR, XRD patterns). Prefer columnar text formats (CSV/TSV) with metadata file or header block describing instrument, conditions, units, and preprocessing steps.

- reference/  
  General reference data used by models or examples (constants, calibration curves, lookup tables).

Guidelines
- Keep raw (immutable) datasets separate from processed derivatives; name with suffixes like _raw and _proc if both are stored.
- Include a README.md beside any complex dataset to document provenance, license, units, and schema.
- Prefer SI units and document any deviations explicitly.
- If files are large, consider linking to an external storage location and provide a fetch script, rather than committing megabyte-scale binaries.
- For tabular data, include a schema (columns, units, types) in a companion YAML/JSON file when practical.

Suggested file conventions
- materials/*.csv           # Tabular properties by material or phase
- materials/*.json|yaml     # Structured property databases with units and citations
- spectra/*/*.csv           # One file per spectrum with wavelength/frequency column and intensity columns
- reference/*.csv|json      # Reference constants or tables

Versioning and integrity
- Track data changes with clear commit messages describing edits and sources.
- If you regenerate processed data, include the generating script/notebook path and git commit of the code.

Licensing
- Ensure data licensing permits redistribution. Include LICENSE or source link in a dataset-level README.

