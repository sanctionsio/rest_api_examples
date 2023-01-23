const axios = require("axios")

const hostname = "api.sanctions.io"
const bearerToken = "ded11a1cbd164242b6bb28c51f1dad5f"
const apiVersion = "2.0"

let uri = `https://${hostname}/search`
axios
  .get(uri, {
    headers: {
      Authorization: `Bearer ${bearerToken}`,
      Accept: `application/json; version=${apiVersion}`,
    },
    params: {
      name: "juan",
      country_residence: "FR",
    },
  })
  .then((response) => {
    let json = response.data
    console.log(`Found ${json.count} results.`)
  })
