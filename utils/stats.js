import { readFileSync, writeFileSync } from 'fs';
import { join, dirname } from 'path';
import { fileURLToPath } from 'url';

const __filename = fileURLToPath(import.meta.url);
const __dirname = dirname(__filename);

const STATS_FILE = join(__dirname, '..', 'Data', 'stats.json');

/**
 * Update bot usage statistics
 * @param {string} command - Command name to increment
 */
export function updateStats(command) {
    try {
        let stats = {};
        
        // Try to load existing stats
        try {
            const data = readFileSync(STATS_FILE, 'utf8');
            stats = JSON.parse(data);
        } catch (error) {
            // File doesn't exist or is invalid, start with empty stats
            stats = {};
        }

        // Initialize command counter if it doesn't exist
        if (!stats[command]) {
            stats[command] = 0;
        }

        // Increment counter
        stats[command]++;

        // Save updated stats
        writeFileSync(STATS_FILE, JSON.stringify(stats, null, 2));
    } catch (error) {
        console.error('Error updating stats:', error);
    }
}