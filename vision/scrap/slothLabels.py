from sloth import items
from sloth.items import PointItem
from PyQt4.Qt import Qt
from PyQt4.QtGui import QPen



class PositivePointItem(PointItem):
    def __init__(self, *args, **kwargs):
        PointItem.__init__(self, *args, **kwargs)

        self.setPen(QPen(Qt.red, 2))

class NegativePointItem(PointItem):
    def __init__(self, *args, **kwargs):
        PointItem.__init__(self, *args, **kwargs)

        self.setPen(QPen(Qt.black, 2))

LABELS = (
    {"attributes": {
        "class":  "positive"},
        "item":     PositivePointItem,
        "inserter": "sloth.items.PointItemInserter",
        "text":     "positive"
    },

    {"attributes": {
        "class":  "negative"},
        "item":     NegativePointItem,
        "inserter": "sloth.items.PointItemInserter",
        "text":     "negative"
    },
)