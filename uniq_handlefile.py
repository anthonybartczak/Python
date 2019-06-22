import sys


class FileReader:
    def __init__(self, filename):
        self.file = open(filename)

    def readline(self):
        line = self.file.readline()
        if line == '':
            raise EOFError
        return line[:-1]

    def close(self):
        self.file.close()


class FileWriter:
    def __init__(self, filename):
        self.file = open(filename, "w")

    def writeline(self, line):
        self.file.write(line + '\n')

    def close(self):
        self.file.close()


class InputReader:
    def readline(self):
        return input()

    def close(self):
        pass


class OutputWriter:
    def writeline(self, line):
        print(line)

    def close(self):
        pass


def main():
    should_read_from_file = len(sys.argv) >= 2
    should_write_to_file = len(sys.argv) == 3
    try:
        if should_read_from_file:
            reader = FileReader(sys.argv[1])
        else:
            reader = InputReader()
        if should_write_to_file:
            writer = FileWriter(sys.argv[2])
        else:
            writer = OutputWriter()
        try:
            last_line = ''
            while True:
                current_line = reader.readline()

                if last_line != current_line:
                    writer.writeline(current_line)
                    last_line = current_line
        except EOFError:
            pass
        finally:
            reader.close()
            writer.close()
    except FileNotFoundError:
        print('Nonexistent file, try again.')


if __name__ == '__main__':
    main()
