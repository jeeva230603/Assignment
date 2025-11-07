import time
from django.dispatch import Signal

test_signal = Signal()

def receiver_func(sender, **kwargs):
    print("Receiver started")
    time.sleep(3)
    print("Receiver finished")

test_signal.connect(receiver_func)

print("Before sending signal")
test_signal.send(sender=None)
print("After sending signal")

