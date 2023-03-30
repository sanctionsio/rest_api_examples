const axios = require("axios")

const hostname = "api.sanctions.io"
const bearerToken = "12345678-12AF-12aF-12aF-1234567890aF"
const apiVersion = "2.1"

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
      data_source: "ALL",
    },
  })
  .then((response) => {
    let json = response.data
    console.log(`Found ${json.count} results.`)
  })
