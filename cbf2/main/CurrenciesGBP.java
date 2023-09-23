//package com.codingblackfemales;

import java.util.HashMap;

public class CurrenciesGBP{
    
    //Declaring the exchange rates map
    public static HashMap<String, Double> exchangeRates;

    static{
        //Initializing the exchange rates map
        exchangeRates = new HashMap<String, Double>(); 
        exchangeRates.put("GBP", 1.0);
        exchangeRates.put("EUR", 1.16);
        exchangeRates.put("USD", 1.31);
        exchangeRates.put("JPY", 181.78); 
    }
}