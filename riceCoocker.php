<?php

class RiceCooker
{
    private $riceType = '';
    private $waterLevel = 0;
    private $isCooking = false;
    private $cookingTime = 0;

    public function setRiceType($riceType)
    {
        $this->riceType = $riceType;
        echo "Type de riz réglé sur : {$this->riceType}\n";
    }

    public function setWaterLevel($level)
    {
        if (!($level >= 0 && $level <= 100)) {
            throw new InvalidArgumentException('Niveau d\'eau invalide. Veuillez choisir une valeur entre 0 et 100.');
        }

        $this->waterLevel = $level;
        echo "Niveau d'eau réglé sur : {$this->waterLevel}%\n";
    }

    public function setCookingTime($timeMinutes)
    {
        if (!($timeMinutes >= 0 && $timeMinutes <= 60)) {
            throw new InvalidArgumentException('Temps de cuisson invalide. Veuillez choisir une valeur entre 0 et 60 minutes.');
        }

        $this->cookingTime = $timeMinutes;
        echo "Temps de cuisson réglé sur : {$this->cookingTime} minutes\n";
    }

    public function startCooking()
    {
        try {
            if (empty($this->riceType)) {
                throw new InvalidArgumentException('Veuillez sélectionner un type de riz avant de commencer la cuisson.');
            }

            if ($this->waterLevel == 0) {
                throw new InvalidArgumentException('Veuillez définir le niveau d\'eau avant de commencer la cuisson.');
            }

            if ($this->cookingTime == 0) {
                throw new InvalidArgumentException('Veuillez définir le temps de cuisson avant de commencer.');
            }

            echo "Cuisson en cours...\n";
            $this->isCooking = true;

            echo "Avant la simulation : is_cooking={$this->isCooking}\n";

            // Simulation de la cuisson - remplacez cela par une logique de détection réelle
            sleep($this->cookingTime * 60); // Convertir le temps de cuisson en secondes

            echo "La cuisson est terminée.\n";
            $this->isCooking = false;

            echo "Après la simulation : is_cooking={$this->isCooking}\n";
        } catch (InvalidArgumentException $e) {
            echo "Erreur de cuisson : {$e->getMessage()}\n";
            $this->isCooking = false;
        }
    }

    public function stopCooking()
    {
        if (!$this->isCooking) {
            echo "Le cuiseur à riz n'est pas en cours de cuisson.\n";
        } else {
            echo "Arrêt de la cuisson.\n";
            $this->isCooking = false;
        }
    }

    public function checkCookingStatus()
    {
        $cookingStatus = $this->isCooking ? "Oui" : "Non";
        return "État du cuiseur à riz - Type de riz: {$this->riceType}, Niveau d'eau: {$this->waterLevel}%, Cuisson en cours: {$cookingStatus}";
    }
}

// Exemple d'utilisation du cuiseur à riz en PHP
$riceCooker = new RiceCooker();

try {
    $riceCooker->setRiceType('riz blanc');
    $riceCooker->setWaterLevel(50);
    $riceCooker->setCookingTime(0.5);
    $riceCooker->startCooking();
    echo $riceCooker->checkCookingStatus() . "\n";
    $riceCooker->stopCooking();
} catch (InvalidArgumentException $error) {
    echo "Erreur: {$error->getMessage()}\n";
}
?>
