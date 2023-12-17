import time

class RiceCooker:
    def __init__(self):
        self.rice_type = ''
        self.water_level = 0
        self.is_cooking = False
        self.cooking_time = 0

    def set_rice_type(self, rice_type):
        self.rice_type = rice_type
        print(f"Type de riz réglé sur : {self.rice_type}")

    def set_water_level(self, level):
        if not 0 <= level <= 100:
            raise ValueError('Niveau d\'eau invalide. Veuillez choisir une valeur entre 0 et 100.')

        self.water_level = level
        print(f"Niveau d'eau réglé sur : {self.water_level}%")

    def set_cooking_time(self, time_minutes):
        if not 0 <= time_minutes <= 60:
            raise ValueError('Temps de cuisson invalide. Veuillez choisir une valeur entre 0 et 60 minutes.')

        self.cooking_time = time_minutes
        print(f"Temps de cuisson réglé sur : {self.cooking_time} minutes")

    def start_cooking(self):
        try:
            if not self.rice_type:
                raise ValueError('Veuillez sélectionner un type de riz avant de commencer la cuisson.')

            if self.water_level == 0:
                raise ValueError('Veuillez définir le niveau d\'eau avant de commencer la cuisson.')

            if self.cooking_time == 0:
                raise ValueError('Veuillez définir le temps de cuisson avant de commencer.')

            print("Cuisson en cours...")
            self.is_cooking = True

            # Simulation de la cuisson - remplacez cela par une logique de détection réelle
            time.sleep(self.cooking_time * 60)  # Convertir le temps de cuisson en secondes

            print("La cuisson est terminée.")
            self.is_cooking = False

        except ValueError as e:
            print(f"Erreur de cuisson : {e}")
            self.is_cooking = False

    def stop_cooking(self):
        if not self.is_cooking:
            print("Le cuiseur à riz n'est pas en cours de cuisson.")
        else:
            print("Arrêt de la cuisson.")
            self.is_cooking = False

    def check_cooking_status(self):
        cooking_status = "Oui" if self.is_cooking else "Non"
        print(f"État du cuiseur à riz - Type de riz: {self.rice_type}, Niveau d'eau: {self.water_level}%, Cuisson en cours: {cooking_status}")

# Utilisation du cuiseur à riz
rice_cooker = RiceCooker()

try:
    rice_cooker.set_rice_type('riz blanc')
    rice_cooker.set_water_level(50)
    rice_cooker.set_cooking_time(10)
    rice_cooker.start_cooking()
    rice_cooker.check_cooking_status()
    rice_cooker.stop_cooking()
except ValueError as error:
    print(f"Erreur: {error}")
