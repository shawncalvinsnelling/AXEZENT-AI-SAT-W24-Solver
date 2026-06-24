# AXEZENT AI SAT W24 Solver

![AXEZENT AI Logo](assets/axezent-ai-logo.svg)

Finite verification scaffold for W(2,4)=35.

## Included

- n=34 avoider verification.
- n=35 DIMACS CNF generator.
- Native DPLL UNSAT receipt path.
- External CaDiCaL / DRAT / FRAT path.

## Truth boundary

```text
Native DPLL UNSAT receipt: included
External C4 solver proof log: pending until CaDiCaL/DRAT/FRAT log is committed
```

## Run

```bash
python -m pip install -e . pytest
python -m w24_cert.verifier
pytest -q
```
