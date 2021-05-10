package com.common;

import org.slf4j.LoggerFactory;

public final class Logger {

    private static final org.slf4j.Logger LOGGER = LoggerFactory.getLogger(Logger.class);

    public static void log(String str) {
        LOGGER.info(str);
    }

    public static void log(String format, Object... arguments) {
        LOGGER.info(format, arguments);
    }
}
