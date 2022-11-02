from test_movies.models import Reaction


def get_reactions_from_movie(id):
    reactions = Reaction.objects.get(movieId=id)
    return reactions


