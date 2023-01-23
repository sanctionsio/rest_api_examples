const axios = require("axios")

const hostname = "api.sanctions.io"
const bearerToken = "ded11a1cbd164242b6bb28c51f1dad5f"
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
