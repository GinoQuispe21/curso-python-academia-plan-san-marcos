import reflex as rx

class CounterState(rx.State):
    count:int = 0
    # event handlers
    def increment(self):
        self.count += 1
    def decrement(self):
        self.count -= 1