package ru.spbu.apmath.prog.hw2.task1;

import java.util.Scanner;

public class Discount  {
    public static void main(String[] args) {
        System.out.println("Введите 'маркетинговую' скидку в процентах: ");
        Scanner sc = new Scanner(System.in);
        try{
            int shopDiscount = sc.nextInt();
            DiscountSum sum = new DiscountSum(shopDiscount);
            System.out.println("Реальная скидка составляет");
            System.out.println(sum.sumDiscount(shopDiscount));
            System.out.println("процентов");
        }
        catch (java.util.InputMismatchException k) {
            System.out.println("Введите целое число ");
        }
        catch (IllegalArgumentException k) {
            System.out.println("Введите положительное число ");
        }
    }
}