# CamelCase: la primera mayuscula y la segunda palabra tambien 
# Identacion: 4 espacios (no tabs)
# Parametros separados por un espacio   
# Ahora son 8 espacios 
# snake_case: Espacio entre operadores

class UserAdmin():


    def __init__(self, username, password = ''):
        self.usarname = username
        self.password = password


    def set_password(self):
        pass

condy_user = UserAdmin('Cody')
