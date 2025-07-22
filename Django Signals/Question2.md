#### Question 2: Do django signals run in the same thread as the caller? Please support your answer with a code snippet that conclusively proves your stance. The code does not need to be elegant and production ready, we just need to understand your logic.


#### Explainations 
Yes, Django signals run in the same thread as the code that triggers them.

In the given example, both the view and the signal print the same thread ID, proving that the signal is not executed in a separate thread. This confirms that Django signals are handled synchronously and in the same execution thread as the caller by default.


##### apps/signals.py
```python 
import threading
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User

@receiver(post_save, sender=User)
def user_created_signal(sender, instance, **kwargs):
    print(f"Signal Thread ID: {threading.get_ident()}")
```

apps/views.py
```python
from django.http import HttpResponse
from django.contrib.auth.models import User
import threading

def create_user_view(request):
    print(f"View Thread ID: {threading.get_ident()}")
    User.objects.create(username="thread_user")
    return HttpResponse("Done")
```

#### Output:

```bash
View Thread ID: 123456789
Signal Thread ID: 123456789
```