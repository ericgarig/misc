"""Gilded Rose Exercise."""


class GildedRose(object):
    """Shop class."""

    def __init__(self, items):
        """Init."""
        self.items = items

    def update_quality(self):
        """Update quality."""
        for item in self.items:
            if item.name == "Sulfuras, Hand of Ragnaros":
                item.quality = 80
                continue
            if is_appreciate_item(item):
                item.quality = item.quality + 1
                if item.sell_in < 11:
                    item.quality = item.quality + 1
                if item.sell_in < 6:
                    item.quality = item.quality + 1
                if item.sell_in == 0:
                    item.quality = 0
            elif item.quality > 0:
                item.quality = item.quality - 1
            item.sell_in = item.sell_in - 1
            if item.sell_in < 0:
                if not is_appreciate_item(item) and item.quality > 0:
                    item.quality = item.quality - 1
            if item.quality > 50:
                item.quality = 50


def is_appreciate_item(item):
    """Determine if this an item that appreciates."""
    appreciate_items = [
        "Aged Brie",
        "Backstage passes to a TAFKAL80ETC concert",
    ]
    return item.name in appreciate_items


class Item:
    """Item class."""

    def __init__(self, name, sell_in, quality):
        """Init."""
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        """Obj representation."""
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
