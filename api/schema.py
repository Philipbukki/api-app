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

class MemberUpdateMutation(graphene.Mutation):
    member = graphene.Field(MemberType)
    class Arguments:
        name =graphene.String()
        is_son = graphene.Boolean()
        household_count =graphene.Int()
        id =graphene.ID(required=True)

    def mutate(self, info, name, is_son, household_count, id):

        member = Member.objects.get(pk=id)
        if name is not None:
            member.name = name
        if household_count is not None:
            member.household_count= household_count
        if is_son is not None:
            member.is_son =is_son

        member.save()

        return MemberUpdateMutation(member)

class Mutation(graphene.ObjectType):
    create_member = MemberCreateMutation.Field()
    update_member = MemberUpdateMutation.Field()





