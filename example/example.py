import sys
import os
import qtboot

toolbar_items = [
    {
        "id": "tb-back",
        "type": "button",
        "event": "back",
        "icon": "go-previous",
        "label": "Go back to the previous page",
        "shortcut": "B",
    },
    {
        "id": "tb-close",
        "type": "button",
        "event": "back",
        "icon": "application-exit",
        "label": "Exit mdpreview",
        "shortcut": "Escape",
    },
    {
        "id": "tb-keepontop",
        "type": "check",
        "event": "back",
        "icon": "go-top",
        "label": "Keep window on top",
        "shortcut": "T",
    },
]


class ExampleGUI(qtboot.QTBoot):
    def __init__(self, *args, **kwargs):
        qtboot.QTBoot.__init__(self, *args, **kwargs)

    def _ev_back(self):
        print("BACK")


if __name__ == "__main__":
    app = ExampleGUI("electricmonk",
                     "qtbootexample",
                     sys.argv,
                     icon=os.path.join(os.path.dirname(sys.argv[0]), 'icon.png'),
                     toolbar_items=toolbar_items)
    app.run()
