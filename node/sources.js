const axios = require('axios');

const hostname = "sandbox.sanctions.io";
const bearerToken = "Bearer ded11a1cbd164242b6bb28c51f1dad5f";
const apiVersion = "1.0";

let uri = `https://${hostname}/sources`;
axios.get(uri, {
    headers: {
        'Authorization': bearerToken,
        'Accept': `application/json; version=${apiVersion}`,
    },
}).then(response => {
    let json = response.data;
    let results = json.results;
    let sourceNames = results.map(source => source["short_name"]);
    console.log(`Sources found: ${sourceNames.join(', ')}.`)
})
