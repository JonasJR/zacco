package com.company;

public class Main {

    public static void main(String[] args) {
    DeadLock deadLock = new DeadLock();
    deadLock.thread1.start();
    deadLock.thread2.start();
    }
}
