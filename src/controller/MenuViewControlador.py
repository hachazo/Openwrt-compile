import sys
import threading

import pygame

from controller.ControladorABM import ControllerABM
from controller.GameOverViewControlador import GameOverViewControlador
from controller.JugarViewControlador import JugarController
from controller.OpcionesViewControlador import OpcionesController
from controller.RankingViewControlador import RankingController
from settings import SCREEN
from view.MenuView import MenuView
from view.VistaABM import LoginView
from controller.MiembrosController import MiembrosController

from .Controlador import Controlador


class MenuController(Controlador):
    def __init__(self):
        super().__init__()
        self._view = MenuView(SCREEN)  # dificultad predeterminada#
        self.__ranking = RankingController()
        self.__opciones = OpcionesController()
        self.__controlador_abm = ControllerABM()
        self.__jugar = JugarController()
        self.__miembros = MiembrosController()

    def manejar_eventos(self, eventos, mouse_pos):
        botones = self._view.get_botones()
        for event in eventos:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if botones["login"].checkForInput(mouse_pos):
                    app = LoginView(self.__controlador_abm)
                    threading.Thread(target=app.mainloop(), daemon=True).start()
                if botones["jugar"].checkForInput(mouse_pos):
                    self._view.ocultar_visibilidad()
                    self.__jugar.main_loop()
                if botones["opciones"].checkForInput(mouse_pos):
                    self._view.ocultar_visibilidad()
                    self.__opciones.main_loop()
                if botones["ranking"].checkForInput(mouse_pos):
                    self._view.ocultar_visibilidad()
                    self.__ranking.main_loop()
                if botones["salir"].checkForInput(mouse_pos):
                    pygame.quit()
                    sys.exit()
                if botones["miembros"].checkForInput(mouse_pos):
                    self._view.ocultar_visibilidad()
                    self.__miembros.main_loop()
