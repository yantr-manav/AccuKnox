#### Question 1: By default are django signals executed synchronously or asynchronously? Please support your answer with a code snippet that conclusively proves your stance. The code does not need to be elegant and production ready, we just need to understand your logic.


- Yes, Django signals are executed synchronously by default.
When a signal is sent, the receiver is executed immediately before the next line of the sender continues.


#### apps/signals.py
```python 
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
import time

@receiver(post_save, sender=User)
def user_created_signal(sender, instance, created, **kwargs):
    print("Signal START")
    time.sleep(5)  # Simulate delay
    print("Signal END")


```
#### apps/views.py
```python 
from django.contrib.auth.models import User
from django.http import HttpResponse
import time

def create_user_view(request):
    print("View START")
    User.objects.create(username='test_user')
    print("View END")
    return HttpResponse("Done")

```

#### OUPUT:

```bash
View START
Signal START
(wait 5 seconds)
Signal END
View END

```