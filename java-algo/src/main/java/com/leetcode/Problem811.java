package com.leetcode;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * 811. Subdomain Visit Count
 * https://leetcode.com/problems/subdomain-visit-count/
 */
public class Problem811 {
    public List<String> subdomainVisits(String[] cpdomains) {
        Map<String, Integer> store = new HashMap<>();
        for (String domain : cpdomains) {
            String[] segments = domain.split(" ");
            int cnt = Integer.parseInt(segments[0]);
            String[] subDomains = segments[1].split("\\.");
            String url = "";
            for (int i = subDomains.length - 1; i >= 0; i--) {
                url = subDomains[i] + (i == subDomains.length - 1 ? "" : "." + url);
                store.put(url, cnt + store.getOrDefault(url, 0));
            }
        }
        List<String> ans = new ArrayList<>();
        for (Map.Entry<String, Integer> entry : store.entrySet()) {
            ans.add(entry.getValue() + " " + entry.getKey());
        }
        return ans;
    }
}
