from abc import ABC, abstractmethod


class Subscriber(ABC):

    def __init__(self):
        pass

    @abstractmethod
    def update(self):
        pass


class Publisher:
    def __init__(self):

        self.subscribers = []

    def notify(self) -> None:
        
        if len(self.subscribers) == 0:
            print("I don't have subscribers :( ")

        for subscriber in self.subscribers:
            subscriber.update()

    def register_subscriber(self, subscriber: Subscriber) -> None:
        self.subscribers.append(subscriber)

    def unregister_subscriber(self, subscriber: Subscriber) -> None:
        self.subscribers.remove(subscriber)


class Subscriber1(Subscriber):

    def __init__(self):

        self.call_no = 0
    
    def update(self):
        self.call_no += 1
        print(f"I am a subscriber 1! Call count is: {self.call_no}")


class Subscriber2(Subscriber):

    def __init__(self):

        self.call_no = 0
    
    def update(self):
        self.call_no += 1
        print(f"I am a subscriber 2! Call count is: {self.call_no}")


if __name__ == "__main__":
    
    publisher = Publisher()
    publisher.notify()
    
    subscriber1 = Subscriber1()
    subscriber2 = Subscriber2()

    publisher.register_subscriber(subscriber1)
    publisher.notify()

    publisher.register_subscriber(subscriber2)
    publisher.notify()
    publisher.notify()

    publisher.unregister_subscriber(subscriber1)
    publisher.notify()
