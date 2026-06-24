from .dpll_solver import AVOIDER_34, aps, coloring_valid, cnf, write_dimacs, dpll_unsat, verify

def main():
    import json
    from pathlib import Path
    Path("receipts").mkdir(exist_ok=True)
    write_dimacs(35, "receipts/w24_upper_bound.cnf")
    r = verify()
    Path("receipts/w24_native_dpll_unsat_receipt.json").write_text(json.dumps(r, indent=2), encoding="utf-8")
    print(json.dumps(r, indent=2))
    raise SystemExit(0 if r["status"] == "PASS" else 1)

if __name__ == "__main__":
    main()
