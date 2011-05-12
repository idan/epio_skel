from django.core.cache import cache

from django.core.management.base import NoArgsCommand

class Command(NoArgsCommand):
    help = 'Flushes the cache.'

    def handle_noargs(self, **options):
        cache.clear()
        print "Cache flushed."
