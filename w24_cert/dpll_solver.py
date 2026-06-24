import json
from pathlib import Path

AVOIDER_34 = "0101110001001011100010010111000101"

def aps(n, k=4):
    out = []
    for a in range(1, n + 1):
        d = 1
        while a + (k - 1) * d <= n:
            out.append(tuple(a + i * d for i in range(k)))
            d += 1
    return out

def coloring_valid(col, k=4):
    d = {i + 1: int(c) for i, c in enumerate(col)}
    for ap in aps(len(col), k):
        vals = [d[x] for x in ap]
        if all(v == vals[0] for v in vals):
            return False
    return True

def cnf(n, k=4):
    clauses = []
    for ap in aps(n, k):
        clauses.append(tuple(ap))
        clauses.append(tuple(-x for x in ap))
    clauses.append((-1,))
    return tuple(clauses)

def write_dimacs(n, path):
    clauses = cnf(n)
    with open(path, "w", encoding="utf-8") as f:
        f.write(f"p cnf {n} {len(clauses)}\\n")
        for cl in clauses:
            f.write(" ".join(map(str, cl)) + " 0\\n")
    return len(clauses)

def simplify(clauses, lit):
    new = []
    neg = -lit
    for cl in clauses:
        if lit in cl:
            continue
        if neg in cl:
            c = tuple(x for x in cl if x != neg)
            if not c:
                return None
            new.append(c)
        else:
            new.append(cl)
    return tuple(new)

def dpll_unsat(n=35):
    clauses = cnf(n)
    nodes = 0
    def rec(clauses):
        nonlocal nodes
        nodes += 1
        if not clauses:
            return True
        while True:
            units = [cl[0] for cl in clauses if len(cl) == 1]
            if not units:
                break
            for u in units:
                clauses = simplify(clauses, u)
                if clauses is None:
                    return False
                if not clauses:
                    return True
        counts = {}
        for cl in clauses:
            weight = 10 - len(cl)
            for lit in cl:
                counts[abs(lit)] = counts.get(abs(lit), 0) + weight
        var = max(counts, key=counts.get)
        for lit in (var, -var):
            reduced = simplify(clauses, lit)
            if reduced is not None and rec(reduced):
                return True
        return False
    sat = rec(clauses)
    return {"n": n, "clause_count": len(clauses), "ap_count": len(aps(n)), "symmetry_break": "x1=0", "sat": sat, "unsat": not sat, "dpll_nodes": nodes, "truth_label": "NATIVE_DPLL_UNSAT_RECEIPT_NOT_EXTERNAL_SOLVER"}

def verify():
    lower = coloring_valid(AVOIDER_34)
    upper = dpll_unsat(35)
    return {"theorem": "W(2,4)=35", "n34_avoider_verified": lower, "n34_avoider": AVOIDER_34, "n35_native_dpll": upper, "external_cadical_log_included": False, "c4_external_solver_status": "PENDING_CADICAL_DRAT_FRAT_LOG", "status": "PASS" if lower and upper["unsat"] else "FAIL"}
