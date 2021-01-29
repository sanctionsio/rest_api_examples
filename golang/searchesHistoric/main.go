package main

import (
    "encoding/json"
    "fmt"
    "io/ioutil"
    "log"
    "net/http"
    "strings"
)

const (
    hostname = "sandbox.sanctions.io"
    bearerToken = "Bearer ded11a1cbd164242b6bb28c51f1dad5f"
    apiVersion = "1.0"
)

func main() {
    data, err := invokeSearchesHistoric()
    if err != nil {
        log.Fatal(err)
    } else {
        log.Printf("Found %v results.", data["count"])
    }
}

// Example showing how to invoke the /search function in the sanctions.io REST api
func invokeSearchesHistoric() (map[string]interface{}, error) {
    client := &http.Client{}
    req, err := http.NewRequest("GET", fmt.Sprintf("https://%s/searches/historic", hostname), nil)
    if err != nil {
        return nil, err
    }

    query := req.URL.Query()
    query.Add("timestamp", "2021-01-21T16:00:00+01:00")
    query.Add("result_count", "10")

    rawQuery := query.Encode()
    rawQuery = strings.ReplaceAll(rawQuery, "&", "%26")
    rawQuery = strings.ReplaceAll(rawQuery, "=", "%3D")
    req.URL.RawQuery = query.Encode()

    req.Header.Add("Accept", fmt.Sprintf("application/json; version=%s", apiVersion))
    req.Header.Add("Authorization", bearerToken)
    resp, err := client.Do(req)

    if err != nil {
        return nil, err
    }

    body, err := ioutil.ReadAll(resp.Body)
    if err != nil {
        return nil, err
    }

    var data map[string]interface{}
    err = json.Unmarshal(body, &data)
    if err != nil {
        return nil, err
    } else {
        return data, nil
    }
}
