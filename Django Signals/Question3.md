####  Question 3: Do Django signals run in the same database transaction as the caller?


#### Explaination 
- Yes, by default Django signals run within the same database transaction, especially pre_save and post_save.

- The signal fires and sees the user (signal runs within transaction).

- After rollback, the user no longer exists (proof that signal shared the transaction context).

#### apps/signals.py
```python 
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.db import connection

@receiver(post_save, sender=User)
def user_created_signal(sender, instance, **kwargs):
    print("Signal triggered: User in DB?", User.objects.filter(id=instance.id).exists())
```

app/views.py
```python 
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.db import transaction

def create_user_with_rollback(request):
    try:
        with transaction.atomic():
            user = User.objects.create(username="rollback_user")
            raise Exception("Force rollback")
    except Exception as e:
        print("Exception occurred:", e)

    user_exists = User.objects.filter(username="rollback_user").exists()
    print("User still in DB after rollback?", user_exists)
    return HttpResponse("Check terminal")
```

#### Output:
```bash
Signal triggered: User in DB? True
Exception occurred: Force rollback
User still in DB after rollback? False
```
