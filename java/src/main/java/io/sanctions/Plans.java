package io.sanctions;

import org.apache.hc.client5.http.ClientProtocolException;
import org.apache.hc.client5.http.impl.classic.CloseableHttpClient;
import org.apache.hc.client5.http.impl.classic.HttpClients;
import org.apache.hc.core5.http.ClassicHttpRequest;
import org.apache.hc.core5.http.HttpEntity;
import org.apache.hc.core5.http.HttpStatus;
import org.apache.hc.core5.http.ParseException;
import org.apache.hc.core5.http.io.HttpClientResponseHandler;
import org.apache.hc.core5.http.io.entity.EntityUtils;
import org.apache.hc.core5.http.io.support.ClassicRequestBuilder;
import org.json.JSONArray;
import org.json.JSONObject;

import java.io.IOException;
import java.util.StringJoiner;
import java.util.stream.IntStream;

public class Plans {
    private static final String HOSTNAME = "sandbox.sanctions.io";
    private static final String BEARER_TOKEN = "Bearer ded11a1cbd164242b6bb28c51f1dad5f";
    private static final String API_VERSION = "1.0";

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
                    .setHeader("Authorization", BEARER_TOKEN)
                    .setHeader("Accept", String.format("application/json; version=%s", API_VERSION))
                    .build();

            HttpClientResponseHandler<String> responseHandler = response -> {
                int status = response.getCode();
                if (status >= HttpStatus.SC_SUCCESS && status < HttpStatus.SC_REDIRECTION) {
                    HttpEntity entity = response.getEntity();
                    try {
                        return entity != null ? EntityUtils.toString(entity) : null;
                    } catch (final ParseException e) {
                        throw new ClientProtocolException(e);
                    }
                } else {
                    throw new ClientProtocolException(String.format("Server responded with status: %d", status));
                }
            };

            String jsonString = client.execute(request, responseHandler);
            return new JSONObject(jsonString);
        }
    }
}
