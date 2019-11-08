"""Test gilded rose."""
import unittest

from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):
    """Test class."""

    def test_item_decreases(self):
        """Test condition."""
        items = [Item("Vest of Agility", 4, 4)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual([3, 3], [items[0].sell_in, items[0].quality])

    def test_item_double_decreases_after_sell_in(self):
        """Test condition."""
        items = [Item("Vest of Agility", 0, 4)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual([-1, 2], [items[0].sell_in, items[0].quality])

    def test_quality_never_negative(self):
        """Test condition."""
        items = [Item("Vest of Agility", 4, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual([3, 0], [items[0].sell_in, items[0].quality])

    def test_aged_brie_goes_up(self):
        """Test condition."""
        items = [Item("Aged Brie", 11, 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual([10, 11], [items[0].sell_in, items[0].quality])

    def test_passes_brie_goes_up(self):
        """Test condition."""
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 11, 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual([10, 11], [items[0].sell_in, items[0].quality])

    def test_passes_sub_10_days(self):
        """Test condition."""
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 9, 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual([8, 12], [items[0].sell_in, items[0].quality])

    def test_passes_sub_5_days(self):
        """Test condition."""
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 4, 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual([3, 13], [items[0].sell_in, items[0].quality])

    def test_passes_expired(self):
        """Test condition."""
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 0, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual([-1, 0], [items[0].sell_in, items[0].quality])

    def test_items_not_more_than_50(self):
        """Test condition."""
        items = [Item("Vest of Agility", 4, 60)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual([3, 50], [items[0].sell_in, items[0].quality])

    def test_sulfuras(self):
        """Test condition."""
        items = [Item("Sulfuras, Hand of Ragnaros", 4, 80)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual([4, 80], [items[0].sell_in, items[0].quality])


if __name__ == "__main__":
    unittest.main(exit=False)
