from django.db import models
from django.core.validators import MinLengthValidator, MaxLengthValidator

# Create your models here.

class Publisher(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    website = models.URLField()


class Book(models.Model):
    GENRE_CHOICE = (
        ("C", "Comedy"),
        ("T", "Tragede"),
        ("TC", "Tragicomedy"),
        ("CR", "Romance"),
        ("SF", "Science Fiction")
    )
    title = models.CharField(max_length=255)
    slug = models.SlugField(db_index=True, default='-')
    isbn = models.CharField(max_length=20)
    date_published = models.DateField()
    date_added = models.DateField(auto_now_add=True)
    edition = models.PositiveSmallIntegerField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    genre = models.CharField(max_length=2, choices=GENRE_CHOICE)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE, related_name="books")
    authors = models.ManyToManyField("Author", related_name="books")


class Author(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)


class Address(models.Model):
    number = models.PositiveIntegerField()
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    zipcode = models.CharField(max_length=5, validators=[MaxLengthValidator(5, "code must be five"),
                                                         MaxLengthValidator(6, "code can not exceed a length of 6")])
    publisher = models.OneToOneField(Publisher, on_delete=models.CASCADE)
