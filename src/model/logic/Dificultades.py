from abc import ABC,abstractmethod

class Dificultad(ABC):
    def __init__(self) -> None:
        super().__init__()
        self._probabilidad=100
    
    @abstractmethod
    def get_mensaje(self):
        pass
    
    @abstractmethod
    def get_probabilidad(self):
        pass
    
    @abstractmethod
    def get_pts_por_ganar(self):
        pass
    
    def get_pts_por_empatar(self):
        return 1
    
    def get_pts_por_perder(self):
        return 0

class Facil(Dificultad):
    
    def get_mensaje(self):
        return f'reparto de puntos (FACIL):\n victoria (+ {self.get_pts_por_ganar()}pts) ;empate (+ {self.get_pts_por_empatar()}pts);derrota ({self.get_pts_por_perder()}pts)'
    def get_probabilidad(self):
        return int(self._probabilidad * 0.8)
    
    def get_pts_por_ganar(self):
        return 3

class Medio(Dificultad):
    
    def get_mensaje(self):
        return f'reparto de puntos (MEDIO):\n victoria (+ {self.get_pts_por_ganar()}pts) ;empate (+ {self.get_pts_por_empatar()}pts);derrota ({self.get_pts_por_perder()}pts)'
    def get_probabilidad(self):
        return int(self._probabilidad * 1)
    
    def get_pts_por_ganar(self):
        return 4

class Dificil(Dificultad):
    def get_mensaje(self):
        return f'reparto de puntos (DIFICIL):\n victoria (+ {self.get_pts_por_ganar()}pts) ;empate (+ {self.get_pts_por_empatar()}pts);derrota ({self.get_pts_por_perder()}pts)'
    
    def get_probabilidad(self):
        return int(self._probabilidad * 1.5)
    
    def get_pts_por_ganar(self):
        return 6
    
    def get_pts_por_empatar(self):
        return 2
