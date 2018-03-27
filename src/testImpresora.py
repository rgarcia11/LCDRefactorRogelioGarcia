"""
Pruebas para verificar que la impresora este funcionando bien.
"""
import unittest
from impresora import *

class TestAncho(unittest.TestCase):
    """
    Esta clase se encarga de hacer las pruebas unitarias
    para cada funcion de la impresora. Se probara que el ancho sea
    el deseado para cada funcion, cada digito (y varios digitos) y cada size.
    Los valores de size a probar son de 1 a 10.
    El ancho para un digito debe ser size+2.
    El ancho para varios digitos debe ser (size+2) * numero de digitos
    """
    def test_techo(self):
        """
        Prueba para el ancho del techo.
        """
        for size in range(1,11):
            for numero in todosLosDigitos:
                resultado = techo(size,numero)
                self.assertEqual(len(resultado),size+2,'En TestAncho > test_techo > probando con size: {} y numero: {}.'.format(size,numero))
            resultado = techo(size,todosLosDigitos)
            self.assertEqual(len(resultado),(size+2)*len(todosLosDigitos),'En TestAncho > test_techo > probando con size: {} y numero: {}.'.format(size,todosLosDigitos))


    def test_cuerpoSuperior(self):
        """
        Prueba para el ancho del cuerpo superior del digito.
        El numero de lineas generadas debe ser igual a size.
        Cada linea generada sigue las reglas establecidas.
        """
        for size in range(1,11):
            for numero in todosLosDigitos:
                resultado = cuerpoSuperior(size,numero)
                resultado = resultado.split('\n')
                self.assertEqual(len(resultado),size,'En TestAncho > test_cuerpoSuperior > probando son size: {} y numero: {}. Numero de lineas no es el esperado.'.format(size,numero))
                for r in resultado:
                    self.assertEqual(len(r),size+2,'En TestAncho > test_cuerpoSuperior > probando son size: {} y numero: {}.'.format(size,numero))
            resultado = cuerpoSuperior(size,todosLosDigitos)
            resultado = resultado.split('\n')
            self.assertEqual(len(resultado),size,'En TestAncho > test_cuerpoSuperior > probando son size: {} y numero: {}. Numero de lineas no es el esperado.'.format(size,todosLosDigitos))
            for r in resultado:
                self.assertEqual(len(r),(size+2)*len(todosLosDigitos),'En TestAncho > test_cuerpoSuperior > probando son size: {} y numero: {}.'.format(size,todosLosDigitos))

    def test_mitad(self):
        """
        Prueba para el ancho de la seccion de la mitad.
        """
        for size in range(1,11):
            for numero in todosLosDigitos:
                resultado = mitad(size,numero)
                self.assertEqual(len(resultado),size+2,'En TestAncho > test_mitad > probando con size: {} y numero: {}.'.format(size,numero))
        resultado = mitad(size,todosLosDigitos)
        self.assertEqual(len(resultado),(size+2)*len(todosLosDigitos),'En TestAncho > test_mitad > probando con size: {} y numero: {}.'.format(size,todosLosDigitos))

    def test_cuerpoInferior(self):
        """
        Prueba para el ancho del cuerpo inferior del digito.
        El numero de lineas generadas debe ser igual a size.
        Cada linea generada sigue las reglas establecidas.
        """
        for size in range(1,11):
            for numero in todosLosDigitos:
                resultado = cuerpoSuperior(size,numero)
                resultado = resultado.split('\n')
                self.assertEqual(len(resultado),size,'En TestAncho > test_cuerpoInferior > probando son size: {} y numero: {}. Numero de lineas no es el esperado.'.format(size,numero))
                for r in resultado:
                    self.assertEqual(len(r),size+2, 'En TestAncho > test_cuerpoInferior > probando son size: {} y numero: {}.'.format(size,numero))
            resultado = cuerpoSuperior(size,todosLosDigitos)
            resultado = resultado.split('\n')
            self.assertEqual(len(resultado),size,'En TestAncho > test_cuerpoSuperior > probando son size: {} y numero: {}. Numero de lineas no es el esperado.'.format(size,todosLosDigitos))
            for r in resultado:
                self.assertEqual(len(r),(size+2)*len(todosLosDigitos),'En TestAncho > test_cuerpoSuperior > probando son size: {} y numero: {}.'.format(size,todosLosDigitos))

    def test_piso(self):
        """
        Prueba para el ancho del piso.
        """
        for size in range(1,11):
            for numero in todosLosDigitos:
                resultado = piso(size,numero)
                self.assertEqual(len(resultado),size+2,'En TestAncho > test_piso > probando con size: {} y numero: {}.'.format(size,numero))
            resultado = piso(size,todosLosDigitos)
            self.assertEqual(len(resultado),(size+2)*len(todosLosDigitos),'En TestAncho > test_mitad > probando con size: {} y numero: {}.'.format(size,todosLosDigitos))

class TestAlto(unittest.TestCase):
    """
    Esta clase se encarga de hacer las pruebas unitarias
    para cada funcion de la impresora. Se probara que la altura sea
    la deseada para cada funcion, cada digito (y varios digitos) y cada size.
    Los valores de size a probar son de 1 a 10.
    El alto para un digito debe ser 2*size+3.
    El alto para varios digitos debe ser igual: 2*size+3.
    El alto se define como el numero de saltos de linea que haya.
    """
    def test_alto(self):
        """
        Prueba para el alto de uno o mas numeros.
        El salto de linea se agrega despues de cada llamado a impresora debido
        a que al imprimir en consola se agrega una linea luego de cada print().
        """
        for size in range(1,11):
            for numero in todosLosDigitos:
                resultado = techo(size,numero)+'\n'+cuerpoSuperior(size,numero)+'\n'+mitad(size,numero)+'\n'+cuerpoInferior(size,numero)+'\n'+piso(size,numero)
                resultado = resultado.split('\n')
                self.assertEqual(len(resultado),(2*size)+3,'En TestAlto > test_alto > probando son size: {} y numero: {}.'.format(size,numero))
            resultado = techo(size,todosLosDigitos)+'\n'+cuerpoSuperior(size,todosLosDigitos)+'\n'+mitad(size,todosLosDigitos)+'\n'+cuerpoInferior(size,todosLosDigitos)+'\n'+piso(size,todosLosDigitos)
            resultado = resultado.split('\n')
            self.assertEqual(len(resultado),(2*size)+3,'En TestAlto > test_alto > probando son size: {} y numero: {}.'.format(size,todosLosDigitos))

if __name__ == '__main__':
    todosLosDigitos = '0123456789'
    unittest.main()
