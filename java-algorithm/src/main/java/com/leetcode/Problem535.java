package com.leetcode;

import java.util.HashMap;
import java.util.Map;
import java.util.Random;

/**
 * 535. Encode and Decode TinyURL
 * https://leetcode.com/problems/encode-and-decode-tinyurl/
 */
public class Problem535 {
    private static class Codec {

        private String alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789";
        private static final String BASE_URL = "https://tinyurl.com/";
        private final Random rand = new Random();
        private String key = getKey();
        private final Map<String, String> map = new HashMap<>();

        // Encodes a URL to a shortened URL.
        public String encode(String longUrl) {
            while (map.containsKey(key)) {
                key = getKey();
            }
            map.put(key, longUrl);
            return BASE_URL + key;
        }

        // Decodes a shortened URL to its original URL.
        public String decode(String shortUrl) {
            String key = shortUrl.substring(BASE_URL.length());
            return map.getOrDefault(key, "");
        }

        private String getKey() {
            StringBuilder sb = new StringBuilder();
            for (int i = 0; i < 6; i++) {
                sb.append(alphabet.charAt(rand.nextInt(62)));
            }
            return sb.toString();
        }
    }
}
