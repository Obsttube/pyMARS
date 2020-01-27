import instruction


class Loader:
    def __init__(self, core):
        self.__core = core

    def load_file_at(self, warior, file_path, index, core_size):
        warior_code = []
        try:
            with open(file_path, "r") as f:
                first_line = True
                block_number = 0
                start_offset = 0
                start_label = None
                for line in f:
                    line = line.split(";")[0].strip().upper()
                    if len(line) == 0:
                        continue
                    if first_line == True:
                        first_line = False
                        if line.startswith("ORG"):
                            start_label = line.split()[1]
                            continue
                    if start_label is not None and line.startswith(start_label):
                        start_offset = block_number
                        line = line.replace(start_label, "").strip()
                    block_number += 1
                    warior_code.append(
                        instruction.Instruction.from_line(line, warior, core_size))
                    if warior.gui != None:
                        warior.gui.update_block_color(
                            block_number-1+index, warior.color)
                # print(start_offset)
                # for w in warior_code:
                # print(w)
                # return warior_code
                self.load_instructions(warior_code, start_offset+index)
                return start_offset+index
        except FileNotFoundError:
            print("File not found")
        except OSError as err:
            print(f"OS error: {err}")
        return None

    def load_instructions(self, warior_code, start_offset):
        warior = warior_code[0].last_warior
        if warior.gui != None:
            warior.gui.update_outline(start_offset, True)
        for i in range(len(warior_code)):
            self.__core.set_at(i+start_offset, warior_code[i])
