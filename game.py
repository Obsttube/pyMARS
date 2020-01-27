import core
import warior
import loader
import instruction
import window


class Game():
    def __init__(self, core_size, window_width_and_height):
        self.core_size = core_size
        self.set_up(window_width_and_height)
        self.gui.mainloop(self.loop)

    def set_up(self, window_width_and_height):
        self.__core = core.Core(self.core_size)
        self.gui = window.GUI(window_width_and_height, self.__core)
        self.__core.set_gui_callback(self.gui)
        main_loader = loader.Loader(self.__core)

        # load instructions

        first_warior = warior.Warior(
            "first_warior", "#ff0000")  # todo index
        first_warior.set_gui_callback(self.gui)
        self.__core.add_warior(first_warior)
        start_index = main_loader.load_file_at(
            first_warior, "dwarf.txt", 0, self.core_size)
        first_warior.add_process(start_index)

        second_warior = warior.Warior("second_warior", "#00ff00")
        second_warior.set_gui_callback(self.gui)
        self.__core.add_warior(second_warior)
        start_index = main_loader.load_file_at(
            second_warior, "agony3.1.txt", 100, self.core_size)
        second_warior.add_process(start_index)

    def loop(self):
        if self.__core.wariors_alive() < 2:
            print(f"{self.__core.get_winning_warior().name} won!")
        else:
            self.__core.execute_current_ins()
            # print(self.__core)
            # print()
