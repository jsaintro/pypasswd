#!/usr/bin/env python


# ENTRY_ATTRIBS is a list of tupples.
# each tupple contains the attribute name and it's description
ENTRY_ATTRIBS = [('name', 'Name'), ('url', 'URL'),
    ('UserName', 'User Name'), ('password', 'Password'),
    ('note', 'Note'), ('test', 'Test')]


class Entry:
    """Account data container"""
    def __init__(self, name):
        for i in range(len(ENTRY_ATTRIBS)):
            setattr(self, ENTRY_ATTRIBS[i][0], '')
        # Populate the name with the real value
        self.name = name

    def __str__(self):
        message = ''
        for i in range(len(ENTRY_ATTRIBS)):
            (attrib, desc, value) = self.fetch_attr(i)
            message += attrib + ": " + value + "\n"
        return message

    def fetch_attr(self, i):
        attrib = ENTRY_ATTRIBS[i][0]
        desc = ENTRY_ATTRIBS[i][1]
        value = getattr(self, attrib)
        return (attrib, desc, value)

    def edit_entry(self):
        print "Editing: " + self.name + "\n"
        for i in range(len(ENTRY_ATTRIBS)):
            (attrib, desc, value) = self.fetch_attr(i)
            print str(i) + " " + desc + ": " + value
        choice = input("Enter number to edit: ")
        setattr(self, ENTRY_ATTRIBS[choice][0],
            raw_input(ENTRY_ATTRIBS[choice][1] + ": "))


class Folder:
    def __init__(self, name):
        self.name = name
        self.nodes = []  # List of nodes.  Can be Entry or Folder

    def __str__(self):
        message = "Branch Name: " + self.name + "\n" \
            "Nodes: "
        for node in self.nodes:
            message += node.name + ","
        return message

    def add_node(self, nodeobj):
        self.nodes.append(nodeobj)
        
    def findex(self):
        for node in self.nodes:
            print node.name


#### Testing stuff
e1 = Entry('e1')
e2 = Entry('e2')
f1 = Folder('f1')
f2 = Folder('f2')
#### Testing stuff
