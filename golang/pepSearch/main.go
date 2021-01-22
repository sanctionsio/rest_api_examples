package main

import (
    "encoding/json"
    "fmt"
    "io/ioutil"
    "log"
    "net/http"
)

const (
    hostname = "sandbox.sanctions.io"
    bearerToken = "Bearer ded11a1cbd164242b6bb28c51f1dad5f"
    apiVersion = "1.0"
)

func main() {
    data, err := invokePepSearch()
    if err != nil {
        log.Fatal(err)
    } else {
        count := data["count"]
        log.Printf("Counting %v results.", count)
    }
}

// Example showing how to invoke the /pep-search function in the sanctions.io REST api
func invokePepSearch() (map[string]interface{}, error) {
    client := &http.Client{}
    req, err := http.NewRequest("GET", fmt.Sprintf("https://%s/pep-search", hostname), nil)
    if err != nil {
        return nil, err
    }

    query := req.URL.Query()
    query.Add("name", "obama")
    req.URL.RawQuery = query.Encode()

    req.Header.Add("Accept", fmt.Sprintf("application/json; version=%s", apiVersion))
    req.Header.Add("Authorization", bearerToken)
    resp, err := client.Do(req)

    if err != nil {
        return nil, err
    } else if resp.StatusCode < 200 || resp.StatusCode >= 300 {
        return nil, fmt.Errorf("server responded with status: %d", resp.StatusCode)
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
