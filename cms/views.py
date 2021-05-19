from django.forms import model_to_dict
from django.http import JsonResponse
from django.views.generic.list import BaseListView

from . import models


class JSONResponseMixin(BaseListView):
    """
    A mixin that can be used to render a JSON response.

    Django REST Framework, eat your heart out.
    """
    def get_data(self, context):
        queryset = context.get('object_list', [])
        context_object_name = self.get_context_object_name(queryset)
        return {
            context_object_name: [
                self.get_model_data(obj)
                for obj in queryset
            ],
        }

    def get_model_data(self, obj):
        return model_to_dict(obj)

    def render_to_response(self, context, **response_kwargs):
        return JsonResponse(
            self.get_data(context),
            **response_kwargs,
        )


class GetPosts(JSONResponseMixin):
    model = models.Post

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.order_by('title')
        return queryset
