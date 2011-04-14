#!/usr/bin/env python

import traceback

# ENTRY_ATTRIBS is a list of tupples.
# each tupple contains the attribute name and it's description
ENTRY_ATTRIBS = [('name', 'Name'), ('url', 'URL'),
    ('UserName', 'User Name'), ('password', 'Password'),
    ('note', 'Note')]

DEFAULTFILE = 'pypasswd.pyp'
class PYPMain:
    """Main Application class"""
    def __init__(self):
        self.file = DEFAULTFILE
        self.pyproot = Folder('Root')
        # Set our initial current position to root
        self.pypcurr = self.pyproot
        #### Test stuff
        self.pyproot.add_node(Folder('f1'))
        self.pyproot.add_node(Folder('f2'))
        self.pyproot.add_node(Entry('e1'))
        #### Test stuff
        
    def whichobj(self, nodeobj):
        if isinstance(nodeobj, Entry):
            return 'e'
        else:
            return 'f'

    def newfolder(self):
        foldername = raw_input("Enter new folder name: ")
        f = Folder(foldername)
        self.pypcurr.add_node(f)

    def newentry(self):
        entryname = raw_input("Enter new entry name: ")
        e = Entry(entryname)
        print "Editing: " + e.name + "\n"
        for i in range(len(ENTRY_ATTRIBS)):
            (attrib, desc, value) = e.fetch_attr(i)
            value = raw_input("Enter " + desc + ": ")
            setattr(e, ENTRY_ATTRIBS[i][0], value)
        self.pypcurr.add_node(e)

    def selectfolder(self):
        fnum = raw_input('Select active folder number: ').split('.')
        node = self.pyproot
        for num in fnum:
            node = node.nodes[int(num) - 1]
        self.pypcurr = node

    def index(self, nodes, level = 0):
        i = 1
        for node in nodes:
            # Build the initial line
            line = str(i) + ' ' + self.whichobj(node) + ' ' + node.name
            # Add level spacing
            line += ' ' * level
            # Add selected brackets
            if node == self.pypcurr:
                line = '[' + line + ']'

            #print "%s%d %s%s %s" % (lspc, i, pointer, self.whichobj(node), node.name)
            print line
            # Redursively display nodes
            if self.whichobj(node) == 'f':
                if len(node.nodes):
                    self.index(node.nodes, level + 1)
            i += 1

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
            raw_input(EfNTRY_ATTRIBS[choice][1] + ": "))


class Folder:
    def __init__(self, name):
        self.name = name
        self.nodes = []  # List of nodes.  Can be Entry or Folder
        self.isopen = False

    def __str__(self):
        message = "Branch Name: " + self.name + "\n" \
            "Nodes: "
        for node in self.nodes:
            message += node.name + ","
        return message

    def add_node(self, nodeobj):
        self.nodes.append(nodeobj)
        
def main():

    appmain = PYPMain()

    while True:
        # Display the folder index
        appmain.index(appmain.pyproot.nodes)
        # print the command key
        print "f: new folder e: new entry sf: select folder q:quit"
        # read line for command
        c = raw_input("Enter Command: ")
        # execute the command
        if c == 'q':
            break
        elif c == 'f':
            appmain.newfolder()
        elif c == 'e':
            appmain.newentry()
        elif c == 'sf':
            appmain.selectfolder()

if __name__ =='__main__':
    # execute main or fail nicely
    try:
        main()
    except:
        # print error message
        traceback.print_exc()

