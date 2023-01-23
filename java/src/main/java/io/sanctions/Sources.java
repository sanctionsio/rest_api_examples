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

public class Sources {
    private static final String HOSTNAME = "api.sanctions.io";
    private static final String BEARER_TOKEN = "ded11a1cbd164242b6bb28c51f1dad5f";
    private static final String API_VERSION = "2.1";

    public static void main(String[] args) throws IOException {
        JSONObject response = Sources.invokeSources();
        JSONArray results = response.getJSONArray("results");

        StringJoiner joiner = new StringJoiner(", ");
        IntStream.range(0, results.length())
                .mapToObj(results::getJSONObject)
                .forEach(jsonObj -> joiner.add(jsonObj.getString("short_name")));

        System.out.printf("Sources found: %s", joiner.toString());
    }

    /**
     * Example showing how to call the {@code /sources} function.
     */
    private static JSONObject invokeSources() throws IOException {
        try (CloseableHttpClient client = HttpClients.createDefault()) {
            String uri = String.format("https://%s/sources", HOSTNAME);
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
