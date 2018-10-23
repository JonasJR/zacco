package com.company;

public class DeadLock {
    static Object lock1 = new Object();
    static Object lock2 = new Object();

    //The threads will first aquire one lock each and then try to get the other lock but will wait for ever for the other to release it.
    Thread thread1 = new Thread("Thread 1"){
        public void run(){
            System.out.println("Thread 1 getting lock1");
                synchronized(lock1){
                    try {
                        sleep(100); //To make sure that the thread does not complete before the other thread starts
                    } catch (InterruptedException e) {
                        e.printStackTrace();
                    }
                    System.out.println("Thread 1 have lock1");
                    System.out.println("Thread 1 getting lock2");
                    synchronized(lock2){
                        System.out.println("Thread 1 have lock2");
                    }
            }
        }
    };

    Thread thread2 = new Thread("Thread 2"){
        public void run(){
            System.out.println("Thread 2 getting lock2");
            synchronized(lock2){
                try {
                    sleep(100);
                } catch (InterruptedException e) {
                    e.printStackTrace();
                }
                System.out.println("Thread 2 have lock2");
                System.out.println("Thread 2 getting lock1");
                synchronized(lock1){
                    System.out.println("Thread 2 have lock1");
                    }
                }
            }
    };
}
