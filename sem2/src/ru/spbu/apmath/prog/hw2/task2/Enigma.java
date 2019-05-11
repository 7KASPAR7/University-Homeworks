package ru.spbu.apmath.prog.hw2.task2;


import java.util.Scanner;

public class Enigma {
    public static void main(String[] args) {
        int sum = 0;
        for (int i = 1; i <=1000 ; i++) {
            Translater word = new Translater(i);
            Converter con = new Converter(word);
            sum += con.sumLetters(word.translate(i));
        }
        System.out.println(sum);
    }
}
