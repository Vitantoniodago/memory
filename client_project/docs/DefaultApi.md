# DefaultApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**caricaParolaCaricaParolaParolaPost**](DefaultApi.md#caricaParolaCaricaParolaParolaPost) | **POST** /carica_parola/{parola} | Carica Parola |
| [**correggiParolaCorreggiParolaParolaPost**](DefaultApi.md#correggiParolaCorreggiParolaParolaPost) | **POST** /correggi_parola/{parola} | Correggi Parola |
| [**getOpenApiEndpointOpenapiJsonGet**](DefaultApi.md#getOpenApiEndpointOpenapiJsonGet) | **GET** /openapi.json | Get Open Api Endpoint |


<a id="caricaParolaCaricaParolaParolaPost"></a>
# **caricaParolaCaricaParolaParolaPost**
> caricaParolaCaricaParolaParolaPost(parola)

Carica Parola

API per caricare una parola nel dizionario.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String parola = "parola_example"; // String | 
    try {
      apiInstance.caricaParolaCaricaParolaParolaPost(parola);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#caricaParolaCaricaParolaParolaPost");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **parola** | **String**|  | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |
| **422** | Validation Error |  -  |

<a id="correggiParolaCorreggiParolaParolaPost"></a>
# **correggiParolaCorreggiParolaParolaPost**
> List&lt;Item&gt; correggiParolaCorreggiParolaParolaPost(parola)

Correggi Parola

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String parola = "parola_example"; // String | 
    try {
      List<Item> result = apiInstance.correggiParolaCorreggiParolaParolaPost(parola);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#correggiParolaCorreggiParolaParolaPost");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **parola** | **String**|  | |

### Return type

[**List&lt;Item&gt;**](Item.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |
| **422** | Validation Error |  -  |

<a id="getOpenApiEndpointOpenapiJsonGet"></a>
# **getOpenApiEndpointOpenapiJsonGet**
> getOpenApiEndpointOpenapiJsonGet()

Get Open Api Endpoint

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    try {
      apiInstance.getOpenApiEndpointOpenapiJsonGet();
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getOpenApiEndpointOpenapiJsonGet");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

