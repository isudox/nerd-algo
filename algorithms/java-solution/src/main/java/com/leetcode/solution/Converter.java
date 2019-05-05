package com.leetcode.solution;

import com.fasterxml.jackson.annotation.JsonInclude;
import com.fasterxml.jackson.core.JsonFactory;
import com.fasterxml.jackson.core.JsonGenerator;
import com.fasterxml.jackson.core.JsonParser;
import com.fasterxml.jackson.core.type.TypeReference;
import com.fasterxml.jackson.databind.DeserializationFeature;
import com.fasterxml.jackson.databind.JavaType;
import com.fasterxml.jackson.databind.ObjectMapper;
import com.fasterxml.jackson.databind.SerializationFeature;
import java.io.InputStream;
import java.io.StringWriter;
import java.util.Arrays;
import java.util.Collection;
import java.util.HashMap;
import java.util.Map;

/**
 * Convenient converters for LeetCode data structure.
 */
public final class Converter {

    /**
     * Convert an array to {@link ListNode}.
     *
     * @param nums An array of int.
     * @return ListNode
     */
    public static ListNode convertListNode(int[] nums) {
        int len = nums.length;

        if (len == 0) {
            return null;
        }

        ListNode node = new ListNode(0);
        node.val = nums[0];
        node.next = convertListNode(Arrays.copyOfRange(nums, 1, len));

        return node;
    }

    public static int[] convertArray(ListNode listNode) {
        if (null == listNode) {
            return null;
        }

        int size = getSize(listNode);
        int[] nums = new int[size];
        for (int i = 0; i < size; i++) {
            nums[i] = listNode.val;
            listNode = listNode.next;
        }

        return nums;
    }

    public static int getSize(ListNode listNode) {
        if (null == listNode) {
            return 0;
        }

        int length = 0;
        while (null != listNode) {
            length++;
            listNode = listNode.next;
        }

        return length;
    }

    public static String printListNode(ListNode listNode) {
        StringBuilder out = new StringBuilder();
        while (listNode != null) {
            out.append(listNode.val).append(", ");
            listNode = listNode.next;
        }
        return out.toString();
    }

    @SuppressWarnings("unchecked")
    public static <T> T[] collToArr(Collection<T> list) {
        T[] array = (T[]) new Object[list.size()];
        return list.toArray(array);
    }

    private static ObjectMapper mapper = new ObjectMapper();

    static {
        mapper.configure(SerializationFeature.WRITE_DATES_AS_TIMESTAMPS, false);
        mapper.configure(DeserializationFeature.FAIL_ON_UNKNOWN_PROPERTIES, false);
        mapper.configure(JsonParser.Feature.ALLOW_UNQUOTED_CONTROL_CHARS, true);
        mapper.configure(JsonParser.Feature.ALLOW_SINGLE_QUOTES, true);
        mapper.setSerializationInclusion(JsonInclude.Include.NON_NULL);
    }

    @SuppressWarnings("unchecked")
    public static Map<String, Object> readValue(String str) throws Throwable {
        return mapper.readValue(str, HashMap.class);
    }

    public static <T> T readValue(String str, Class<T> cls) throws Throwable {
        return mapper.readValue(str, cls);
    }

    @SuppressWarnings("unchecked")
    public static <T> T readValue(String str, TypeReference<T> t) throws Throwable {
        return mapper.readValue(str, t);
    }

    @SuppressWarnings("unchecked")
    public static <T> T readValue(String str, JavaType t) throws Throwable {
        return mapper.readValue(str, t);
    }

    public static <T> T readValue(InputStream is, Class<T> cls) throws Throwable {
        return mapper.readValue(is, cls);
    }

    @SuppressWarnings("unchecked")
    public static <T> T readValue(Object object, Class<T> cls) throws Throwable {
        return mapper.convertValue(object, cls);
    }

    public static <T> String writeValue(T o) throws Throwable {
        return mapper.writeValueAsString(o);
    }

    public static <T> String writeValue(T o, boolean pretty) throws Throwable {
        StringWriter sw = new StringWriter();
        JsonGenerator generator = getFactory().createGenerator(sw);
        if (pretty) {
            generator.useDefaultPrettyPrinter();
        }
        mapper.writeValue(generator, o);
        return sw.toString();
    }

    public static JsonFactory getFactory() {
        return mapper.getFactory();
    }

    public static ObjectMapper getObjectMapper() {
        return mapper;
    }

    public static void main(String[] args) {
        int[] array = new int[] {1, 2, 3, 4, 5, 6};
        ListNode listNode = convertListNode(array);
        System.out.println(Arrays.toString(array));
        System.out.println(printListNode(listNode));
        System.out.println(Arrays.toString(convertArray(listNode)));
        System.out.println(getSize(listNode));
    }
}
