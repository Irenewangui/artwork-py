from peewee import (CharField,
                    SqliteDatabase,
                    Model,
                    TextField,
                    OperationalError,
                    IntegrityError)
db = SqliteDatabase("artwork.db")


class Artwork(Model):
    name = CharField(max_length=1000, unique=True)
    description = TextField(default="Good image")
    thumbnail_link = CharField(max_length=1000)
    fullimage_link = CharField(max_length=1000)

    class Meta:
        database = db


def initialize():
    try:
        Artwork.create_table(safe=True)
    except OperationalError:
        pass
    try:
        Artwork.create(
            name="waves_flowing",
            description="Awesome Artistic Monkey",
            thumbnail_link="static/wave-3473335_640.jpg",
            fullimage_link="static/wave-3473335_1920.jpg"
            )
    except IntegrityError:
        pass
    try:
        Artwork.create(
            name="mercedes",
            description="Awesome Mercedes Car",
            thumbnail_link="static/mercedes-3510327_640.jpg",
            fullimage_link="static/mercedes-3510327_1920.jpg"
            )
    except IntegrityError:
        pass
    