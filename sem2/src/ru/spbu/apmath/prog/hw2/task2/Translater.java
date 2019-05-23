package ru.spbu.apmath.prog.hw2.task2;

public class Translater {
    public int number;
    private String word;
    // код писал самостоятельно

    public Translater(int number){
        this.number = number;
    }
    public String translate(int number){
        if (number<0){
            throw new IllegalArgumentException("Нужно положительное число");
        }
        word = "";
        if (number/100>0){
            int k = number / 100;
            if (k == 1){ word += "сто ";}
            if (k == 2){ word += "двести ";}
            if (k == 3){ word += "триста ";}
            if (k == 4){ word += "четыреста ";}
            if (k == 5){ word += "пятьсот ";}
            if (k == 6){ word += "шестьсот ";}
            if (k == 7){ word += "семьсот ";}
            if (k == 8){ word += "восемьсот ";}
            if (k == 9){ word += "девятьсот ";}
            if (k == 10){ word += "тысяча ";}
            number = number % 100;
        }
        if (number/10>1){
            int k = number/10;
            if (k == 2){ word += "двадцать ";}
            if (k == 3){ word += "тридцать ";}
            if (k == 4){ word += "сорок ";}
            if (k == 5){ word += "пятьдесят ";}
            if (k == 6){ word += "шестьдесят ";}
            if (k == 7){ word += "семьдесят ";}
            if (k == 8){ word += "восемьдесят ";}
            if (k == 9){ word += "девяносто ";}
        }
        if (number/10 == 1){
            int k = number;
            if (k == 10){ word += "десять";}
            if (k == 11){ word += "одиннадцать";}
            if (k == 12){ word += "двенадцать";}
            if (k == 13){ word += "тринадцать";}
            if (k == 14){ word += "четырнадцать";}
            if (k == 15){ word += "пятнадцать";}
            if (k == 16){ word += "шестнадцать";}
            if (k == 17){ word += "семнадцать";}
            if (k == 18){ word += "восемнадцать";}
            if (k == 19){ word += "девятнадцать";}
            } else{
               int k = number % 10;
                if (k == 1){ word += "один";}
                if (k == 2){ word += "два";}
                if (k == 3){ word += "три";}
                if (k == 4){ word += "четыре";}
                if (k == 5){ word += "пять";}
                if (k == 6){ word += "шесть";}
                if (k == 7){ word += "семь";}
                if (k == 8){ word += "восемь";}
                if (k == 9){ word += "девять";}

            }


        return word;

    }
}
