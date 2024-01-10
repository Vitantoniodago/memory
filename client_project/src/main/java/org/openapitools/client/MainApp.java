package org.openapitools.client;
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.model.*;
import org.openapitools.client.api.DefaultApi;

public class MainApp {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String parola = "parola"; // String |
    try {
      apiInstance.setCustomBaseUrl("http://127.0.0.1:8000");
      apiInstance.caricaParolaCaricaParolaParolaPost(parola);
      apiInstance.correggiParolaCorreggiParolaParolaPost(parola);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#caricaParolaCaricaParolaParolaPost");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}