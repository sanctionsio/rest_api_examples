const axios = require("axios")

const hostname = "api.sanctions.io"
const bearerToken = "12345678-12AF-12aF-12aF-1234567890aF"
const apiVersion = "2.1"

let uri = `https://${hostname}/plans`
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
    let planNames = results.map((plan) => plan["plan_name"])
    console.log(`Plans found: ${planNames.join(", ")}.`)
  })
