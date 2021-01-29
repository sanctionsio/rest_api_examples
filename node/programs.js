const axios = require('axios');

const hostname = "sandbox.sanctions.io";
const bearerToken = "Bearer ded11a1cbd164242b6bb28c51f1dad5f";
const apiVersion = "1.0";

let uri = `https://${hostname}/programs`;
axios.get(uri, {
    headers: {
        'Authorization': bearerToken,
        'Accept': `application/json; version=${apiVersion}`,
    },
}).then(response => {
    let json = response.data;
    let results = json.results;
    let programNames = results.map(program => program["short_name"]);
    console.log(`Programs found: ${programNames.join(', ')}.`)
})
