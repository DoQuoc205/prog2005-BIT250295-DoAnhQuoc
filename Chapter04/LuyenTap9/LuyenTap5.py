class User:
    def __init__(self, user_id):
        self._id = user_id

    @property
    def id(self):
        return self._id

u = User(123)
print("User ID:", u.id)