package org.example;

import java.util.*;

public class SentenceSimilarity2 {

    // ex 1
    // a b c
    // a b c

    // ex 2
    // a a c
    // d e c
    // [a, f] [f, d] [a e]
    // a, f, d, e -> 1
    // c -> 2

    public boolean areSentencesSimilarTwo(String[] sentence1, String[] sentence2, List<List<String>> similarPairs) {

        Map<String, Integer> components = findConnections(sentence1, sentence2, similarPairs);

        if (sentence1.length != sentence2.length) {
            return false;
        }

        for(int i = 0; i < sentence1.length; i++) {
            int component1 = components.get(sentence1[i]);
            int component2 = components.get(sentence2[i]);
            if(component1 != component2) {
                return false;
            }
        }

        return true;
    }

    private Map<String, Integer> findConnections(String[] sentence1, String[] sentence2, List<List<String>> similarPairs) {

        Map<String, Integer> components = new HashMap<>();

        // loop through all words in sentence1 and sentence2 along with words in similarWords, by creating a set
        Map<String, List<String>> graph = new HashMap<String, List<String>>();

        for(List<String> pair: similarPairs) {
            String u = pair.get(0);
            String v = pair.get(1);
            List<String> uCons = graph.getOrDefault(u, new ArrayList<String>());
            uCons.add(v);
            graph.put(u, uCons);
            List<String> vCons = graph.getOrDefault(v, new ArrayList<String>());
            vCons.add(u);
            graph.put(v, vCons);
        }
        Set<String> nodes = new HashSet<String>();
        nodes.addAll(Arrays.asList(sentence1));
        nodes.addAll(Arrays.asList(sentence2));
        nodes.addAll(graph.keySet());
        int componentId = 0;
        HashSet<String> visited = new HashSet<>();
        for(String node: nodes) {
            if(!visited.contains(node)) {
                traverseAndAssign(node, graph, componentId, components, visited);
                componentId++;
            }
        }
        return components;
    }

    private void traverseAndAssign(String start, Map<String, List<String>> graph, int componentId, Map<String, Integer> components, Set<String> visited) {
        if(visited.contains(start)) {
            return;
        }
        components.put(start, componentId);
        visited.add(start);
        List<String> child = graph.getOrDefault(start, Collections.emptyList());
        for(String v: child) {
            traverseAndAssign(v, graph, componentId, components, visited);
        }
    }
}
