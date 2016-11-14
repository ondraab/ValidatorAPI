5
import

6
pygtk.require('2.0')
7
import gtk

8
9


class BasicTreeViewExample:


    10
11  # close the window and quit
12


def delete_event(self, widget, event, data=None):
    13
    gtk.main_quit()


14
return False
15
16


def __init__(self):
    17  # Create a new window


18
self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)
19
20
self.window.set_title("Basic TreeView Example")
21
22
self.window.set_size_request(200, 200)
23
24
self.window.connect("delete_event", self.delete_event)
25
26  # create a TreeStore with one string column to use as the model
27
self.treestore = gtk.TreeStore(str)
28
29  # we'll add some data now - 4 rows with 3 child rows each
30
for parent in range(4):
    31
    piter = self.treestore.append(None, ['parent %i' % parent])
32
for child in range(3):
    33
    self.treestore.append(piter, ['child %i of parent %i' %
                                  34(child, parent)])
35
36  # create the TreeView using treestore
37
self.treeview = gtk.TreeView(self.treestore)
38
39  # create the TreeViewColumn to display the data
40
self.tvcolumn = gtk.TreeViewColumn('Column 0')
41
42  # add tvcolumn to treeview
43
self.treeview.append_column(self.tvcolumn)
44
45  # create a CellRendererText to render the data
46
self.cell = gtk.CellRendererText()
47
48  # add the cell to the tvcolumn and allow it to expand
49
self.tvcolumn.pack_start(self.cell, True)
50
51  # set the cell "text" attribute to column 0 - retrieve text
52  # from that column in treestore
53
self.tvcolumn.add_attribute(self.cell, 'text', 0)
54
55  # make it searchable
56
self.treeview.set_search_column(0)
57
58  # Allow sorting on the column
59
self.tvcolumn.set_sort_column_id(0)
60
61  # Allow drag and drop reordering of rows
62
self.treeview.set_reorderable(True)
63
64
self.window.add(self.treeview)
65
66
self.window.show_all()
67
68


def main():
    69
    gtk.main()


70
71
if __name__ == "__main__":
    72
    tvexample = BasicTreeViewExample()
73
main()