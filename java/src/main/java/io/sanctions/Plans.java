package io.sanctions;

import org.apache.hc.client5.http.impl.classic.CloseableHttpClient;
import org.apache.hc.client5.http.impl.classic.HttpClients;
import org.apache.hc.core5.http.ClassicHttpRequest;
import org.apache.hc.core5.http.io.HttpClientResponseHandler;
import org.apache.hc.core5.http.io.entity.EntityUtils;
import org.apache.hc.core5.http.io.support.ClassicRequestBuilder;
import org.json.JSONArray;
import org.json.JSONObject;

import java.io.IOException;
import java.util.StringJoiner;
import java.util.stream.IntStream;

public class Plans {
    private static final String HOSTNAME = "api.sanctions.io";
    private static final String BEARER_TOKEN = "12345678-12AF-12aF-12aF-1234567890aF";
    private static final String API_VERSION = "2.1";

    public static void main(String[] args) throws IOException {
        JSONObject response = Plans.invokePlans();
        JSONArray results = response.getJSONArray("results");

        StringJoiner joiner = new StringJoiner(", ");
        IntStream.range(0, results.length())
                .mapToObj(results::getJSONObject)
                .forEach(jsonObj -> joiner.add(jsonObj.getString("plan_name")));

        System.out.printf("Plans found: %s", joiner.toString());
    }

    /**
     * Example showing how to call the {@code /plans} function.
     */
    private static JSONObject invokePlans() throws IOException {
        try (CloseableHttpClient client = HttpClients.createDefault()) {
            String uri = String.format("https://%s/plans", HOSTNAME);
            ClassicHttpRequest request = ClassicRequestBuilder.get()
                    .setUri(uri)
                    .setHeader("Authorization", String.format("Bearer %s", BEARER_TOKEN))
                    .setHeader("Accept", String.format("application/json; version=%s", API_VERSION))
                    .build();

            HttpClientResponseHandler<String> responseHandler = response -> EntityUtils.toString(response.getEntity());
            String jsonString = client.execute(request, responseHandler);
            return new JSONObject(jsonString);
        }
    }
}
