const crypto = require('crypto');

/**
 * Hashes an input string into a numerical value using SHA-256.
 * 
 * @param {string} inputString - The input string to hash.
 * @return {number} The numerical value of the hash.
 */
function hashString(inputString) {
    // Create a SHA-256 hash of the input string.
    const hash = crypto.createHash('sha256');
    hash.update(inputString);
    // Convert the hash to a hexadecimal string and parse it as a BigInt.
    // Then use modulo to ensure it fits into a JavaScript number safely.
    const hashInt = BigInt('0x' + hash.digest('hex')) % BigInt(Number.MAX_SAFE_INTEGER);
    return Number(hashInt);
}

function hashString2(inputString) {
    let hash = 0;
    if (inputString.length == 0) return 0;
    for (let i = 0; i < inputString.length; i++) {
        hash = ((hash << 5) - hash) + inputString.charCodeAt(i);
        hash |= 0; //converts to integer
    }
    return hash;
}

function computeScore2(username, server) {
    return (hashString2(username)*13  + hashString2(server)*11 ) %67;
}

/**
 * Computes a combined hash score for a resource-server pair.
 * 
 * @param {string} resource - The resource identifier.
 * @param {string} server - The server identifier.
 * @return {number} The hash score of the resource-server pair.
 */
function computeScore(resource, server) {
    // Concatenate resource and server with a separator to ensure unique combinations.
    const pairString = resource + ":" + server;
    return hashString(pairString);
}

module.exports = { hashString, computeScore };
