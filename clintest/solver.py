from abc import ABC, abstractmethod
from typing import Optional, Sequence

from clingo.control import Control

from .test import Test


class Solver(ABC):
    @abstractmethod
    def solve(self, test: Test) -> None:
        pass


class Clingo(Solver):
    def __init__(
        self,
        arguments: Optional[Sequence[str]] = None,
        program: Optional[str] = None,
        files: Optional[Sequence[str]] = None,
    ) -> None:
        self.__arguments = [] if arguments is None else arguments
        self.__program = "" if program is None else program
        self.__files = [] if files is None else files

    def solve(self, test: Test) -> None:
        ctl = Control(self.__arguments)

        ctl.add("base", [], self.__program)

        for file in self.__files:
            ctl.load(file)

        ctl.ground([("base", [])])

        if not test.outcome().is_certain():
            ctl.solve(
                on_model=test.on_model,
                on_unsat=test.on_unsat,
                on_core=test.on_core,
                on_statistics=test.on_statistics,
                on_finish=test.on_finish,
            )
