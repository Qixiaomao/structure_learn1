'''
从上图中可以看到生产者和消费者之间用中间类似一个队列一样的东西串起来。
这个队列可以想像成一个存放产品的“仓库”，生产者只需要关心这个“仓库”，
并不需要关心具体的消费者，对于生产者而言甚至都不知道有这些消费者存在。
对于消费者而言他也不需要关心具体的生产者，
到底有多少生产者也不是他关心的事情，
他只要关心这个“仓库”中还有没有东西。这种模型是一种松耦合模型。
'''
import time,threading,queue

class Consumer(threading.Thread):
    def __init__(self,queue):
        super().__init__()
        self._queue = queue
        
    # 继承了Thread类后，需要重写run方法来定义事件
    def run(self):
        while True:
            # msg是我们说的消息，也是仓库中的货物
            msg = self._queue.get()
            if isinstance(msg,str) and msg == 'quit':
                break
            print(f"我是线程，我接收到了{msg}")
        print("白白")
        
def producer():
    queue = queue.Queue()
    worker = Consumer(queue)
    worker.start()
    start_time = time.time()
    # 退出条件
    while time.time() - start_time < 5:
        queue.put('时间在%s' % time.time())
        time.sleep(1)
    queue.put('quit')
    worker.join()
    
if __name__ == '__main__':
    producer()