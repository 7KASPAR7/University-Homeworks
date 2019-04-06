package ru.spbu.apmath.prog.hw1.task2;

import java.util.Scanner;

public class DenegNet {
    public static void main(String[] args) {
        String name;
        double hourly;
        int hours;
        Scanner sc =new Scanner(System.in);
        System.out.println("Введите количество рабочих");
        int n = sc.nextInt();
        Employee[] employees = new Employee[n];
        for (int i=0; i<n; i++) {
            System.out.println("ФИО: ");
            sc.nextLine();
            name=sc.nextLine();
            System.out.println("Почасовая оплата: ");
            hourly=sc.nextDouble();
            System.out.println("Количество часов: ");
            hours=sc.nextInt();
            employees[i]=new Employee(name, hourly, hours);
    }
        for (int i=0; i<n; i++) {
            System.out.println(employees[i].toString());
        }
    }
}
