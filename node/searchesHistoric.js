const axios = require("axios")
const qs = require("querystring")

const hostname = "api.sanctions.io"
const bearerToken = "12345678-12AF-12aF-12aF-1234567890aF"
const apiVersion = "2.1"

let uri = `https://${hostname}/searches/historic`
axios
  .get(uri, {
    headers: {
      Authorization: `Bearer ${bearerToken}`,
      Accept: `application/json; version=${apiVersion}`,
    },
    params: {
      timestamp: "2021-01-04T15:56:41.210100+01:00",
      result_count: 1,
    },
  })
  .then((response) => {
    let json = response.data
    console.log(`Found ${json.count} results.`)
  })
