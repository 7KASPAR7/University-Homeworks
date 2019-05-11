package ru.spbu.apmath.prog.hw2.task1;

public class DiscountSum {
    public int shopDiscount;

    public DiscountSum(int shopDiscount) {
        this.shopDiscount = shopDiscount;
    }

    public int sumDiscount(int shopDiscount) {
        int discount = shopDiscount;
        int sum = 0;
        if (shopDiscount<0){
            throw new IllegalArgumentException("Нужно положительное число");
        }
        while (discount >= 10) {
            while (discount != 0) {
                sum += (discount % 10);
                discount /= 10;
            }
            discount = sum;
            sum = 0;
        }
        return discount;
    }
}
