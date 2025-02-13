# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):

    # # example of test that checks for logical errors
    # def test_sulfuras_should_not_decrease_quality(self):
    #     items = [Item("Sulfuras", 5, 80)]
    #     gilded_rose = GildedRose(items)
    #     gilded_rose.update_quality()
    #     sulfuras_item = items[0]
    #     self.assertEqual(80, sulfuras_item.quality)
    #     self.assertEqual(4, sulfuras_item.sell_in)
    #     self.assertEqual("Sulfuras", sulfuras_item.name)

    # # example of test that checks for syntax errors
    # def test_gilded_rose_list_all_items(self):
    #     items = [Item("Sulfuras", 5, 80)]
    #     gilded_rose = GildedRose(items)
    #     all_items = gilded_rose.get_item()
    #     self.assertEqual(["Sulfuras"], all_items)

    def test_conjured_items_degrade_twice_as_fast(self):
        items = [Item(name="ConjuredItem", sell_in=2, quality=8)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(items[0].quality, 6)

    def test_quality_never_negative(self):
        items = [Item(name="ABC", sell_in=5, quality=0.5)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertGreaterEqual(items[0].quality, 0)

    def test_quality_never_exceed_50(self):
        items = [Item(name="Aged Brie", sell_in=5, quality=49.5)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertLessEqual(items[0].quality, 50)

    def test_none_items(self):
        gilded_rose = GildedRose([])
        gilded_rose.update_quality() # No Exception should be raised even if there is no item 




if __name__ == '__main__':
    unittest.main()
