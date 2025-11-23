Quantum Logic Gates (Python)

Overview
This repository contains a tiny Python module that models classical/boolean-style logic gates acting on bitstring indices alongside matrices for common quantum gates. It provides:
- quantum.py: Matrix definitions for single-, two-, and three-qubit quantum gates (X, Y, Z, H, S, T, Rx, Ry, Rz, CNOT, CZ, CY, SWAP, CCNOT) and small helper functions to inspect/flip bit indices.
- normal.py: A convenience class Gates that applies classical-style boolean operations (NOT, AND, OR, IMPLY, XOR, NOR, NAND, NIMPLY, XNOR) to a full state vector by permuting amplitudes based on bit indices.

The code is self-contained and minimal, suitable for experimentation or as a teaching aid for representing gates and operating on small state vectors using NumPy.


Stack and Requirements
- Language: Python (tested with 3.x; no explicit version pinning here)
- Libraries: NumPy
- Package manager: None required (no Poetry/Pipenv/Conda files present). Use pip.

Minimum requirements
- Python 3.9+ (recommended; earlier 3.x may also work)
- pip (to install NumPy)


Installation and Setup
1) Create and activate a virtual environment (recommended)
   - macOS / Linux:
     python3 -m venv .venv
     source .venv/bin/activate
   - Windows (PowerShell):
     python -m venv .venv
     .\.venv\Scripts\Activate.ps1

2) Install dependencies
   pip install numpy


How to Run / Use
There is no command-line entry point or app runner in this repository. Import the modules in Python and call the classes/functions directly.

Example: using boolean-style gates on a 3-qubit state vector (size 8)
```python
import numpy as np
from normal import Gates

# Start in basis state |110> (index 6) with amplitude 1
state = np.zeros(8, dtype=complex)
state[6] = 1.0

# Apply XOR between q0 and q1, flipping target q2
new_state = Gates.XOR(state, q1_idx=0, q2_idx=1, target_idx=2)
print(np.nonzero(new_state)[0])  # shows the new index where amplitude moved
```

Example: using quantum gate matrices directly
```python
import numpy as np
from quantum import QuantumGates as Q

# Single-qubit |0> state
zero = np.array([1, 0], dtype=complex)

# Apply Hadamard: H|0> = (|0> + |1>) / sqrt(2)
psi = Q.H @ zero
print(psi)
```


Entry Points and Scripts
- Entry points: None (library-style modules only)
- Scripts: None provided

TODO:
- Consider adding a small CLI or examples script (e.g., examples/run_demo.py) to showcase operations.


Environment Variables
No environment variables are currently used.

TODO:
- Document any future configuration via env vars if added.


Tests
There are no automated tests included in this repository at the moment.

TODO:
- Add unit tests (e.g., with pytest) to verify gate behavior and state transformations.


Project Structure
.
├── LICENSE
├── normal.py   # Boolean-style gate operations over state vectors using NumPy
└── quantum.py  # Quantum gate matrices and helper functions (get_value, flip)


Notable APIs
- quantum.QuantumGates
  - Constants: X, Y, Z, H, S, T, CNOT, CZ, CY, SWAP, CCNOT, I2, I4, I8
  - Functions: Rx(theta), Ry(theta), Rz(theta), get_value(idx, q_idx), flip(idx, target_idx)

- normal.Gates
  - Functions: NOT(state, target_idx), AND(state, q1_idx, q2_idx, target_idx), OR(...), IMPLY(...), XOR(...), NOR(...), NAND(...), NIMPLY(...), XNOR(...)

Notes and Limitations
- The boolean-style gate functions in normal.py operate by permuting amplitudes of a full state vector. They expect the state to be sized as 2^n for n qubits and do not validate dimensions rigorously.
- No tensor-product composition helpers or multi-qubit layout utilities are provided; indices are assumed to refer to bit positions in the basis index.
- This project does not include a simulator for applying arbitrary unitary matrices to multi-qubit states; only minimal examples are shown.


License
This project is distributed under the terms of the license in the LICENSE file at the repository root.


Changelog
- 2025-11-23: Added README with overview, usage, and TODOs.
