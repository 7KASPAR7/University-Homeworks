package ru.spbu.apmath.prog.hw1.task3;

import java.util.ArrayList;
import java.util.List;

public class RotateFunc {
    public static void main(String[] args) {
        List lst1 = new ArrayList();
        lst1.add(1);
        lst1.add(2);
        lst1.add(3);
        lst1.add(4);
        System.out.println("Your List: "+ lst1);
        ArrayList lst2 = rotate((ArrayList) lst1);
        System.out.println("Rotated List: " + lst2);
    }
    public static ArrayList rotate(ArrayList lst) {
        Object element = lst.remove(lst.size()-1);
        lst.add(0,element);
        return lst;
    }
}
