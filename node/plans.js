const axios = require('axios');

const hostname = "sandbox.sanctions.io";
const bearerToken = "Bearer ded11a1cbd164242b6bb28c51f1dad5f";
const apiVersion = "1.0";

let uri = `https://${hostname}/plans`;
axios.get(uri, {
    headers: {
        'Authorization': bearerToken,
        'Accept': `application/json; version=${apiVersion}`,
    },
}).then(response => {
    let json = response.data;
    let results = json.results;
    let planNames = results.map(plan => plan["plan_name"]);
    console.log(`Plans found: ${planNames.join(', ')}.`)
})
