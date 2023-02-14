#
# @lc app=leetcode id=1195 lang=python3
#
# [1195] Fizz Buzz Multithreaded
#

# @lc code=start
# 这段代码通过使用四个Semaphore信号量，将FizzBuzz游戏中的数字分类输出逻辑进行了并发控制
# 如果多个线程同时调用number方法，由于Semaphore信号量的机制，
# 每个线程将依次获取资源，并根据当前数字的分类请求、释放对应的Semaphore信号量，保证输出的正确性

import threading 
class FizzBuzz:
    def __init__(self, n: int):
        self.n = n+1
        self.Fizz=threading.Semaphore(0)
        self.Fizzbuzz=threading.Semaphore(0)
        self.Buzz=threading.Semaphore(0)
        self.Num=threading.Semaphore(1)

    # printFizz() outputs "fizz"
    def fizz(self, printFizz: 'Callable[[], None]') -> None:
        for i in range(1,self.n):
            if i%3 ==0 and i%5 !=0:
                self.Fizz.acquire()
                printFizz()
                self.Num.release()

    # printBuzz() outputs "buzz"
    def buzz(self, printBuzz: 'Callable[[], None]') -> None:
        for i in range(1,self.n):
            if i%3 !=0 and i%5==0:
                self.Buzz.acquire()
                printBuzz()
                self.Num.release()

    # printFizzBuzz() outputs "fizzbuzz"
    def fizzbuzz(self, printFizzBuzz: 'Callable[[], None]') -> None:
        for i in range(1,self.n):
            if i%3==0 and i%5==0:
                self.Fizzbuzz.acquire()
                printFizzBuzz()
                self.Num.release()

    # printNumber(x) outputs "x", where x is an integer.
    def number(self, printNumber: 'Callable[[int], None]') -> None:
        for i in range(1,self.n):
            self.Num.acquire() # 请求一个资源，Semaphore计数器减1，以保证只有一个线程能够访问接下来的逻辑

            if i%3==0 and i%5==0:
                self.Fizzbuzz.release() # 释放一个FizzBuzz信号量（Semaphore计数器加1），唤醒正在等待FizzBuzz输出的线程
            elif i%3==0:
                self.Fizz.release()
            elif i%5==0:
                self.Buzz.release()
            else:
                printNumber(i)
                self.Num.release() # 释放一个Num信号量（Semaphore计数器加1）

# @lc code=end

