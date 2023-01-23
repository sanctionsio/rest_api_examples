const axios = require("axios")

const hostname = "api.sanctions.io"
const bearerToken = "ded11a1cbd164242b6bb28c51f1dad5f"
const apiVersion = "2.1"

let uri = `https://${hostname}/pep-search`
axios
  .get(uri, {
    headers: {
      Authorization: `Bearer ${bearerToken}`,
      Accept: `application/json; version=${apiVersion}`,
    },
    params: {
      name: "obama",
    },
  })
  .then((response) => {
    let json = response.data
    console.log(`Counting ${json.count} results.`)
  })
