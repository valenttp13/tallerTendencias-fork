from restframework import serializers
from .models import Document, Tag, DocumentTag

class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = 'all'

