class RiceCooker {
    constructor() {
        this.riceType = '';
        this.waterLevel = 0;
        this.isCooking = false;
        this.cookingTime = 0;
    }

    setRiceType(riceType) {
        this.riceType = riceType;
        console.log(`Type de riz réglé sur : ${this.riceType}`);
    }

    setWaterLevel(level) {
        if (!(level >= 0 && level <= 100)) {
            throw new Error('Niveau d\'eau invalide. Veuillez choisir une valeur entre 0 et 100.');
        }

        this.waterLevel = level;
        console.log(`Niveau d'eau réglé sur : ${this.waterLevel}%`);
    }

    setCookingTime(timeMinutes) {
        if (!(timeMinutes >= 0 && timeMinutes <= 60)) {
            throw new Error('Temps de cuisson invalide. Veuillez choisir une valeur entre 0 et 60 minutes.');
        }

        this.cookingTime = timeMinutes;
        console.log(`Temps de cuisson réglé sur : ${this.cookingTime} minutes`);
    }

    startCooking() {
        try {
            if (!this.riceType) {
                throw new Error('Veuillez sélectionner un type de riz avant de commencer la cuisson.');
            }

            if (this.waterLevel === 0) {
                throw new Error('Veuillez définir le niveau d\'eau avant de commencer la cuisson.');
            }

            if (this.cookingTime === 0) {
                throw new Error('Veuillez définir le temps de cuisson avant de commencer.');
            }

            console.log("Cuisson en cours...");
            this.isCooking = true;

            console.log(`Avant la simulation : isCooking=${this.isCooking}`);

            // Simulation de la cuisson - remplacez cela par une logique de détection réelle
            setTimeout(() => {
                console.log("La cuisson est terminée.");
                this.isCooking = false;
                console.log(`Après la simulation : isCooking=${this.isCooking}`);
            }, this.cookingTime * 60 * 1000); // Convertir le temps de cuisson en millisecondes

        } catch (error) {
            console.error(`Erreur de cuisson : ${error.message}`);
            this.isCooking = false;
        }
    }

    stopCooking() {
        if (!this.isCooking) {
            console.log("Le cuiseur à riz n'est pas en cours de cuisson.");
        } else {
            console.log("Arrêt de la cuisson.");
            this.isCooking = false;
        }
    }

    checkCookingStatus() {
        const cookingStatus = this.isCooking ? "Oui" : "Non";
        return `État du cuiseur à riz - Type de riz: ${this.riceType}, Niveau d'eau: ${this.waterLevel}%, Cuisson en cours: ${cookingStatus}`;
    }
}

// Utilisation du cuiseur à riz en JavaScript
const riceCooker = new RiceCooker();

try {
    riceCooker.setRiceType('riz blanc');
    riceCooker.setWaterLevel(50);
    riceCooker.setCookingTime(0.5);
    riceCooker.startCooking();
    console.log(riceCooker.checkCookingStatus());
    riceCooker.stopCooking();
} catch (error) {
    console.error(`Erreur: ${error.message}`);
}

module.exports = RiceCooker;