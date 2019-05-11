package ru.spbu.apmath.prog.hw2.task2;

public class Converter {
    private Translater word;

    public Converter(Translater word){
        this.word = word;
    }
    public int sumLetters(String word){
        word = word.replaceAll(" ", "");
    return word.length();
    }

}
