const axios = require("axios")

const hostname = "api.sanctions.io"
const bearerToken = "ded11a1cbd164242b6bb28c51f1dad5f"
const apiVersion = "2.1"

let uri = `https://${hostname}/programs`
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
    let programNames = results.map((program) => program["short_name"])
    console.log(`Programs found: ${programNames.join(", ")}.`)
  })
