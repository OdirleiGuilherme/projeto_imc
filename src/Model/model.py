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
    
    def classificar_imc(self):
            imc = self.calcular_imc()
            if imc < 18.5:  
                return "Abaixo do peso"
            elif 18.5 <= imc < 24.9:
                return "Peso normal"
            elif 25 <= imc < 29.9:
                return " Acima do peso (Sobrepeso)"
            elif 30 <= imc < 34.9:
                return "Obesidade grau I"
            elif 35 <= imc < 39.9:
                return "Obesidade grau II (Severa)"
            else:
                return "Obesidade grau III (Mórbida)"
    
        
  
        
        
        
        