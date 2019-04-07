from django_elasticsearch_dsl import DocType, Index
from store.catalog.models import Product


products = Index('products')


@products.doc_type
class ProductDocument(DocType):

    class Meta:
        model = Product

        fields = ('title', )