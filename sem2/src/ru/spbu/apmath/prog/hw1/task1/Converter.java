package ru.spbu.apmath.prog.hw1.task1;

public class Converter {
    public int value;

    public Converter(int value){
        this.value=value;
    }
    public String toBinary(){
        StringBuilder answer = new StringBuilder();
        int value = this.value;
        if (value<0){
            throw new IllegalArgumentException("Нужно положительное число");
        }
        if (value==0) {
            return "0";
        }
    while (value!=0){
        if (value%2==0){
            answer.insert(0, "0");
        } else {
            answer.insert(0, "1");
        }
        value = value/2;
    }
        return answer.toString();
    }
}
