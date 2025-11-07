import threading
from django.dispatch import Signal

test_signal = Signal()

def receiver_func(sender, **kwargs):
    print("Receiver thread:", threading.current_thread().name)

test_signal.connect(receiver_func)

print("Caller thread:", threading.current_thread().name)
test_signal.send(sender=None)



