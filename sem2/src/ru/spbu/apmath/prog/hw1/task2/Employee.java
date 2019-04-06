package ru.spbu.apmath.prog.hw1.task2;

import java.util.Scanner;

public class Employee {
    private String name;
    private double hourly;
    private int hours;

    public Employee(String name, double hourly, int hours) {
        this.name = name;
        this.hourly = hourly;
        this.hours = hours;
    }

    private double get_Salary() {
        double salary;
        if (this.hourly<70 || this.hours>60) {
            salary = -1;
        }
        else if (this.hours<=40) {
            salary = this.hourly * this.hours;
        }
        else {
            salary = (40 * this.hourly) + (this.hours-40) * 1.5 * this.hourly;
        }
        return salary;
    }

    @Override
    public String toString() {
        if (this.get_Salary()<0){
            return (this.name + " " + this.hourly + " " + this.hours + " " + "ОШИБКА");
        }
        else {
            return (this.name + " " + this.hourly + " " + this.hours + " " + this.get_Salary());
        }
    }
    }

