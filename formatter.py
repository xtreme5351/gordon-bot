import os.path


class Formatter:
    def counterChange(self):
        self.createFile(self.counter)
        f = open("counter.txt", 'w')
        f.write(str(self.counter))
        f.close()

    def incrementCounter(self):
        self.counter += 1

    def getInputFilePath(self, index_num):
        title = "inputText_{}.txt".format(str(index_num))
        completed_path = os.path.join(self.input_path, title)
        return completed_path

    def createFile(self, index):
        print("COUNTER CALLED: ", self.counter)
        f = open(self.getInputFilePath(index), 'x')
        f.close()
        print("EVENT: New file created")

    def packData(self, message):
        with open(self.getInputFilePath(int(open("counter.txt", 'r').readline())), 'a') as inputText:
            inputText.write(message + "\n")
        inputText.close()

    def unpackData(self):
        formatted_input = ""
        raw_input = open(self.getInputFilePath(int(open("counter.txt", 'r').readline())), 'r')
        for string in raw_input.readlines():
            formatted_input += string
        raw_input.close()
        return formatted_input

    def __init__(self, channel):
        print("REQUEST: Formatting text")
        self.channel = channel
        self.input_path = '/Users/pc/Code/Python/gordon_bot/inputs'
        self.counter = int(open("counter.txt", 'r').readline())
