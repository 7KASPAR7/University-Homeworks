package ru.spbu.apmath.prog.hw1.task3;

import java.util.List;
import java.util.ArrayList;

public class RotateFunc {
    public static void main(String[] args) {
        List<Integer> lst1 = new ArrayList();
        lst1.add(1);
        lst1.add(2);
        lst1.add(3);
        lst1.add(4);
        System.out.println("Your List: "+ lst1);
        List<Integer> lst2 = rotate(lst1);
        System.out.println("Rotated List: " + lst2);
    }
    public static List<Integer> rotate(List<Integer> lst) {
        List<Integer> answer = lst;
        if (answer.size() > 0){
            Integer element = answer.remove(answer.size() - 1);
        answer.add(0, element);
    }
        return answer;
    }
}
