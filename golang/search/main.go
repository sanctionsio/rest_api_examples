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
	bearerToken = "ded11a1cbd164242b6bb28c51f1dad5f"
	apiVersion  = "2.0"
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
	query.Add("countries", "FR")
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
