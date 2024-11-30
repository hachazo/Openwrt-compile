import pygame


class Boton:
    def __init__(self, image, pos, text_input, font, base_color, hovering_color):
        self.imagen = image
        self.x_pos = pos[0]
        self.y_pos = pos[1]
        self.fuente = font
        self.color_base, self.hovering_color = base_color, hovering_color
        self.texto_input = text_input
        self.texto = self.fuente.render(self.texto_input, True, self.color_base)
        if self.imagen is None:
            self.imagen = self.texto
        self.rect = self.imagen.get_rect(center=(self.x_pos, self.y_pos))
        self.text_rect = self.texto.get_rect(center=(self.x_pos, self.y_pos))
        self.clickeado = False
        self.seleccionado = False
        self.hovering = False

    def update(self, screen):
        if self.imagen is not None:
            pygame.transform.scale(self.imagen, self.text_rect.size)
            screen.blit(self.imagen, self.rect)
        screen.blit(self.texto, self.text_rect)

    def checkForInput(self, posicion) -> bool:
        accionado = False
        if self.rect.collidepoint(posicion):
            if pygame.mouse.get_pressed()[0] == 1 and self.clickeado == False:
                self.clickeado = True
                accionado = True
            if pygame.mouse.get_pressed()[0] == 0:
                self.clickeado = False
        return accionado

    def changeColor(self, posicion = (-1,-1)):
        if posicion[0] in range(self.rect.left, self.rect.right) and posicion[1] in range(self.rect.top, self.rect.bottom):
            self.texto = self.fuente.render(self.texto_input, True, self.hovering_color)
            self.hovering = True
    
        else:
            self.texto = self.fuente.render(self.texto_input, True, self.color_base)
            self.hovering = False
    'el hovering lo puse para probar, si no me funciona lo que quier hacer lo borro - leo'
    
    def mantener_color(self):
        if self.seleccionado:
            self.texto = self.fuente.render(self.texto_input, True, self.hovering_color)
        
    
    def seleccionar(self):
        self.seleccionado = True
   
        
    def deseleccionar (self):
        self.seleccionado = False
   


