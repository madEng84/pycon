from graphene import ObjectType
from graphene_form.mutations import FormMutation

from .forms import LoginForm, RegisterForm
from .types import MeUserType


class Login(FormMutation):
    class Meta:
        form_class = LoginForm
        output_types = (MeUserType,)


class Register(FormMutation):
    class Meta:
        form_class = RegisterForm
        output_types = (MeUserType,)


class UsersMutations(ObjectType):
    login = Login.Field()
    register = Register.Field()
