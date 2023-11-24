from pyswip import Prolog

class MyProlog:
    def __init__(self) -> None:
        self._prolog = Prolog()
        self._prolog.consult('prolog/my_bellman.pl') # This is for the production        
    
    def getPathDetails(self, src, des):
        result = list(self._prolog.query(f'bellman_ford(1, {src}, {des}, Cost, Path)'))[0]
        return result