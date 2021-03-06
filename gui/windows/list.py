__author__ = 'perun'


import gui.templates.show as show
import gui.templates.scrolled_list as scl
import core.distribution as dist
import gui.config.list
import gui.templates.menu_bar as menu_bar
import gui.templates.inser_box as insert_box
import core.networks
import core.devices
from tkinter import *


class AccessNetworksList(scl.ScrolledList, show.ShowInfo, menu_bar.ContextMenu):
    def __init__(self, distribution, parent=None):
        self.parent = parent
        self.list_frame = Frame(parent)
        self.list_frame.pack(side=LEFT, fill=BOTH, expand=YES)

        self.info_frame = Frame(parent)
        self.info_frame.pack(side=LEFT, fill=BOTH, expand=YES)

        self.distribution = distribution

        scl.ScrolledList.__init__(self, self.make_fields_list(),
                                  self.list_frame)

    def make_fields_list(self):
        return (network.name for network in self.distribution.networks)

    def run_command_left(self, selection):
        """
        When user click two times on the item in list, method checks what type of network has been chosen and send it to
        ShowInfo class.
        :param selection: selected item from list (double clicked)
        """
        index = self.listbox.curselection()
        if self.distribution.networks[index[0]]:
            print('Network with selected index from list exists.')
            if type(self.distribution.networks[index[0]]) is core.networks.Circuit:
                print('Selected item {} from listbox represents Circuit class.'.format(selection))
                show.ShowInfo.__init__(self, self.distribution.networks[index[0]], self.info_frame)
            elif type(self.distribution.networks[index[0]]) is core.networks.Package:
                print('Selected item {} from listbox represents Package class.'.format(selection))
                show.ShowInfo.__init__(self, self.distribution.networks[index[0]], self.info_frame)
        else:
            print('Network with given index does not exists.')

    def process_data(self, instance):
        """

        :param instance: Network instance
        :return: fetch from config file labels name and values to be displayed in entry.
        """
        index = self.listbox.curselection()
        print('Network with selected index from list exists.')
        if type(self.distribution.networks[index[0]]) is core.networks.Circuit:
            print('Fetching Circuit\'s class entry labels from config file.')
            return gui.config.list.access_network_list_circuit(instance)
        elif type(self.distribution.networks[index[0]]) is core.networks.Package:
            print('Fetching package\'s class entry labels from config file.')
            return gui.config.list.access_network_list_package(instance)

    def run_command_right(self, selection, xy):
        tmp = [z + 120 for z in xy]
        xy = tuple(tmp)
        menu_bar.ContextMenu.__init__(self, coordinates=xy, fields=selection, parent=Frame(self.list_frame))

    def make_menu_widget(self, pull_downs, parent):
        self.menu = self.create_top_menu_widget(parent)

        self.create_command(self.menu, 'Edit network', self.edit_item)
        self.create_command(self.menu, 'Delete', self.delete_item)

    def delete_item(self):
        index = self.listbox.curselection()
        # for network in self.distribution.networks:
         #   if network.name == self.selection:
          #      index = network.index
        self.distribution.delete_network(index[0])
        self.delete_selected_item_from_listbox()

    def edit_item(self):
        """
        Context menu edit option. After operation reloads listbox.

        """
        index = self.listbox.curselection()
        gui.templates.inser_box.EditNetworkCircuit(index[0], self.distribution, Toplevel())
        scl.ScrolledList.__init__(self, self.make_fields_list(),
                                  self.list_frame)


