/*
 * FastAPI
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 0.1.0
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */


package org.openapitools.client.api;

import org.openapitools.client.ApiException;
import org.openapitools.client.model.HTTPValidationError;
import org.junit.jupiter.api.Disabled;
import org.junit.jupiter.api.Test;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * API tests for DefaultApi
 */
@Disabled
public class DefaultApiTest {

    private final DefaultApi api = new DefaultApi();

    /**
     * Carica Parola
     *
     * API per caricare una parola nel dizionario.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void caricaParolaCaricaParolaParolaPostTest() throws ApiException {
        String parola = null;
        api.caricaParolaCaricaParolaParolaPost(parola);
        // TODO: test validations
    }

    /**
     * Correggi Parola
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void correggiParolaCorreggiParolaParolaPostTest() throws ApiException {
        String parola = null;
        api.correggiParolaCorreggiParolaParolaPost(parola);
        // TODO: test validations
    }

    /**
     * Read Docs
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void readDocsDocsGetTest() throws ApiException {
        api.readDocsDocsGet();
        // TODO: test validations
    }

}
