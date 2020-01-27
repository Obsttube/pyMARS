class Warior():

    def __init__(self, name, color):
        self.name = name
        self.color = color
        # contains indexes of curent processes
        self.processes = []
        self.curr_proc_index = 0
        self.gui = None

    def add_process(self, index):
        self.processes.append(index)

    def set_gui_callback(self, gui):
        self.gui = gui

    def next_process(self):
        self.curr_proc_index += 1
        if self.curr_proc_index >= len(self.processes):
            self.curr_proc_index = 0

    def remove_curr_process(self):
        del self.processes[self.curr_proc_index]
        self.curr_proc_index -= 1
        if self.curr_proc_index < 0:
            self.curr_proc_index = len(self.processes)-1

    def next_instruction(self, core_size):
        if self.gui != None:
            self.gui.update_outline(
                self.processes[self.curr_proc_index], False)
        if self.curr_proc_index >= len(self.processes):
            return
        self.processes[self.curr_proc_index] += 1
        if self.processes[self.curr_proc_index] >= core_size:
            self.processes[self.curr_proc_index] = 0
        if self.gui != None:
            self.gui.update_outline(self.processes[self.curr_proc_index], True)

    def set_next_instruction(self, index):
        self.processes[self.curr_proc_index] = index

    def get_instruction_index(self):
        if self.curr_proc_index >= len(self.processes):
            return None
        return self.processes[self.curr_proc_index]
