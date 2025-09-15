import { readFileSync } from 'fs';
import { join, dirname } from 'path';
import { fileURLToPath } from 'url';

const __filename = fileURLToPath(import.meta.url);
const __dirname = dirname(__filename);

/**
 * Load JSON data from the Data directory
 * @param {string} filename - Name of the JSON file
 * @returns {Object} Parsed JSON data
 */
export function loadJsonData(filename) {
    try {
        const filePath = join(__dirname, '..', 'Data', filename);
        const data = readFileSync(filePath, 'utf8');
        return JSON.parse(data);
    } catch (error) {
        console.error(`Error loading JSON file ${filename}:`, error);
        return {};
    }
}