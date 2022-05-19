import clingo

from typing import Any, List
from .evaluator import EvaluatorContainer
from .model import *



class Solver:
    ctls = {
        "clingo": clingo.Control
    }

    def __init__(self, function: str, argument: Any, encoding: List[List[str]], instance: List[str], folder: str = ""):
        self.function = function
        self.argument = argument
        self.encoding = encoding + instance
        self.folder = folder

    def from_json(json):
        if not 'instance' in json:
            instance = []
        else:
            instance = json['instance']
        solver = Solver(function=json['function'],
                        argument=json['argument'],
                        encoding=json['encoding'],
                        instance=instance,
                        folder=json['folder'])
        return solver

    def prepare_ctl(self):
        try:
            ctl = self.ctls[self.function](self.argument)
        except:
            raise "Control object not recognized"

        for p in self.encoding:
            ctl.load(self.folder + p)
        ctl.ground([("base", [])])
        return ctl

    def run(self, ec:EvaluatorContainer) -> EvaluatorContainer:
        ctl = self.prepare_ctl()
        ctl.solve(on_model=ec.on_model, on_finish=ec.on_finish)
        return ec

    def __str__(self):
        ret = f"{self.function}, arguments : '{str(self.argument)}', encodings : {str(self.encoding)}\n"
        return ret