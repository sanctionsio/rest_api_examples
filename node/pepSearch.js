const axios = require('axios');

const hostname = "sandbox.sanctions.io";
const bearerToken = "Bearer ded11a1cbd164242b6bb28c51f1dad5f";
const apiVersion = "1.0";

let uri = `https://${hostname}/pep-search`;
axios.get(uri, {
    headers: {
        'Authorization': bearerToken,
        'Accept': `application/json; version=${apiVersion}`,
    },
    params: {
        name: 'obama',
    }
}).then(response => {
    let json = response.data;
    console.log(`Counting ${json.count} results.`)
});
