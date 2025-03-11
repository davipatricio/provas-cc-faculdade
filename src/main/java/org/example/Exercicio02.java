package org.example;

import java.util.Scanner;

public class Exercicio02 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Insira a temperatura em Celsius: ");

        float c = scanner.nextFloat();
        float f = (c*9/5) + 32;

        System.out.printf("%sºC = %sºF", c, f);
    }
}
