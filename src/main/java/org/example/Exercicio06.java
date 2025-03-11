package org.example;

import java.util.Scanner;
import java.lang.Math;

public class Exercicio06 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        float a = 0;

        while (true) {
            System.out.print("Digite o valor de A: ");
            a = scanner.nextFloat();
            if (a != 0){
                break;
            }
            System.out.println("A não pode ser 0!");
        }

        System.out.print("Digite o valor de B: ");
        float b = scanner.nextFloat();

        System.out.print("Digite o valor de C: ");
        float c = scanner.nextFloat();

        float delta = (b*b) - (4*a*c);
        float raizDelta = (float) Math.sqrt(delta);

        float x1 = (b*(-1) + raizDelta) / (2*a);

        System.out.printf("Equação: %sx² + %sx + %s = 0\n", a, b,c);

        System.out.println("Delta (Δ) = " + delta);

        if (delta > 0) {
            float x2 = (b*(-1) - raizDelta) / (2*a);
            System.out.printf("\nS = {%s, %s}", x1, x2);
        } else if (delta == 0) {
            System.out.printf("\nS = {%s}", x1);
        } else {
            System.out.print("A equação não possui raízes reais.");
        }
    }
}
