from graphene_django.types import DjangoObjectType
import graphene
from .models import Member

class MemberType(DjangoObjectType):
    class Meta:
        model =Member
class Query(graphene.ObjectType):
    all_members =graphene.List(MemberType)

    def resolve_all_members(self, info, **kwargs):
        return Member.objects.all()

class MemberCreateMutation(graphene.Mutation):
    member = graphene.Field(MemberType)
    class Arguments:
        name =graphene.String(required=True)
        is_son = graphene.Boolean(required=True)
        household_count =graphene.Int(required=True)


    def mutate(self, info, name, is_son, household_count):

        member = Member.objects.create(name=name, is_son=is_son, household_count=household_count)
        member.save()


        return MemberCreateMutation(member)

class Mutation(graphene.ObjectType):
    create_member = MemberCreateMutation.Field()





