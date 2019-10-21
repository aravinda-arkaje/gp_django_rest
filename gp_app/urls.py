from django.urls import include, path
from .views import RecipeListView,RecipeView,RecipeCreateView, RecipeRetrieveUpdatdDestroy

app_name = 'gp_app'

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    # path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('list/',RecipeListView.as_view()),
    path('list-user/',RecipeView.as_view()),
    path('create-recipe/',RecipeCreateView.as_view()),
    path('receipe/<int:pk>/',RecipeRetrieveUpdatdDestroy.as_view())
]
