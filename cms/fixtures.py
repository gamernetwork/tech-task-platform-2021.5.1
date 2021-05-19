from . import models


class Fixtures:
    def create_category(self):
        """
        Creates a category with a dummy name and slug.

        Args: none
        Returns:
            `models.Category` object.
        """
        pass

    def create_post(self, category):
        """
        Creates a post within a chosen category. Also associates that post with
        a random selection of tags (at least one tag per post).

        All other fields on the post will be filled with dummy data.

        Args:
            * `category` - `models.Category` object.
        Returns:
            * `models.Post` object.
        """
        pass

    def create_tag(self):
        """
        Creates a tag with a dummy name.

        Args: none
        Returns:
            `models.Tag` object.
        """
        pass
