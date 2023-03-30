package main

import (
	"encoding/json"
	"fmt"
	"io/ioutil"
	"log"
	"net/http"
)

const (
	hostname    = "api.sanctions.io"
	bearerToken = "12345678-12AF-12aF-12aF-1234567890aF"
	apiVersion  = "2.1"
)

func main() {
	data, err := invokeSearch()
	if err != nil {
		log.Fatal(err)
	} else {
		log.Printf("Found %v results.", data["count"])
	}
}

// Example showing how to invoke the /search function in the sanctions.io REST api
func invokeSearch() (map[string]interface{}, error) {
	client := &http.Client{}
	req, err := http.NewRequest("GET", fmt.Sprintf("https://%s/search", hostname), nil)
	if err != nil {
		return nil, err
	}

	query := req.URL.Query()
	query.Add("name", "juan")
	query.Add("country_residence", "FR")
	query.Add("data_source", "ALL")
	req.URL.RawQuery = query.Encode()

	req.Header.Add("Accept", fmt.Sprintf("application/json; version=%s", apiVersion))
	req.Header.Add("Authorization", fmt.Sprintf("Bearer %s", bearerToken))
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
