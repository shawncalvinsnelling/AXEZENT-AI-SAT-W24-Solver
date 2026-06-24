from w24_cert.dpll_solver import coloring_valid, AVOIDER_34, cnf, dpll_unsat

def test_avoider34():
    assert coloring_valid(AVOIDER_34)

def test_cnf():
    assert len(cnf(35)) == 375

def test_native_dpll_unsat():
    r = dpll_unsat(35)
    assert r["unsat"] is True
    assert r["sat"] is False
