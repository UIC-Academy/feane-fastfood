from django.db import models

from django.core.validators import MaxValueValidator, MinValueValidator


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Food(BaseModel):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to="food_images/", null=True, blank=True)
    category = models.ForeignKey("Category", on_delete=models.PROTECT, related_name="foods")
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"Food(name={self.name})"
    

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"
    

class Booking(BaseModel):
    user_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()
    num_of_people = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(7)])
    datetime = models.DateTimeField()
    is_request_verified = models.BooleanField(default=False)
    is_they_actually_come = models.BooleanField(default=False)

    def __str__(self):
        return f"Booking(name={self.user_name})"
    
    class Meta:
        verbose_name = "Booking"
        verbose_name_plural = "Bookings"


class Feedback(BaseModel):
    user = models.ForeignKey("auth.User", on_delete=models.PROTECT, related_name="feedbacks")
    message = models.CharField(max_length=500)
    stars = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])

    def __str__(self):
        return f"Feedback(message={self.message[:10]})"
    
    class Meta:
        verbose_name = "Feedback"
        verbose_name_plural = "Feedbacks"