''' A wrapper class module the pygubu builder for easy gui building '''
import tkinter as tk


class Builder:
    ''' A wrapper class around the pygubu builder for easy gui building '''

    def __init__(self, builder):
        self.builder = builder

    def widget_exists(self, name):
        ''' Checks if a widget exists '''
        return name in self.builder.objects

    def set_entry(self, name, value):
        ''' Sets value of entry component '''
        if self.widget_exists(name):
            self.builder.get_object(name).delete(0, tk.END)
            self.builder.get_object(name).insert(0, str(value))

    def write_line(self, name, value):
        ''' Writes a line to a textbox '''
        self.builder.get_object(name).insert(tk.END, '>> ' + str(value) + '\n')
        self.builder.get_object(name).see('end')

    def insert_row(self, name, value):
        ''' Sets value of a single row of treeview component '''
        self.builder.get_object(name).insert('', 'end', values=value)

    def set_cell(self, name, row, column, value):
        ''' Sets the value of a specific cell of the tree view '''
        item_id = self.builder.get_object(name).get_children()[row]
        self.builder.get_object(name).set(item_id, '#{}'.format(column), value)

    def set_treeview(self, name, values):
        ''' Sets value of whole treeview component '''
        self.clear_treeview(name)
        for value in values:
            self.insert_row(name, value)

    def clear_treeview(self, name):
        ''' Clears the values of treeview component '''
        tree = self.builder.get_object(name)
        tree.delete(*tree.get_children())

    def init_checkboxes(self, options):
        ''' Checks all the checkboxes at the start '''
        for option, value in options.items():
            self.init_checkbox(option, value)

    def init_checkbox(self, name, value):
        ''' Initializes a checkbox component using boolean value '''
        self.builder.get_object(name).state(['!alternate'])
        if value:
            self.builder.get_object(name).state(['selected'])
        else:
            self.builder.get_object(name).state(['!selected'])

    def set_button_list_state(self, buttons, state):
        ''' Sets the state of a list of button components '''
        for button in buttons:
            self.builder.get_object(button)['state'] = state

    def set_row(self, name, value):
        ''' Sets a row value of a treeview component '''
        self.builder.get_object(name).insert(
            '', 'end', values=value)
