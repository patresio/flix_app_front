from actors.repository import ActorRepository


class ActorService:
    def __init__(self):
        self.actor_repository = ActorRepository()

    def get_actors(self):
        return self.actor_repository.get_actors()

    # def create_genre(self, name):
    #     genre = dict(name=name)
    #     return self.actor_repository.create_genre(genre)
