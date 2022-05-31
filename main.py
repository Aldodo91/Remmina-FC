from ulauncher.api.client.Extension import Extension
from ulauncher.api.client.EventListener import EventListener
from ulauncher.api.shared.event import KeywordQueryEvent
from ulauncher.api.shared.item.ExtensionResultItem import ExtensionResultItem
from ulauncher.api.shared.action.RenderResultListAction import RenderResultListAction
from ulauncher.api.shared.action.RunScriptAction import RunScriptAction


class GnomeSessionExtension(Extension):
    def __init__(self):
        super(GnomeSessionExtension, self).__init__()
        self.subscribe(KeywordQueryEvent, KeywordQueryEventListener())


class KeywordQueryEventListener(EventListener):
    def on_event(self, event, extension):
        items = []
        my_list = event.query.split(" ")
        items.append(pi())
        items.append(piMini())

        return RenderResultListAction(items)

    path = "/home/aldo/.local/share/remmina/"


def pi():
    return ExtensionResultItem(icon='images/ras.png',
                               name='Connetti airDot',
                               description='vnc connect rasberry',
                               on_enter=RunScriptAction("remmina -c /home/aldo/.local/share/remmina/group_vnc_rasberry_nano-server-ddns-net.remmina", None))


def piMini():
    return ExtensionResultItem(icon='images/rasNano.png',
                               name='Disconnetti airDot',
                               description='vnc connect rasberry nano',
                               on_enter=RunScriptAction("remmina -c /home/aldo/.local/share/remmina/group_vnc_nano_192-168-1-69.remmina", None))


if __name__ == '__main__':
    GnomeSessionExtension().run()
