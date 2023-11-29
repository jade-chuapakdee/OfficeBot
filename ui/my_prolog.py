import pyswip

class MyProlog:
    def __init__(self) -> None:
        self.prolog = pyswip.Prolog()
        self.prolog.consult('prolog/my_astar.pl')
    
    def getPathDetails(self, src, des):
        result = list(self.prolog.query(f'my_astar({src},{des},Path)'))
        return result[0]['Path']

if __name__ == '__main__':
    lmao = MyProlog()
    temp = lmao.getPathDetails('(9,1)','(0,2)')
    print(temp)