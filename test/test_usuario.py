# Bueno nada por aqui
import unittest
import usuario

class UsuarioTest(unittest.TestCase):

    def TestSaludarDeberiaDevolverHola(self):
        #AAA

        #ARRANGE
        saludoesperado = usuario.saludar()

        #ACT
        saludoRecibido = usuario.saludar()

        #ASSERT
        self.assertEquals(saludoesperado, saludoRecibido)

