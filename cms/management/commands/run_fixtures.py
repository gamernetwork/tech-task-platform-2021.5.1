from django.core.management.base import BaseCommand

from ...fixtures import Fixtures


class Command(BaseCommand):
    categories = 3
    posts = 10
    tags = 20

    help = 'Generate some categories, posts and tags using fixtures.'

    def handle(self, *args, **kwargs):
        fixtures = Fixtures()

        self.stdout.write(f'Creating {self.tags} tags…')
        for i in range(self.tags):
            tag = fixtures.create_tag()
            self.stdout.write('\t' + repr(tag))

        self.stdout.write(f'Creating {self.categories} categories…')
        for i in range(self.categories):
            category = fixtures.create_category()
            self.stdout.write('\t' + repr(category))

            self.stdout.write(f'\tCreating {self.posts} posts…')
            for j in range(self.posts):
                post = fixtures.create_post(category)
                self.stdout.write('\t\t' + repr(post))
