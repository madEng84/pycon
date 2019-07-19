import dataclasses
from typing import Union

import strawberry
from graphql import GraphQLError

from .utils import convert_form_fields_to_fields, create_error_type, create_input_type


class FormMutation:
    @classmethod
    def __init_subclass__(cls):
        name = cls.__name__

        form_class = cls.Meta.form_class
        form = form_class()

        form_fields = form.fields
        graphql_fields = convert_form_fields_to_fields(form_fields)

        input_type = create_input_type(name, graphql_fields)
        error_type = create_error_type(name, graphql_fields)

        output_types = (
            cls.Meta.output_types if hasattr(cls.Meta, "output_types") else ()
        )

        output = Union[
            error_type, None
        ]  # We add `None` here because we need at least 2 types to create an Union
        output.__args__ = (error_type, *output_types)

        def mutate(root, info, input: input_type) -> output:
            # Once we implement the permission in strawberry we can remove this :)
            if hasattr(cls.Meta, "permission_classes") and cls.Meta.permission_classes:
                for permission in cls.Meta.permission_classes:
                    if not permission().has_permission(info):
                        raise GraphQLError(permission.message)

            form_kwargs = cls.get_form_kwargs(root, info, dataclasses.asdict(input))
            form = form_class(**form_kwargs)
            error = cls.validate_form(form)

            if error:
                return error

            result = form.save()

            if hasattr(cls, "transform"):
                result = cls.transform(result)

            return result

        mutate.__name__ = f"{name}Output"
        mutate.name = name
        mutate = strawberry.mutation(mutate, description=cls.__doc__)

        cls.Mutation = mutate
        cls.Meta.error_type = error_type

    @classmethod
    def validate_form(cls, form):
        if form.is_valid():
            return

        error_cls = cls.get_error_type()
        error_instance = error_cls()

        for name, messages in form.errors.items():
            if name == "__all__":
                name = "nonFieldErrors"

            setattr(error_instance, name, messages)

        return error_instance

    @classmethod
    def get_error_type(cls):
        return cls.Meta.error_type

    @classmethod
    def get_form_kwargs(cls, root, info, input):
        kwargs = {"data": input}

        if hasattr(info, "context"):
            kwargs["context"] = info.context

        return kwargs
