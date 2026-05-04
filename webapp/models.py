from django.db import models


class Member(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
    ]

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    date_joined = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

    # String representation method , this controls how object appears in django admin 
    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Trainer(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    specialization = models.CharField(max_length=150)
    phone = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class MembershipPlan(models.Model):
    name = models.CharField(max_length=100)
    duration_months = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name

#Member + Plan 
class Membership(models.Model):
  #on_delete=models.CASCADE > if Memeber is deleted > Memberships are also deleted
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    plan = models.ForeignKey(MembershipPlan, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.member} - {self.plan}"


class GymClass(models.Model):
    name = models.CharField(max_length=100)
    trainer = models.ForeignKey(Trainer, on_delete=models.SET_NULL, null=True)
    schedule_time = models.DateTimeField()
    max_capacity = models.IntegerField()

    def __str__(self):
        return self.name


class Booking(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    gym_class = models.ForeignKey(GymClass, on_delete=models.CASCADE)
    booked_at = models.DateTimeField(auto_now_add=True)

#Unique constraint 
#Prevent duplicate booking

    class Meta:
        unique_together = ('member', 'gym_class')

    def __str__(self):
        return f"{self.member} -> {self.gym_class}"
