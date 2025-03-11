package org.example;

import java.util.Scanner;

public class Exercicio03 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Insira seu peso (kg): ");
        float peso = scanner.nextFloat();

        System.out.print("Insira sua altura (m): ");
        float altura = scanner.nextFloat();

        float imc = peso / (altura * altura);

        System.out.printf("Seu IMC é: %s", imc);
    }
}
