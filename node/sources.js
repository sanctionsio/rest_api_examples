const axios = require("axios")

const hostname = "api.sanctions.io"
const bearerToken = "12345678-12AF-12aF-12aF-1234567890aF"
const apiVersion = "2.1"

let uri = `https://${hostname}/sources`
axios
  .get(uri, {
    headers: {
      Authorization: `Bearer ${bearerToken}`,
      Accept: `application/json; version=${apiVersion}`,
    },
  })
  .then((response) => {
    let json = response.data
    let results = json.results
    let sourceNames = results.map((source) => source["short_name"])
    console.log(`Sources found: ${sourceNames.join(", ")}.`)
  })
