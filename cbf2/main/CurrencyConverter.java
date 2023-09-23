//package com.codingblackfemales;
import java.util.HashMap;


public class CurrencyConverter{

        //Initialization of variables
        private String sourceCurrencyCode;
        private String destinationCurrencyCode;
        private double amount, source, destination;

        public CurrencyConverter(String sourceCurrencyCode, String destinationCurrencyCode, double amount){
            this.sourceCurrencyCode = sourceCurrencyCode;
            this.destinationCurrencyCode =destinationCurrencyCode;
            this.amount = amount;
        }

        // method to return an array of currency codes
        public String[] getCurrencyCodes(){
            return new String[] {"USD", "EUR", "GBP","JPY"};
        }

        // method returns the exchange rate between the source and destination code
        public double getExchangeRate(String sourceCurrencyCode, String destinationCurrencyCode){
            double source = CurrenciesGBP.exchangeRates.get(sourceCurrencyCode);
            double destination = CurrenciesGBP.exchangeRates.get(destinationCurrencyCode);
            return destination / source ; 
        }

        // method to calculate and return the converted amount in the destination currency
        public double convertCurrency() {
             return amount * getExchangeRate(sourceCurrencyCode, destinationCurrencyCode);
        }

}