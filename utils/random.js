/**
 * Get a random element from an array
 * @param {Array} array - Array to choose from
 * @returns {any} Random element from the array
 */
export function getRandomChoice(array) {
    if (!Array.isArray(array) || array.length === 0) {
        return null;
    }
    return array[Math.floor(Math.random() * array.length)];
}

/**
 * Get multiple random elements from an array without duplicates
 * @param {Array} array - Array to choose from
 * @param {number} count - Number of elements to choose
 * @returns {Array} Array of random elements
 */
export function getRandomChoices(array, count) {
    if (!Array.isArray(array) || array.length === 0 || count <= 0) {
        return [];
    }
    
    const shuffled = [...array].sort(() => 0.5 - Math.random());
    return shuffled.slice(0, Math.min(count, array.length));
}