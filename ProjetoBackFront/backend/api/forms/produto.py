from api.forms import BaseForm
from api.models.produto import Produto

class ProdutoForm(BaseForm):
    class Meta:
        model = Produto
        fields = '__all__'