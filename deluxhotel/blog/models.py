from django.db import models
from django.urls import reverse


class TagsModel(models.Model):
    name = models.CharField(max_length=120, verbose_name='Тэг')
    slug = models.SlugField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Тэг'
        verbose_name_plural = 'Тэги'


class BlogPostModel(models.Model):
    title = models.CharField(max_length=120, verbose_name='Заголовок')
    author = models.CharField(max_length=120,
                              verbose_name='Автор',
                              null=True,
                              blank=True)
    publish_date = models.DateTimeField(verbose_name='Дата публикации')
    image = models.ImageField(verbose_name='Картинка',
                              upload_to='blog/%Y/%m/%d')
    text = models.TextField(verbose_name='Описание')
    tags = models.ManyToManyField(TagsModel, related_name='tags')
    slug = models.SlugField()
    active = models.BooleanField(verbose_name='Показывать?', default=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:detail', kwargs={'slug': self.slug})

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'


class CommentModel(models.Model):
    name = models.CharField(max_length=120, verbose_name='Имя')
    subject = models.CharField(max_length=120, verbose_name='Тема')
    email = models.EmailField(verbose_name='Почта')
    text = models.TextField(verbose_name='Текст комментария')
    date_publish = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(BlogPostModel,
                             on_delete=models.CASCADE,
                             related_name='post_comment')

    def __str__(self):
        return self.name + " -> " + self.email

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
        ordering = ['-date_publish']
