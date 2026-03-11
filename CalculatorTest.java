package com.ammar;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

public class CalculatorTest {

    Calculator calc = new Calculator();

    @Test
    void testAdd() {
        assertEquals(5, calc.add(2,3));
    }

    @Test
    void testSubtract() {
        assertEquals(2, calc.subtract(5,3));
    }

    @Test
    void testMultiply() {
        assertEquals(6, calc.multiply(2,3));
    }

    @Test
    void testDivide() {
        assertEquals(2, calc.divide(4,2));
    }

    @Test
    void testDivideByZero() {
        assertThrows(
                IllegalArgumentException.class,
                () -> calc.divide(5,0)
        );
    }

    @Test
    void testNegativeAdd() {
        assertEquals(-1, calc.add(-2,1));
    }

    @Test
    void testNegativeSubtract() {
        assertEquals(-4, calc.subtract(-1,3));
    }

    @Test
    void testNegativeMultiply() {
        assertEquals(-6, calc.multiply(-2,3));
    }

    @Test
    void testDivideNegative() {
        assertEquals(-2, calc.divide(-4,2));
    }

}