from graphene_django.types import DjangoObjectType
import graphene
from .models import Member

class MemberType(DjangoObjectType):
    class Meta:
        model=Member
class Query(graphene.ObjectType):
    all_members=graphene.List(MemberType)

    def resolve_all_members(self, info, **kwargs):
        return Member.objects.all()


