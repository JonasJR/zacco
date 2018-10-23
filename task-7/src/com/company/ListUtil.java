package com.company;

import java.util.*;

public class ListUtil {
    public void MergeSortedLists(LinkedList list1, LinkedList list2) {
        int total = list1.size() + list2.size();

        //First we ahve to check if the list is the int or the string lists
        //This asumes we do not send in the number in a string format...
        if (list1.peekFirst() instanceof Integer){
            List<Integer> result = new LinkedList<>();

            //loops through the two lists and compares the first elements and
            // pops it until one of the two lists are depleted
            while(list1.size() != 0 && list2.size() != 0){
                if ((Integer)list1.peekFirst() < (Integer)list2.peekFirst()){
                    result.add((Integer)list1.removeFirst());
                } else {
                    result.add((Integer)list2.removeFirst());
                }
            }
            //Add possible leftovers in lists
            result.addAll(list1);
            result.addAll(list2);

            //Just for demonstration
            for(int l : result){
                System.out.println(l);
            }
        } else {
            //I find that the time is not enough for me to complete a sorting of alphabetic order without using Collections
            List<String> result = new ArrayList<>(total);
            result.addAll(list1);
            result.addAll(list2);
            Collections.sort(result);

            //Just for demonstration
            for(String l : result){
                System.out.println(l);
            }
        }
    }
}
