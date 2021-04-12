from django.test import TestCase
import redis

client = redis.StrictRedis(port=6379, db=0)
client.set('nome', 'Augusto')
print(client.get('nome'))
