import { loadJsonData } from './jsonLoader.js';
import { getRandomChoice } from './random.js';

// Load data from JSON files
const armesData = loadJsonData('armes.json');
const atoutsData = loadJsonData('atouts.json');
const equipementsData = loadJsonData('equipements.json');
export const defisData = loadJsonData('defis.json');

/**
 * Safe list getter - returns array or empty array if not valid
 * @param {Object} obj - Object to get property from
 * @param {string} key - Property key
 * @returns {Array} Array or empty array
 */
function safeList(obj, key) {
    const value = obj?.[key];
    return Array.isArray(value) ? value : [];
}

// Category key mapping for display names to JSON keys
const CATEGORY_KEY_MAP = {
    // Primary weapons
    "Fusils d'assaut": "fusils_d_assaut",
    "Mitraillettes": "mitraillettes", 
    "Fusils à pompe": "fusils_a_pompe",
    "Mitrailleuses": "mitrailleuses",
    "Fusils tactiques": "fusils_tactiques",
    "Fusils de précision": "fusils_de_precision",
    // Secondary weapons
    "Pistolets": "pistolets",
    "Lanceurs": "lanceurs",
    "Spécial": "special"
};

// Cache for weapons by category
const weaponCache = {
    principales: {},
    secondaires: {}
};

/**
 * Initialize weapon cache
 */
function initCache() {
    // Cache primary weapons
    if (armesData.principales) {
        for (const [displayName, key] of Object.entries(CATEGORY_KEY_MAP)) {
            if (armesData.principales[key]) {
                weaponCache.principales[displayName] = armesData.principales[key];
            }
        }
    }
    
    // Cache secondary weapons
    if (armesData.secondaires) {
        for (const [displayName, key] of Object.entries(CATEGORY_KEY_MAP)) {
            if (armesData.secondaires[key]) {
                weaponCache.secondaires[displayName] = armesData.secondaires[key];
            }
        }
    }
}

initCache();

/**
 * Find weapons list for a given category
 * @param {string} category - Category name
 * @returns {Array} Array of weapons in the category
 */
export function findCategoryList(category) {
    // Check primary weapons first
    if (weaponCache.principales[category]) {
        return weaponCache.principales[category];
    }
    // Then check secondary weapons
    if (weaponCache.secondaires[category]) {
        return weaponCache.secondaires[category];
    }
    return [];
}

/**
 * Generate a random weapon from all available weapons
 * @returns {string} Random weapon name
 */
export function generateRandomWeapon() {
    const allWeapons = [];
    
    // Add primary weapons
    if (armesData.principales) {
        for (const weapons of Object.values(armesData.principales)) {
            if (Array.isArray(weapons)) {
                allWeapons.push(...weapons);
            }
        }
    }
    
    // Add secondary weapons
    if (armesData.secondaires) {
        for (const weapons of Object.values(armesData.secondaires)) {
            if (Array.isArray(weapons)) {
                allWeapons.push(...weapons);
            }
        }
    }
    
    return allWeapons.length > 0 ? getRandomChoice(allWeapons) : "Aucune arme disponible";
}

/**
 * Generate a random primary weapon
 * @returns {string} Random primary weapon name
 */
export function generatePrimaryWeapon() {
    const primaryWeapons = [];
    
    if (armesData.principales) {
        for (const weapons of Object.values(armesData.principales)) {
            if (Array.isArray(weapons)) {
                primaryWeapons.push(...weapons);
            }
        }
    }
    
    return primaryWeapons.length > 0 ? getRandomChoice(primaryWeapons) : "Aucune arme principale";
}

/**
 * Generate a random secondary weapon
 * @returns {string} Random secondary weapon name
 */
export function generateSecondaryWeapon() {
    const secondaryWeapons = [];
    
    if (armesData.secondaires) {
        for (const weapons of Object.values(armesData.secondaires)) {
            if (Array.isArray(weapons)) {
                secondaryWeapons.push(...weapons);
            }
        }
    }
    
    return secondaryWeapons.length > 0 ? getRandomChoice(secondaryWeapons) : "Aucune arme secondaire";
}

// Cache for faster generation
const generationCache = {
    armePrincipales: [],
    armeSecondaires: [],
    atouts1: [],
    atouts2: [],
    atouts3: [],
    tactiques: [],
    mortels: []
};

/**
 * Refresh the generation cache
 */
function refreshCache() {
    // Primary weapons
    generationCache.armePrincipales = [];
    for (const weapons of Object.values(armesData.principales || {})) {
        if (Array.isArray(weapons)) {
            generationCache.armePrincipales.push(...weapons);
        }
    }
    
    // Secondary weapons
    generationCache.armeSecondaires = [];
    for (const weapons of Object.values(armesData.secondaires || {})) {
        if (Array.isArray(weapons)) {
            generationCache.armeSecondaires.push(...weapons);
        }
    }
    
    // Perks and equipment
    generationCache.atouts1 = safeList(atoutsData, 'atout_1');
    generationCache.atouts2 = safeList(atoutsData, 'atout_2');
    generationCache.atouts3 = safeList(atoutsData, 'atout_3');
    generationCache.tactiques = safeList(equipementsData, 'tactiques');
    generationCache.mortels = safeList(equipementsData, 'mortels');
}

refreshCache();

/**
 * Generate a complete BO6 class with 1 perk per slot
 * @returns {Object} Generated class object
 */
export function generateClass() {
    // Select primary weapon
    const armePrincipale = generationCache.armePrincipales.length > 0 
        ? getRandomChoice(generationCache.armePrincipales) 
        : "Aucune arme principale disponible";

    // Select secondary weapon (avoid duplicates if possible)
    let armeSecondaire;
    if (generationCache.armeSecondaires.length > 0) {
        armeSecondaire = getRandomChoice(generationCache.armeSecondaires);
        // If same as primary and we have other options, try to get a different one
        if (armeSecondaire === armePrincipale && generationCache.armeSecondaires.length > 1) {
            const otherWeapons = generationCache.armeSecondaires.filter(w => w !== armePrincipale);
            if (otherWeapons.length > 0) {
                armeSecondaire = getRandomChoice(otherWeapons);
            }
        }
    } else {
        armeSecondaire = "Aucune arme secondaire disponible";
    }

    return {
        arme_principale: armePrincipale,
        arme_secondaire: armeSecondaire,
        atout_1: generationCache.atouts1.length > 0 ? getRandomChoice(generationCache.atouts1) : "Aucun atout slot 1",
        atout_2: generationCache.atouts2.length > 0 ? getRandomChoice(generationCache.atouts2) : "Aucun atout slot 2", 
        atout_3: generationCache.atouts3.length > 0 ? getRandomChoice(generationCache.atouts3) : "Aucun atout slot 3",
        equipement_tactique: generationCache.tactiques.length > 0 ? getRandomChoice(generationCache.tactiques) : "Aucun équipement tactique",
        equipement_mortel: generationCache.mortels.length > 0 ? getRandomChoice(generationCache.mortels) : "Aucun équipement mortel"
    };
}