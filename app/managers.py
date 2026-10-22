import sqlite3

from app.models import Actor


class ActorManager:
    def __init__(self) -> None:
        self._connection = sqlite3.connect("cinema.db")
        self.db_name = "cinema.db"
        self.table_name = "actors"

    def create(self, first_name: str, last_name: str) -> None:
        self._connection.execute(
            f"INSERT INTO {self.table_name} "
            "(first_name, last_name) VALUES (?, ?)",
            (first_name, last_name),
        )
        self._connection.commit()

    def all(self) -> List[Actor]:
        actors = self._connection.execute(
            f"SELECT * FROM {self.table_name}"
        )
        if actors:
            return [Actor(*actor) for actor in actors]
        return []

    def update(self, pk: int, new_first_name: str, new_last_name: str) -> None:
        self._connection.execute(
            f"UPDATE {self.table_name} "
            "SET pk = ?, first_name = ?, last_name = ? WHERE pk = ?",
            (pk, new_first_name, new_last_name),
        )
        self._connection.commit()
