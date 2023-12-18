const chai = require('chai');
const assert = chai.assert;
const RiceCooker = require('./riceCoocker');

describe('RiceCooker', () => {
    let riceCooker;

    beforeEach(() => {
        riceCooker = new RiceCooker();
    });

    it('devrait initialiser le cuiseur à riz avec les valeurs par défaut', () => {
        assert.equal(riceCooker.riceType, '');
        assert.equal(riceCooker.waterLevel, 0);
        assert.isFalse(riceCooker.isCooking);
        assert.equal(riceCooker.cookingTime, 0);
    });

    it('devrait définir le type de riz', () => {
        riceCooker.setRiceType('riz complet');
        assert.equal(riceCooker.riceType, 'riz complet');
    });

    it('devrait définir le niveau d\'eau', () => {
        riceCooker.setWaterLevel(50);
        assert.equal(riceCooker.waterLevel, 50);
    });

    it('devrait lever une erreur pour un niveau d\'eau invalide', () => {
        assert.throw(() => riceCooker.setWaterLevel(150), Error, 'Niveau d\'eau invalide.');
    });

    it('devrait définir le temps de cuisson', () => {
        riceCooker.setCookingTime(30);
        assert.equal(riceCooker.cookingTime, 30);
    });

    it('devrait lever une erreur pour un temps de cuisson invalide', () => {
        assert.throw(() => riceCooker.setCookingTime(70), Error, 'Temps de cuisson invalide.');
    });

    it('devrait démarrer la cuisson', (done) => {
        riceCooker.setRiceType('riz basmati');
        riceCooker.setWaterLevel(40);
        riceCooker.setCookingTime(0.5);

        riceCooker.startCooking();

        setTimeout(() => {
            assert.isTrue(riceCooker.isCooking);
            done();
        }, 100); // Laisser un peu de temps pour que la logique de startCooking s'exécute
    });

    it('devrait arrêter la cuisson', () => {
        riceCooker.isCooking = true;
        riceCooker.stopCooking();
        assert.isFalse(riceCooker.isCooking);
    });

    it('devrait vérifier l\'état de la cuisson', () => {
        riceCooker.setRiceType('riz sauvage');
        riceCooker.setWaterLevel(70);
        riceCooker.setCookingTime(0.8);
        riceCooker.startCooking();

        const status = riceCooker.checkCookingStatus();
        assert.include(status, 'État du cuiseur à riz - Type de riz: riz sauvage, Niveau d\'eau: 70%, Cuisson en cours: Oui');
    });

    // it('devrait arrêter la cuisson lorsque le temps est écoulé', (done) => {
    //     riceCooker.setRiceType('riz blanc');
    //     riceCooker.setWaterLevel(60);
    //     riceCooker.setCookingTime(0.1);

    //     riceCooker.startCooking();

    //     setTimeout(() => {
    //         assert.isFalse(riceCooker.isCooking);
    //         done();
    //     }, 200); // Laisser suffisamment de temps pour que la cuisson se termine
    // });
});
