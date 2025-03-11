package org.example;

import javax.sound.midi.SysexMessage;
import java.util.Scanner;

public class Exercicio05 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Insira a base do triângulo: ");
        float base = scanner.nextFloat();

        System.out.print("Insira a altura do triângulo: ");
        float altura = scanner.nextFloat();

        float area = (base * altura) / 2;
        System.out.print("Area do triângulo: "+ area);
    }
}
