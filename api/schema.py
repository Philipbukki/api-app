from graphene_django.types import DjangoObjectType
import graphene
from .models import Member, Variable


class MemberType(DjangoObjectType):
    class Meta:
        model = Member


class VariableType(DjangoObjectType):
    class Meta:
        model = Variable


class Query(graphene.ObjectType):
    all_variables = graphene.List(VariableType)
    all_members = graphene.List(MemberType)

    def resolve_all_variables(self, info, **kwargs):
        return Variable.objects.all()

    def resolve_all_members(self, info, **kwargs):
        return Member.objects.all()


class MemberCreateMutation(graphene.Mutation):
    member = graphene.Field(MemberType)

    class Arguments:
        name = graphene.String(required=True)
        is_son = graphene.Boolean(required=True)
        household_count = graphene.Int(required=True)

    def mutate(self, info, name, is_son, household_count):
        h_count = 0
        if is_son:
            h_count = household_count
        member = Member.objects.create(
            name=name, is_son=is_son, household_count=h_count)
        member.save()

        return MemberCreateMutation(member=member)


class VariableCreateMutation(graphene.Mutation):
    variable = graphene.Field(VariableType)

    class Arguments:
        name = graphene.String(required=True)
        value = graphene.Int(required=True)

    def mutate(self, info, name, value):
        variable = Variable.objects.create(name=name, value=value)
        variable.save()

        return VariableCreateMutation(variable=variable)


class MemberUpdateMutation(graphene.Mutation):
    member = graphene.Field(MemberType)

    class Arguments:
        name = graphene.String()
        is_son = graphene.Boolean()
        household_count = graphene.Int()
        id = graphene.ID(required=True)

    def mutate(self, info, name, is_son, household_count, id):

        member = Member.objects.get(pk=id)
        if name is not None:
            member.name = name
        if household_count is not None:
            member.household_count = household_count
        if is_son is not None:
            member.is_son = is_son

        member.save()

        return MemberUpdateMutation(member=member)


class VariableUpdateMutation(graphene.Mutation):
    variable = graphene.Field(VariableType)

    class Arguments:
        name = graphene.String()
        value = graphene.Int()
        id = graphene.ID(required=True)

    def mutate(self, info, name, value, id):

        variable = Variable.objects.get(pk=id)
        if name is not None:
            variable.name = name
        if value is not None:
            variable.value = value

        variable.save()

        return VariableUpdateMutation(variable=variable)


class MemberDeleteMutation(graphene.Mutation):
    member = graphene.Field(MemberType)

    class Arguments:
        id = graphene.ID(required=True)

    def mutate(self, info, id):
        member = Member.objects.get(pk=id)
        member.delete()

        return MemberDeleteMutation(member=None)


class VariableDeleteMutation(graphene.Mutation):
    variable = graphene.Field(VariableType)

    class Arguments:
        id = graphene.ID(required=True)

    def mutate(self, info, id):
        variable = Variable.objects.get(pk=id)
        variable.delete()

        return VariableDeleteMutation(variable=None)


class Mutation(graphene.ObjectType):
    create_member = MemberCreateMutation.Field()
    update_member = MemberUpdateMutation.Field()
    delete_member = MemberDeleteMutation.Field()
    create_variable = VariableCreateMutation.Field()
    update_variable = VariableUpdateMutation.Field()
    delete_variable = VariableDeleteMutation.Field()
