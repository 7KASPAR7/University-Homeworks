package ru.spbu.apmath.prog.hw1.task1;

import java.util.Scanner;

public class Binarshina {
    public static void main(String[] args) {
        System.out.println("Введите число: ");
        Scanner sc = new Scanner(System.in);
        try{
            int num = sc.nextInt();
            Converter con = new Converter(num);
            System.out.println(con.toBinary());
        }
        catch (java.util.InputMismatchException k) {
            System.out.println("Введите целое число ");
        }
        catch (IllegalArgumentException k) {
            System.out.println("Введите положительное число ");
        }
    }
}
