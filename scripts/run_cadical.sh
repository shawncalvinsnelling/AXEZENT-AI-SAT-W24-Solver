#!/usr/bin/env bash
set -euo pipefail
mkdir -p receipts
python -m w24_cert.verifier
cadical receipts/w24_upper_bound.cnf > receipts/w24_upper_bound_cadical.log
