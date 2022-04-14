from django.test import TestCase
from django.urls import reverse

from ..models import Item


class ItemTest(TestCase):
    def test_items_exists_at_desired_location(self):
        response = self.client.get('/goods/items')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'goods/items_list.html')

    def test_goods_items_page(self):
        url = reverse('items')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

"""    def test_item_detail_page(self):
        ids_list = Item.objects.values_list('id', flat=True)
        for id in ids_list:
            response=self.client.get(f'/goods/items{id}')
            self.assertEqual(response.status_code, 200)


    def test_itempage_has_items(self):
        ids_list=Item.objects.values_list('id', flat=True)
        print(ids_list)
        url=reverse('items')
        response=self.client.get(url)
        id_count = 1/len(ids_list)
        self.assertContains(response, '</a>', id_count)
"""