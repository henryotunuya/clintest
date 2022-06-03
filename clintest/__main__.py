if __name__ == "__main__":
    # TODO

    import colorama
    colorama.init()

    from .assessment import Any, All, Not, Sat, Unsat
    from .solver import Clingo

    assessment = Not(All([Any([Sat(), Unsat()])]))

    solver = Clingo(arguments=["0"], program=":-.")
    solver.solve(assessment)

    print(solver)
    print()
    print(assessment)
