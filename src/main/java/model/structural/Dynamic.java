package model.structural;

import java.util.*;

/**
 * Dynamic is a glorified byte wrapper,
 * which allows for a little more dress
 * and prevents problems down the line
 * with arguments to constructors.
 */
public class Dynamic implements Comparator<Dynamic>, Comparable<Dynamic> {

    /* Useful variable bounds */
    public static int MIN_DYNAMIC = 0;
    public static int MAX_DYNAMIC = 100;

    /**
     * Stores the loudness of this Dynamic
     */
    private final byte value;

    /**
     * Constructor taking in a loudness value.
     * @param value The pitch's loudness value.
     */
    public Dynamic(int value) {
        if(value >= MIN_DYNAMIC && value <= MAX_DYNAMIC) {
            this.value = (byte)value;
        }
        else {
            throw new Error("Invalid dynamic range!");
        }
    }

    /**
     * Copy constructor for Dynamic.
     * @param other The other Dynamic.
     */
    public Dynamic(Dynamic other) {
        this.value = other.value;
    }

    /**
     * Compares this Dynamic to another Dynamic.
     * @param other The other Dynamic.
     * @return The comparison.
     */
    @Override
    public int compareTo(Dynamic other) {
        return Byte.compare(value,other.value);
    }

    /**
     * Compares two Dynamics.
     * @param p1 The first Dynamic.
     * @param p2 The second Dynamic.
     * @return The comparison.
     */
    @Override
    public int compare(Dynamic p1, Dynamic p2) {
        return Byte.compare(p1.value,p2.value);
    }

    /**
     * Checks if this Dynamic equals another Object.
     * @param o The other Object.
     * @return If this Dynamic is equal to the Object.
     */
    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;
        Dynamic dynamic = (Dynamic) o;
        return value == dynamic.value;

    }

    /**
     * A simple hash code for storage of Dynamics in special Collections.
     * @return The hash code for this Dynamic.
     */
    @Override
    public int hashCode() {
        return (int) value;
    }
}