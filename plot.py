# Standard Library
import io
import itertools
import pathlib

# 3rd Party Packages
from PIL import Image


class Plot:
    """..."""
    id_iter = itertools.count()

    def __init__(self, title_text=None, size=500):
        self.title_text = title_text  
        self.size = size
        self.figure = None
        self.id = next(Plot.id_iter)
        self.path = str(pathlib.Path().resolve()) + "/images/" + str(self.id) + ".png"
    
    def get_image(self):
        if self.title_text is not None:
            self.figure.update_layout(title=self.title_text)
        self.figure.write_image(self.path)
        image = Image.open(self.path)
        image.thumbnail((self.size, self.size))
        bio = io.BytesIO()
        image.save(bio, format="PNG")
        return bio.getvalue()
