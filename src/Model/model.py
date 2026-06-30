class UsuarioModel:
    def __init__(self, nome, sobrenome, idade, genero, peso , altura):
        self.nome = nome
        self.sobrenome = sobrenome
        self.idade = idade
        self.genero = genero
        self.peso = peso       # em KG
        self.altura = altura   # em CM
        
    def calcular_imc(self):
        altura_usuario = self.altura * 100  # Convertendo altura de metros para centimetros
        imc = self.peso / (altura_usuario ** 2)
        return imc
    
    
        
  
        
        
        
        