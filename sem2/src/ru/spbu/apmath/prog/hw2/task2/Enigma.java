package ru.spbu.apmath.prog.hw2.task2;


import static ru.spbu.apmath.prog.hw2.task2.Converter.sumLetters;

public class Enigma {
    public static void main(String[] args) {
        int sum = 0;
        for (int i = 1; i <=1000 ; i++) {
            Translater word = new Translater(i);
            sum += sumLetters(word.translate(i));
        }
        System.out.println(sum);
    }
}
