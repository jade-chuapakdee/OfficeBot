from pyswip import Prolog

class MyProlog:
    def __init__(self) -> None:
        self._prolog = Prolog()
        self._prolog.consult('prolog/my_bellman.pl')

    def getPrologInstance(self):
        return self._prolog

    def getPath(self, src, des):
        result = list(self._prolog.query(f'bf(5, {src}, {des}, Cost, Path)'))
        print(f'From {src} to {des}: {result}')
        return result[0]['Path']