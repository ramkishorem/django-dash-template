from autoslug import AutoSlugField

from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.conf import settings
from django.core.exceptions import ValidationError


class EntityAllFather(models.Model):
    name = models.CharField(_('Name'), max_length=255, primary_key=True)

    def __str__(self):
        return self.name

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        if not(self.name):
            raise ValidationError(_('%s name cannot be empty'%self._meta.model_name))
        super(EntityAllFather, self).save(*args, **kwargs)


class SlugifiedEntity(EntityAllFather):
    slug = AutoSlugField(_('Slug'), populate_from='name',
        unique = True)

    class Meta:
        abstract = True


class SingletonModel(models.Model):
    """Singleton Django Model
    Ensures there's always only one entry in the database, and can fix the
    table (by deleting extra entries) even if added via another mechanism.
    Also has a static load() method which always returns the object - from
    the database if possible, or a new empty (default) instance if the
    database is still empty. If your instance has sane defaults (recommended),
    you can use it immediately without worrying if it was saved to the
    database or not.
    Useful for things like system-wide user-editable settings.
    """

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        """
        Save object to the database. Removes all other entries if there
        are any.
        """
        self.__class__.objects.exclude(id=self.id).delete()
        super(SingletonModel, self).save(*args, **kwargs)

    @classmethod
    def load(cls):
        """
        Load object from the database. Failing that, create a new empty
        (default) instance of the object and return it (without saving it
        to the database).
        """

        try:
            return cls.objects.get()
        except cls.DoesNotExist:
            return cls()
