# -*- coding: utf-8 -*-


class Item:
    """ DO NOT CHANGE THIS CLASS!!!"""
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)

class ItemUpdater:
    def __init__(self, item: Item):
        self.item = item

    def update(self):
        """Default update behavior for normal items"""
        self.update_quality()
        self.update_sell_in()
        if self.item.sell_in < 0:
            self.handle_expired()

    def update_quality(self):
        """Default quality degradation"""
        self.decrease_quality()

    def update_sell_in(self):
        """Decrease sell_in by 1"""
        self.item.sell_in -= 1

    def handle_expired(self):
        """Handles quality changes when sell_in < 0"""
        self.decrease_quality()

    def increase_quality(self, amount=1):
        """Increase quality but cap at 50"""
        if self.item.quality < 50:
            self.item.quality = min(50, self.item.quality + amount)

    def decrease_quality(self, amount=1):
        """Decrease quality but not below 0"""
        if self.item.quality > 0:
            self.item.quality = max(0, self.item.quality - amount)

class AgedBrieUpdater(ItemUpdater):
    def update_quality(self):
        """Aged Brie increases in quality"""
        self.increase_quality()

    def handle_expired(self):
        """After expiration, Aged Brie increases twice as fast"""
        self.increase_quality()     


class SulfurasUpdater(ItemUpdater):
    def update(self):
        """Sulfuras never changes in quality or sell_in"""
        pass

class BackstagePassUpdater(ItemUpdater):
    def update_quality(self):
        """Backstage passes increase in quality as sell_in decreases"""
        if self.item.sell_in > 10:
            self.increase_quality()
        elif self.item.sell_in > 5:
            self.increase_quality(2)
        elif self.item.sell_in > 0:
            self.increase_quality(3)
        else:
            self.item.quality = 0

class ConjuredItemUpdater(ItemUpdater):
    def update_quality(self):
        """Conjured items degrade twice as fast"""
        self.decrease_quality(2)

    def handle_expired(self):
        """After expiration, Conjured items degrade twice as fast again"""
        self.decrease_quality(2)

class GildedRose:
    def __init__(self, items: list[Item]):
        self.items = items

    def update_quality(self):
        item_updaters = {
            "Aged Brie": AgedBrieUpdater,
            "Sulfuras, Hand of Ragnaros": SulfurasUpdater,
            "Backstage passes to a TAFKAL80ETC concert": BackstagePassUpdater,
        }

        for item in self.items:
            updater_class = item_updaters.get(item.name, ConjuredItemUpdater if "Conjured" in item.name else ItemUpdater)
            updater_class(item).update()
