from django.db import models
from django.conf import settings
from django.utils.encoding import python_2_unicode_compatible
from django.contrib.auth.models import AbstractUser, Group, Permission
import uuid

class UUIDUser(AbstractUser):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    groups = models.ManyToManyField(Group, blank=True, related_name="uuiduser_set", related_query_name="user")
    user_permissions = models.ManyToManyField(Permission, blank=True, related_name="uuiduser_set", related_query_name="user")

    def __str__(self):
        return self.first_name

    class Meta:
        verbose_name = 'usuário'
        verbose_name_plural = 'usuários'

# CreateUpdateModel
# - - - - - - - - - - - - - - - - - - -
class CreateUpdateModel(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField('criado em', auto_now_add=True)
    updated_at = models.DateTimeField('atualizado em', auto_now=True)

    class Meta:
        abstract = True

class Propose(CreateUpdateModel):
	name = models.CharField(verbose_name = 'nome', max_length = 50)
	propost = models.TextField(verbose_name = 'proposta')
	up = models.IntegerField(verbose_name = 'positivo', default=0)
	down = models.IntegerField(verbose_name = 'negativo', default=0)

	def __str__(self):
		return self.name

	def vote_up(self):
		up += 1
		return True

	def vote_down(self):
		down += 1
		return True

	class Meta:
		verbose_name = 'proposta'
		verbose_name_plural = 'propostas'

# Comment
# - - - - - - - - - - - - - - - - - - -
class Comment(CreateUpdateModel):
	comment = models.TextField(verbose_name = 'comentário')
	id_user = models.ForeignKey(UUIDUser, on_delete = models.CASCADE, related_name = 'comentários1')
	id_prop = models.ForeignKey(Propose, on_delete = models.CASCADE, related_name = 'comentários2')
