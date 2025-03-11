package org.example;

import java.util.Scanner;
import java.lang.Math;

public class Exercicio04 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Valor: ");
        float valor = scanner.nextFloat();

        double quadrado = Math.pow(valor, 2);
        double cubo = Math.pow(valor, 3);

        System.out.printf("Ao quadrado: %s\n", quadrado);
        System.out.printf("Ao cubo: %s", cubo);
    }
}