class NodesList(AccessNetworksList):
    def make_fields_list(self):
        return (node.name for node in self.distribution.nodes)

    def run_command_left(self, selection):
        """
        When user click two times on the item in list, method checks what type of node has been chosen and send it to
        ShowInfo class.
        :param selection: selected item from list (double clicked)
        """
        index = self.listbox.curselection()
        if self.distribution.nodes[index[0]]:
            print('Node with selected index from list exists.')
            print('Selected item {} from listbox represents node class.'.format(selection))
            show.ShowInfo.__init__(self, self.distribution.nodes[index[0]], self.info_frame)
        else:
            print('Network with given index does not exists.')

    def process_data(self, instance):
        """

        :param instance: Network instance
        :return: fetch from config file labels name and values to be displayed in entry.
        """
        index = self.listbox.curselection()
        print('Network with selected index from list exists.')
        if type(self.distribution.nodes[index[0]]) is core.devices.EdgeRouter:
            print('Fetching EdgesNode\'s class entry labels from config file.')
            return gui.config.list.nodes_list_edge(instance)
        elif type(self.distribution.nodes[index[0]]) is core.devices.CoreRouter:
            print('Fetching CoreNode\'s class entry labels from config file.')
            return gui.config.list.nodes_list_core(instance)

    def make_menu_widget(self, pull_downs, parent):
        self.menu = self.create_top_menu_widget(parent)

        self.create_command(self.menu, 'Edit node', self.edit_item)
        self.create_command(self.menu, 'Delete', self.delete_item)

    def delete_item(self):
        index = self.listbox.curselection()
        # for network in self.distribution.networks:
         #   if network.name == self.selection:
          #      index = network.index
        self.distribution.delete_node(index[0])
        self.delete_selected_item_from_listbox()

    def edit_item(self):
        """
        Context menu edit option. After operation reloads listbox.

        """
        index = self.listbox.curselection()
        gui.templates.inser_box.EditNode(index[0], self.distribution, Toplevel())
        scl.ScrolledList.__init__(self, self.make_fields_list(),
                                  self.list_frame)


class LinksList(AccessNetworksList):
    def make_fields_list(self):
        return (link.name for link in self.distribution.links)

    def run_command_left(self, selection):
        """
        When user click two times on the item in list, method checks what type of node has been chosen and send it to
        ShowInfo class.
        :param selection: selected item from list (double clicked)
        """
        index = self.listbox.curselection()
        if self.distribution.links[index[0]]:
            print('Link with selected index from list exists.')
            print('Selected item {} from listbox represents node class.'.format(selection))
            show.ShowInfo.__init__(self, self.distribution.links[index[0]], self.info_frame)
        else:
            print('Network with given index does not exists.')

    def process_data(self, instance):
        """

        :param instance: Network instance
        :return: fetch from config file labels name and values to be displayed in entry.
        """
        print('Link with selected index from list exists.')
        print('Fetching Link\'s class entry labels from config file.')
        tmp = gui.config.list.links_list(instance)
        #for path in self.distribution.links[0].paths_voice:
         #   tmp.append([path, self.distribution.links[0].paths_voice[path]])

        return tmp

    def make_menu_widget(self, pull_downs, parent):
        self.menu = self.create_top_menu_widget(parent)

        self.create_command(self.menu, 'Edit link', self.edit_item)

        paths = Menu(self.menu)
        paths.add_command(label='Voice', command=self.show_paths_voice)
        paths.add_command(label='Video', command=self.show_paths_video)
        paths.add_command(label='BE', command=self.show_paths_be)

        self.menu.add_cascade(label='Paths...', menu=paths)
        #self.create_command(self.menu, 'Delete', self.delete_item)

    def delete_item(self):
        index = self.listbox.curselection()
        # for network in self.distribution.networks:
         #   if network.name == self.selection:
          #      index = network.index
        self.distribution.delete_node(index[0])
        self.delete_selected_item_from_listbox()

    def edit_item(self):
        """
        Context menu edit option. After operation reloads listbox.

        """
        index = self.listbox.curselection()
        gui.templates.inser_box.EditLink(index[0], self.distribution, Toplevel())
        scl.ScrolledList.__init__(self, self.make_fields_list(),
                                  self.list_frame)

    def show_paths_voice(self):
        index = self.listbox.curselection()
        show.ShowPathsThroughLink(Toplevel(), self.distribution.links[index[0]].paths_voice)

    def show_paths_video(self):
        index = self.listbox.curselection()
        show.ShowPathsThroughLink(Toplevel(), self.distribution.links[index[0]].paths_video)

    def show_paths_be(self):
        index = self.listbox.curselection()
        show.ShowPathsThroughLink(Toplevel(), self.distribution.links[index[0]].paths_be)

    def not_ready(self):
        print('Option not ready...')


if __name__ == '__main__':
    root = Tk()
    d = dist.Data()
    d.test()
    #AccessNetworksList(d, root)
    LinksList(d, root)
    root.mainloop()