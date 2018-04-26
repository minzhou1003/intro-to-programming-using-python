# minzhou@bu.edu


class String_file:

    def __init__(self, filename, cursor=0):
        with open(filename, 'r') as myfile:
            self.text = ''.join(myfile.readlines())
        self.cursor = cursor
        self.len = len(self.text)

    # Print the text with cursor
    def print_file(self):
        print(self.text[:self.cursor] + '^' + self.text[self.cursor:])

    # Move cursor one character to the left
    def cmd_h(self):
        if self.cursor > 0:
            self.cursor -= 1
        else:
            self.cursor = 0

    # Move cursor one character to the right
    def cmd_I(self):
        if self.cursor < self.len - 1:
            self.cursor += 1

    # Delete the character to the left of the cursor
    def cmd_X(self):
        delta_right = self.text[self.cursor:].find('\n')
        left = self.text[:self.cursor]
        reverse_left = left[::-1]
        delta_left = reverse_left.find('\n')
        if delta_left != -1:
            left_lines = self.text[:self.cursor - delta_left]
            right_lines = self.text[self.cursor + delta_right + 1:]
            current_line = self.text[delta_left + delta_right:self.cursor + delta_right + 1]
            self.text = left_lines + '\n' + current_line + right_lines
        # on the first line
        if delta_left == -1:
            right_lines = self.text[self.cursor + delta_right + 1:]
            current_line = self.text[self.cursor:self.cursor + delta_right + 1]
            self.text = current_line + right_lines


    # Remove on current line from cursor to the end
    def cmd_D(self):
        right = self.text[self.cursor:]
        delta = right.find('\n')
        self.text = self.text[:self.cursor] + self.text[self.cursor + delta:]

    # Delete current line and move cursor to the beginning of next line
    def cmd_dd(self):
        delta_right = self.text[self.cursor:].find('\n')
        left = self.text[:self.cursor]
        reverse_left = left[::-1]
        delta_left = reverse_left.find('\n')

        # cursor on the last line
        if delta_right == -1:
            self.text = self.text[:self.cursor - delta_left]
            self.cursor = len(self.text) - 1

        # cursor on the first line
        elif delta_left == -1:
            self.text = self.text[self.cursor + delta_right + 1:]
            self.cursor = 0
        else:
            self.text = self.text[:self.cursor - 1 - delta_left] + self.text[self.cursor + delta_right:]
            self.cursor = delta_left + delta_right

    # Transpose two adjacent lines
    def cmd_ddp(self):
        delta_right = self.text[self.cursor:].find('\n')
        left = self.text[:self.cursor]
        reverse_left = left[::-1]
        delta_left = reverse_left.find('\n')

        # cursor on the last line
        if delta_right == -1:
            print('No next line to transpose!')
            return
        # cursor on the first line
        elif delta_left == -1:
            left_lines = ''
            current_line = self.text[:self.cursor + delta_right + 1]
            right_lines = self.text[self.cursor + delta_right + 1:]
            next_n = right_lines.find('\n')
            if next_n == -1:
                next_line = right_lines[:]
                rest_lines = ''
            else:
                next_line = right_lines[:next_n]
                rest_lines = right_lines[next_n + 1:]
            self.cmd_dd()
            self.text = left_lines + next_line + '\n' + current_line + rest_lines
        # cursor on the mid line
        else:
            left_lines = self.text[:self.cursor - delta_left]
            current_line = self.text[delta_left + delta_right:self.cursor + delta_right + 1]
            right_lines = self.text[self.cursor + delta_right + 1:]
            next_n = right_lines.find('\n')
            if next_n == -1:
                next_line = right_lines[:]
                rest_lines = ''
            else:
                next_line = right_lines[:next_n]
                rest_lines = self.text[next_n + 1:]
            self.cmd_dd()
            self.text = left_lines + next_line + '\n' + current_line + rest_lines

    # search for next occurrence of a string
    def cmd_n(self, patten):

        inx = self.text.find(patten)
        self.cursor = inx

    # move cursor vertically up one line
    def cmd_j(self):

        left = self.text[:self.cursor]
        reverse_left = left[::-1]
        delta_left = reverse_left.find('\n')

        # cursor on the first line
        if delta_left == -1:
            print('This is the first line!')
            return
        else:
            left_lines = self.text[:self.cursor - delta_left]
            above_len = left_lines[::-1][1:].find('\n')
            self.cursor -= above_len + 1

    # move cursor vertically down one line
    def cmd_k(self):

        delta_right = self.text[self.cursor:].find('\n')
        left = self.text[:self.cursor]
        reverse_left = left[::-1]
        delta_left = reverse_left.find('\n')

        # cursor on the last line
        if delta_right == -1:
            print('This is the last line!')
            return
        else:
            self.cursor += delta_left + delta_right + 1

    # write your representation as text file and save it
    def cmd_wq(self):

        file = open('saved_file.txt', 'w')
        file.write(self.text)
        print('File is successfully saved as saved_file.txt!')


def main():
    # Test
    file1 = String_file('textfile.txt')

    print('Print initial file:\n')
    file1.print_file()
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

    print('\ncom_h for 3 times:')
    file1.cmd_h()
    file1.cmd_h()
    file1.cmd_h()
    file1.print_file()

    print('\ncom_X:')
    file1.cmd_X()
    file1.print_file()


    print('\ncom_D:')
    file1.cmd_D()
    file1.print_file()

    print('\ncom_ddp:')
    file1.cmd_ddp()
    file1.print_file()


    print("\ncmd_n('complex')")
    file1.cmd_n('complex')
    file1.print_file()

    print('\ncom_k:')
    file1.cmd_k()
    file1.print_file()

    print('\ncom_j:')
    file1.cmd_j()
    file1.print_file()

    print('\ncom_dd:')
    file1.cmd_dd()
    file1.print_file()

    print('\ncmd_wq:')
    file1.cmd_wq()


if __name__ == '__main__':
    main()