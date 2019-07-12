"""Personal Information Manager

Scaffold for a simple PIM
"""

import minioncmd

# test_data
import datetime
today = datetime.date.today()
tomorrow = today + datetime.timedelta(days=1)
nextweek = today + datetime.timedelta(days=6)
lastmonth = today - datetime.timedelta(days=33)
# there are only a few days a year this isn't really "last month"


class ContactManager:
    """Underlying library implementing a bunch of useful ideas"""
    def __init__(self):
        self.contacts = {
            "0": {"Name": "Douglas", "Birthday": nextweek},
            "1": {"Name": "Isaac", "Birthday": lastmonth}
            }

    def list_contacts(self):
        return self.contacts


class EventManager:
    """Underlying library managing stuff"""
    def __init__(self):
        self.events = {
            "0": {"text": "Send birthday card to Isaac",
                  "date": lastmonth,
                  "done": False},
            "1": {"text": "Plan birthday party for Douglas",
                  "date": today,
                  "done": False},
        }

    def list_events(self):
        return self.events


class PIMApp(minioncmd.BossCmd):
    prompt = "pim>"
    doc_leader = "PIM Help"
    doc_header = "Top Level commands"
    minion_header = "Subprograms"

    def __init__(self, completekey='tab', stdin=None, stdout=None):
        super().__init__(completekey, stdin, stdout)
        self.contacts = ContactManager()
        self.events = EventManager()


class ContactCmd(minioncmd.MinionCmd):
    prompt = "contacts>"
    doc_leader = "Contact Manager Help"

    def do_list(self, text):
        """Lists contacts"""
        for cid in self.master.contacts.list_contacts():
            contact = self.master.contacts.contacts[cid]
            print(contact)


class EventCmd(minioncmd.MinionCmd):
    prompt = "events>"
    doc_leader = "Event Manager Help"

    def do_list(self, text):
        """Lists events"""
        for eid in self.master.events.list_events():
            event = self.master.events.events[eid]
            print(event)


if __name__ == '__main__':
    app = PIMApp()
    contacts = ContactCmd('contacts', app)
    events = EventCmd('events', app)

    app.cmdloop()
