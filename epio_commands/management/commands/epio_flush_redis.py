import redis
from bundle_config import config

from django.core.management.base import NoArgsCommand

class Command(NoArgsCommand):
    help = 'Flushes all keys in redis.'

    def handle_noargs(self, **options):
        r = redis.Redis(host=config['redis']['host'], port=int(config['redis']['port']), password=config['redis']['password'])
        r.flushall()
        print "All redis keys flushed."
