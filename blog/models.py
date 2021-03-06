from django.db import models
from django.utils.translation import gettext_lazy as _


class AuthorModel(models.Model):
    first_name = models.CharField(
        max_length=100,
        verbose_name=_('first name')
    )
    last_name = models.CharField(
        max_length=100,
        verbose_name=_('last name')
    )
    avatar = models.ImageField(
        upload_to='author-avatars/',
        verbose_name=_('avatar')
    )

    @property
    def full_name(self):
        return '{} {}'.format(self.first_name, self.last_name)

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = _('author')
        verbose_name_plural = _('authors')


class BlogTagModel(models.Model):
    title = models.CharField(
        max_length=100,
        verbose_name=_('title')
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('tag')
        verbose_name_plural = _('tags')


class BlogPostModel(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name=_('title')
    )
    description = models.TextField(
        verbose_name=_('description')
    )
    main_image = models.ImageField(
        upload_to='blog-post-img/',
        verbose_name=_('main imag')
    )
    banner = models.ImageField(
        upload_to='blog-post-img/',
        verbose_name=_('banner')
    )
    author = models.ForeignKey(
        AuthorModel,
        on_delete=models.RESTRICT,
        related_name='posts',
        verbose_name=_('author')
    )
    tags = models.ManyToManyField(
        BlogTagModel,
        related_name='posts',
        verbose_name=_('tags')
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_('created at')
    )

    def __str__(self):
        return '{} ...'.format(self.title[:100])

    class Meta:
        verbose_name = _('blog')
        verbose_name_plural = _('blogs')


class CommentModel(models.Model):
    post = models.ForeignKey(
        BlogPostModel,
        on_delete=models.CASCADE,
        related_name='comments',
        verbose_name=_('post')
    )
    name = models.CharField(
        max_length=63,
        verbose_name=_('name')
    )
    email = models.EmailField(
        verbose_name=_('email')
    )
    phone = models.CharField(
        max_length=13,
        verbose_name=_('phone')
    )
    comment = models.TextField(
        verbose_name=_('comment')
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_('created at')
    )

    class Meta:
        verbose_name = _('comment')
        verbose_name_plural = _('comments')

    def __str__(self):
        return self.name