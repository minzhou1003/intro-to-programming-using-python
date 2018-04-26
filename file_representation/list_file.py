# minzhou@bu.edu


class List_file:

    def __init__(self, filename, cursor=(0, 0)):
        with open(filename, 'r') as myfile:
            self.text = myfile.readlines()
        self.cursor = cursor
        self.len = len(''.join(self.text))

    # Print the text with cursor
    def print_file(self):
        left = self.cursor[0]
        for line in self.text[:left]:
            print(line, end='')

        print(self.text[left][:self.cursor[1]] + '^' + self.text[left][self.cursor[1]:], end='')

        for line in self.text[left + 1:]:
            print(line, end='')

    # Move cursor one character to the left
    def cmd_h(self):
        if self.cursor[1] > 0:
            tmp = self.cursor[1] - 1
            self.cursor = (self.cursor[0], tmp)
        else:
            self.cursor = (self.cursor[0], 0)

    # Move cursor one character to the right
    def cmd_I(self):
        if self.cursor[1] < self.len - 1:
            tmp = self.cursor[1] + 1
            self.cursor = (self.cursor[0], tmp)

    # Delete the character to the left of the cursor
    def cmd_X(self):
        if self.cursor[1] > 0:
            left = self.cursor[0]
            leftlist = self.text[:left]
            current = self.text[left][self.cursor[1]:]
            rightlist = self.text[left + 1:]
            self.text = leftlist + [current] + rightlist

    # Remove on current line from cursor to the end
    def cmd_D(self):

        left = self.cursor[0]
        leftlist = self.text[:left]
        current = self.text[left][:self.cursor[1]] + '\n'

        rightlist = self.text[left + 1:]
        self.text = leftlist + [current] + rightlist

    # Delete current line and move cursor to the beginning of next line
    def cmd_dd(self):
        left = self.cursor[0]
        leftlist = self.text[:left]
        rightlist = self.text[left + 1:]
        self.text = leftlist + rightlist
        if self.cursor[0] > 0:
            self.cursor = (self.cursor[0] - 1, 0)
        else:
            self.cursor = (0, 0)

    # Transpose two adjacent lines
    def cmd_ddp(self):
        cur_line = self.cursor[0]
        # if on the last line
        if cur_line == len(self.text) - 1:
            print('This is the last line!')
            return
        else:
            self.text[cur_line], self.text[cur_line + 1] = self.text[cur_line + 1], self.text[cur_line]

    # search for next occurrence of a string
    def cmd_n(self, patten):
        for ind, line in enumerate(self.text):
            if line.find(patten) != -1:
                self.cursor = (ind, line.find(patten))

    # move cursor vertically up one line
    def cmd_j(self):

        # if on the first line
        if self.cursor[0] == 0:
            print('This is the first line!')
            return
        else:
            self.cursor = (self.cursor[0] - 1, self.cursor[1])

    # move cursor vertically down one line
    def cmd_k(self):

        # if on the last line
        if self.cursor[0] == len(self.text) - 1:
            print('This is the last line!')
            return
        else:
            self.cursor = (self.cursor[0] + 1, self.cursor[1])

    # write your representation as text file and save it
    def cmd_wq(self):

        file = open('saved_file.txt', 'w')
        for line in self.text:
            file.write(line)
        print('File is successfully saved as saved_file.txt!')


def main():
    file1 = List_file('textfile.txt')

    print('Print initial file:\n')
    file1.print_file()
    print()
    print('\ncmd_I for 14 times:')
    file1.cmd_I()
    file1.cmd_I()
    file1.cmd_I()
    file1.cmd_I()
    file1.cmd_I()
    file1.cmd_I()
    file1.cmd_I()
    file1.cmd_I()
    file1.cmd_I()
    file1.cmd_I()
    file1.cmd_I()
    file1.cmd_I()
    file1.cmd_I()
    file1.cmd_I()
    file1.print_file()

    print()
    print('\ncom_h for 3 times:')
    file1.cmd_h()
    file1.cmd_h()
    file1.cmd_h()
    file1.print_file()

    print()
    print('\ncom_X:')
    file1.cmd_X()
    file1.print_file()
    print()
    print('\ncom_k:')
    file1.cmd_k()
    file1.print_file()

    print()
    print('\ncom_j:')
    file1.cmd_j()
    file1.print_file()

    print()
    print('\ncom_D:')
    file1.cmd_D()
    file1.print_file()

    print()
    print('\ncom_ddp:')
    file1.cmd_ddp()
    file1.print_file()

    print()
    print('\ncom_dd:')
    file1.cmd_dd()
    file1.print_file()

    print()
    print("\ncmd_n('complex')")
    file1.cmd_n('complex')
    file1.print_file()

    print()
    print('\ncmd_wq:')
    file1.cmd_wq()

if __name__ == '__main__':
    main()