import redis
from django.conf import settings
from rest_framework import serializers
from .models import Devices, Endpoints


class AnagramSerializer(serializers.Serializer):
    first_word = serializers.CharField(max_length=50)
    second_word = serializers.CharField(max_length=50)
    count = serializers.ReadOnlyField()
    is_anagram = serializers.ReadOnlyField()

    class Meta:
        fields = '__all__'

    def validate(self, data):
        redis_instance = redis.StrictRedis(host=settings.REDIS_HOST, port=settings.REDIS_PORT, db=9, password='redis')

        if sorted(data['first_word']) == sorted(data['second_word']):
            if not redis_instance.exists('count'):
                redis_instance.set('count', 1)
                data['count'] = 1
            else:
                data['count'] = redis_instance.incr('count')
            data['is_anagram'] = 'true'
        else:
            data['is_anagram'] = 'false'

        if redis_instance.keys('word*'):
            new_word_id = redis_instance.incr('word_count')
        else:
            redis_instance.set('word_count', 1)
            new_word_id = 1
        redis_data = {
            'first_word': data['first_word'],
            'second_word': data['second_word'],
            'is_anagram': data['is_anagram']
        }
        redis_instance.hmset(f'word{new_word_id}', redis_data)
        return data


class DevicesSerializer(serializers.ModelSerializer):
    dev_id = serializers.ReadOnlyField()

    class Meta:
        model = Devices
        fields = '__all__'


class EndpointsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Endpoints
        fields = '__all__'
