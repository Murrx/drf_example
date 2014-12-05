from rest_framework import serializers
import example.models


class ExampleSerializer(serializers.ModelSerializer):

    def __init__(self, *args, **kwargs):
        # Don't pass the 'fields' arg up to the superclass
        # Instantiate the superclass normally
        super(ExampleSerializer, self).__init__(*args, **kwargs)
        print self._context.keys()
#       selected_fields = selected_fields.split(',')
#       if selected_fields is not None:
#           keep_fields = set(selected_fields)
#           all_fields = set(self.fields.keys())
#           print keep_fields
#           print all_fields
#           for field_name in all_fields - keep_fields:
#               del self.fields[field_name]

    def to_representation(self, obj):
        return self.context.keys()

    class Meta:
        model = example.models.Example
        fields = ('foo', 'bar')
