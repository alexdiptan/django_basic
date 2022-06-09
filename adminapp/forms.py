from authapp.forms import ShopUserEditForm
from authapp.models import ShopUser


class UserAdminEditForm(ShopUserEditForm):
    class Meta:
        model = ShopUser
        fields = '__all__'
