package com.company;

import java.util.Arrays;
import java.util.LinkedList;
import java.util.List;

public class Main {

    public static void main(String[] args) {
        List<String> stringArrayList1 = Arrays.asList("Adam", "Anders", "Bertil", "Boris", "Carl", "David", "Dennis", "Peter", "Rasbert", "Ronny", "Sonny", "Sören");
        List<String> stringArrayList2 = Arrays.asList("Anja", "Anna", "Berit", "Bodil", "Carina", "Cecilia", "Doris", "Penny", "Rosalyn", "Signe", "Svetlana", "Tuva", "Sanna");
        LinkedList<String> stringList1 = new LinkedList<>();
        LinkedList<String> stringList2 = new LinkedList<>();
        stringList1.addAll(stringArrayList1);
        stringList2.addAll(stringArrayList2);

        List<Integer> intArrayList1 = Arrays.asList(12, 14, 45, 67, 98, 123, 134, 345, 456, 569, 748, 1123, 5757 , 11111, 3636363);
        List<Integer> intArrayList2 = Arrays.asList(9, 15, 17, 34, 44, 49, 97, 100, 105, 122, 133, 423, 465, 2929, 48484, 3637632);
        LinkedList<Integer> intList1 = new LinkedList<>();
        LinkedList<Integer> intList2 = new LinkedList<>();
        intList1.addAll(intArrayList1);
        intList2.addAll(intArrayList2);

        ListUtil listUtil = new ListUtil();
	    listUtil.MergeSortedLists(stringList1, stringList2);
	    listUtil.MergeSortedLists(intList1, intList2);
    }
}
