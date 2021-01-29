package io.sanctions;

import org.apache.hc.client5.http.impl.classic.CloseableHttpClient;
import org.apache.hc.client5.http.impl.classic.HttpClients;
import org.apache.hc.core5.http.ClassicHttpRequest;
import org.apache.hc.core5.http.io.HttpClientResponseHandler;
import org.apache.hc.core5.http.io.entity.EntityUtils;
import org.apache.hc.core5.http.io.support.ClassicRequestBuilder;
import org.json.JSONObject;

import java.io.IOException;
import java.net.URLEncoder;
import java.nio.charset.StandardCharsets;
import java.time.ZonedDateTime;
import java.time.format.DateTimeFormatter;
import java.util.Locale;

public class SearchesHistoric {
    private static final String HOSTNAME = "sandbox.sanctions.io";
    private static final String BEARER_TOKEN = "Bearer ded11a1cbd164242b6bb28c51f1dad5f";
    private static final String API_VERSION = "1.0";

    public static void main(String[] args) throws IOException {
        JSONObject response = SearchesHistoric.invokeSearchesHistoric();
        System.out.printf("Found %d results.%n", response.getInt("count"));
    }

    /**
     * Example showing how to call the {@code /searches/historic} function.
     */
    private static JSONObject invokeSearchesHistoric() throws IOException {
        ZonedDateTime currentDateTime = ZonedDateTime.now();
        String isoDate = currentDateTime.format(DateTimeFormatter.ofPattern("yyyy-MM-dd'T'HH:mm:ssXXX", Locale.getDefault()));
        String queryString = URLEncoder.encode(String.format("timestamp=%s&result_count=10", isoDate), StandardCharsets.UTF_8);
        String uri = String.format("https://%s/searches/historic?%s", HOSTNAME, queryString);

        try (CloseableHttpClient client = HttpClients.createDefault()) {
            ClassicHttpRequest request = ClassicRequestBuilder.get()
                    .setUri(uri)
                    .setHeader("Authorization", BEARER_TOKEN)
                    .setHeader("Accept", String.format("application/json; version=%s", API_VERSION))
                    .build();

            HttpClientResponseHandler<String> responseHandler = response -> EntityUtils.toString(response.getEntity());
            String jsonString = client.execute(request, responseHandler);
            return new JSONObject(jsonString);
        }
    }
}
