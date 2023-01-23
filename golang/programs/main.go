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
	hostname    = "api.sanctions.io"
	bearerToken = "ded11a1cbd164242b6bb28c51f1dad5f"
	apiVersion  = "2.1"
)

func main() {
	data, err := invokePrograms()
	if err != nil {
		log.Fatal(err)
	} else {
		results := data["results"].([]interface{})
		names := make([]string, len(results))
		for i, result := range results {
			names[i] = result.(map[string]interface{})["short_name"].(string)
		}
		log.Printf("Programs found: %s", strings.Join(names, ", "))
	}
}

// Example showing how to invoke the /programs function in the sanctions.io REST api
func invokePrograms() (map[string]interface{}, error) {
	client := &http.Client{}
	req, err := http.NewRequest("GET", fmt.Sprintf("https://%s/programs", hostname), nil)
	if err != nil {
		return nil, err
	}

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
