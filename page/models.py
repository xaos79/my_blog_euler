from django.db import models

class Article(models.Model):
	title=models.CharField(max_length=20)
	text=models.TextField()
	data=models.DateTimeField(auto_now_add=True)
	description=models.TextField(max_length=800)

	def __str__(self):
		return self.title

	class Meta:
		ordering=['title']

class Comment(models.Model):
	article=models.ForeignKey(Article, on_delete=models.CASCADE)
	text=models.TextField()
	data=models.DateTimeField(auto_now_add=True)
	person=models.CharField(max_length=150, blank=True)

	class Meta:
		ordering=['-data']

	def __str__(self):
		return self.article.title