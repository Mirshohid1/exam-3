from django.db import models
import random, os


# for the post
class Post(models.Model):
    name = models.CharField(max_length=200)
    date = models.DateField(auto_now_add=True)
    description = models.TextField()
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True, blank=True)
    categories = models.ManyToManyField('Category', related_name='posts')
    tags = models.ManyToManyField('Tag', related_name='posts')

    def displaying_descriptions_with_images(self):
        words = self.description.split()[:29]
        return ' '.join(words) + ' ...' if len(words) == 29 else self.description

    def displaying_descriptions_without_images(self):
        words = self.description.split()[:44]
        return ' '.join(words) + ' ...' if len(words) == 44 else self.description

    def __str__(self):
        return self.name

class Author(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    flag_about = models.BooleanField(default=False)

    bio = models.TextField(null=True, blank=True)
    experience = models.TextField(null=True, blank=True)
    photo = models.ImageField(upload_to='photos_authors', null=True, blank=True)
    photo_full = models.ImageField(upload_to='full_photo_author', null=True, blank=True)

    def split_bio_return_left(self):
        if self.bio:
            word = self.bio.split('.')
            word = word[:-1]
            mid = len(word) // 2

            return ''.join(word[:mid])
        return []

    def split_bio_return_right(self):
        if self.bio:
            word = self.bio.split('.')
            word = word[:-1]
            mid = len(word) // 2

            return ''.join(word[mid:])
        return []

    def split_experience_return_left(self):
        if self.experience:
            word = self.experience.split('.')
            word = word[:-1]
            mid = len(word) // 2

            return ''.join(word[:mid])
        return []

    def split_experience_return_right(self):
        if self.experience:
            word = self.experience.split('.')
            word = word[:-1]
            mid = len(word) // 2

            return ''.join(word[mid:])
        return []

    def return_random_quote(self):
        quotes = self.quotes.all()
        return random.choice(quotes).quote if quotes.exists() else "У автора нет цитат."

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Image(models.Model):
    image = models.ImageField(upload_to='post_images/')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True, blank=True, related_name='images')

class Comment(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    comment = models.TextField()
    public_date = models.DateField(auto_now=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')

# for the about
class Quote(models.Model):
    number = models.IntegerField()
    quote = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True, blank=True, related_name='quotes')

class Skill(models.Model):
    skill = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True, blank=True, related_name='skills')

# for the contact
class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return f"Message from {self.name}"