package ru.spbu.apmath.prog.hw1.task1;

public class Converter {
    public int value;

    public Converter(int value){
        this.value=value;
    }
    public String toBinary(){
        String answer ="";
        if (this.value<0){
            throw new IllegalArgumentException("Нужно положительное число");
        }
        if (this.value==0) {
            return answer;
        }
    while (this.value!=0){
        if (this.value%2==0){
            answer = "0" + answer;
        } else {
            answer = "1" + answer;
        }
        this.value = this.value/2;
    }
        return answer;
    }
}
