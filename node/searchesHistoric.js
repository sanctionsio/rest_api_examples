const axios = require('axios');
const qs = require('querystring');

const hostname = "sandbox.sanctions.io";
const bearerToken = "Bearer ded11a1cbd164242b6bb28c51f1dad5f";
const apiVersion = "1.0";

let uri = `https://${hostname}/searches/historic`;
axios.get(uri, {
    headers: {
        'Authorization': bearerToken,
        'Accept': `application/json; version=${apiVersion}`,
    },
    params: {
        timestamp: '2021-01-21T16:48:08+01:00',
        result_count: 10,
    },
    paramsSerializer: params => {
        return qs.stringify(params, qs.escape('&'))
    }
})
    .then(response => {
        let status = response.status;
        if (status >= 200 && status < 300) {
            let json = response.data;
            let results = json.results;
            console.log(`Found ${results.length} results.`)
        } else {
            console.error(`Server responded with status: ${status}`)
        }
    })
    .catch(err => {
        console.error(`Error calling ${uri}: ${err}`)
    })