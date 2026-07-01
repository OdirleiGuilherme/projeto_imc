class UsuarioModel:
    def __init__(self, nome, sobrenome, idade, genero, peso , altura, nivel_atividade):
        self.nome = nome
        self.sobrenome = sobrenome
        self.idade = idade
        self.genero = genero
        self.peso = peso       # em KG
        self.altura = altura   # em CM
        self.nivel_atividade = nivel_atividade  # 1: Sedentário, 2: Pouco ativo, 3: Moderadamente ativo, 4: Muito ativo, 5: Extremamente ativo
    
    def calcular_imc(self):
        imc = self.peso / (self.altura ** 2)
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
            
    def calcular_tmb(self):
        altura_usuario = self.altura * 100 # A Taxa metabolica basal exige altura em centímetros, então convertemos de metros para centímetros
        if self.genero.lower() == "masculino":
            tmb = (10 * self.peso) + (6.25 * altura_usuario) - ( 5 * self.idade) + 5
        elif self.genero.lower() == "feminino":
            tmb = (10 * self.peso) + (6.25 * altura_usuario) - ( 5 * self.idade) - 161
        else:
            raise ValueError("Gênero inválido. Use 'masculino' ou 'feminino'.")
        return tmb
    
    def calcular_gcd(self,tmb):
      fatores_atividades = {
        '1': 1.2,    # Sedentário
        '2': 1.375,  # Pouco ativo
        '3': 1.55,   # Moderadamente ativo
        '4': 1.725,  # Muito ativo
        '5': 1.9     # Extremamente ativo
        }
      
      opcao_atividade = self.nivel_atividade[0]
      fator_atividade = fatores_atividades.get(opcao_atividade, 1.2)  # Padrão para sedentário
      gcd = tmb * fator_atividade
      return gcd
  
    #def calcular_macros(self, gcd):
        # comentário Definindo as porcentagens para cada macronutriente
        #porcentagem_proteina = 0.30  # 30% das calorias
        #porcentagem_gordura = 0.25   # 25% das calorias
        #porcentagem_carboidrato = 0.45  # 45% das calorias

        # comentário Calculando a quantidade de calorias de cada macronutriente
        #calorias_proteina = gcd * porcentagem_proteina
        #calorias_gordura = gcd * porcentagem_gordura
        #calorias_carboidrato = gcd * porcentagem_carboidrato

        # comentário Convertendo calorias em gramas (1g de proteína = 4 kcal, 1g de gordura = 9 kcal, 1g de carboidrato = 4 kcal)
        #gramas_proteina = calorias_proteina / 4
        #gramas_gordura = calorias_gordura / 9
        #gramas_carboidrato = calorias_carboidrato / 4

        #return {
        #    'proteina': gramas_proteina,
        #    'gordura': gramas_gordura,
        #    'carboidrato': gramas_carboidrato
        #}
    def calcular_gcd_perda_peso(self, gcd):
        # Definindo o déficit calórico para perda de peso
        return gcd - 600  # redução com 600 calorias do GCD para perda de peso

    def calcular_manutencao_peso(self, gcd):
        # Para manutenção de peso, o GCD é mantido
        return gcd
    
        