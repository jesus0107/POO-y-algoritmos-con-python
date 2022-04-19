class Automovil:
  def __init__(self, color, modelo, marca):
    self.color = color
    self.modelo = modelo
    self.marca = marca
    self._estado = "reposo"
    self._motor = Motor(cilindros = 4)

  def acelerar(self, movimiento = "despacio"):
    if movimiento == "rapida":
      self._motor.inyecta_gasolina(cantidad = 10)
    else:
      self._motor.inyecta_gasolina(cantidad = 3)
      
    self._estado = "movimiento"


class Motor:
  def __init_(self, cilindros, tipo = "gasolina"):
    self.cilindros = cilindros
    self.tipo = tipo
    self.temperatura = 0
  
  def inyecta_gasolina(self, cantidad):
    pass
    

if __name__ == "__main__":
  pass