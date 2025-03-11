package org.example;

import java.util.Scanner;

public class Exercicio01 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Insira a temperatura em Fahrenheit: ");

        float f = scanner.nextFloat();
        float c = (f-32)*((float) 5 /9);

        System.out.printf("%sºF = %sºC", f, c);
    }
}
