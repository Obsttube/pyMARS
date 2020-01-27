import main
import tkinter
import math
import random

UPDATE_RATE = round(1000 / 100)  # /30 = ~30 fps


class GUI(tkinter.Frame):

    def __init__(self, window_width_height, core):
        self.core = core
        self.window = tkinter.Tk()
        self.window.title("pyMARS - a Core Wars symulator")
        self.window.geometry(f'{window_width_height}x{window_width_height}')
        tkinter.Frame.__init__(self, self.window)
        self.update()
        self.blocks = dict()
        self.create_widgets(window_width_height, core.size)

    def mainloop(self, callback):
        self.callback = callback
        self.updater()
        self.window.mainloop()

    def draw_canvas(self, canvas_size, core_size):
        self.canvas.create_rectangle(
            0, 0, self.canvas.winfo_width(), self.canvas.winfo_height(), fill="#000000", outline="")
        blocks_sqrt = math.ceil(math.sqrt(core_size))
        block_size = math.floor(canvas_size/blocks_sqrt)
        offset = (canvas_size-blocks_sqrt*block_size)/2
        block_id = 0
        for y in range(blocks_sqrt):
            for x in range(blocks_sqrt):
                if block_id >= core_size:
                    break
                self.blocks[block_id] = self.draw_block(
                    offset+x*block_size, offset+y*block_size, block_size, block_size, self.canvas, True)
                block_id += 1

    def create_widgets(self, canvas_size, core_size):
        self.canvas = tkinter.Canvas(self.window, width=0, height=0)
        self.canvas.pack(anchor="nw")
        self.canvas.config(width=canvas_size, height=canvas_size,
                           borderwidth=0, highlightthickness=0)
        self.window.update()
        self.draw_canvas(canvas_size, core_size)

    def draw_rect(self, x, y, width, height, canvas, color):
        return self.canvas.create_rectangle(x, y, x+width, y+height, fill=color, outline="")

    def update_block_color(self, block_index, color):
        self.canvas.itemconfig(self.blocks[block_index][1], fill=color)

    def update_outline(self, block_index, active):
        if active:
            self.canvas.itemconfig(self.blocks[block_index][0], fill="#fff")
        else:
            self.canvas.itemconfig(self.blocks[block_index][0], fill="#000")

    def draw_block(self, x, y, width, height, canvas, active=False):
        block = []
        block.append(self.draw_rect(x, y, width, height, canvas, "#000"))
        block.append(self.draw_rect(
            x+1, y+1, width-2, height-2, canvas, "#666"))
        return block

    def updater(self):
        # for _ in range(5):
        self.callback()
        self.window.after(UPDATE_RATE, self.updater)
