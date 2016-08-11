class EncryptedText(object):

    WorkingCopyText = []
    FunctionResult = ''
    ExceptionList = {}

    def __init__(self, UserInput, EncryptionKey):
        self.UserInput = UserInput
        self.EncriptionKey = EncryptionKey

    def Encrypt_Text(self):
        for index, i in enumerate(self.UserInput, start=0):
            CurrentIntChar = ord(i)
            while True:
                try:
                    CurrentEncryptedChar = str(unichr(CurrentIntChar ^ self.EncryptionKey))
                    break
                except UnicodeEncodeError:
                    CurrentEncryptedChar = str(unichr(127))
                    self.ExceptionList.update({index: CurrentIntChar})
                    break
            self.WorkingCopyText.append(CurrentEncryptedChar)
            print "The letter \"", i, "\"with the integer value of", CurrentIntChar, \
                "was encrypted into \"", CurrentEncryptedChar, \
                "\"that has the integer value", ord(CurrentEncryptedChar), \
                "and has the variable type", type(CurrentEncryptedChar)
        self.FunctionResult = ''.join(self.WorkingCopyText)

    def Resolve_Text(self):
        for index, i in enumerate(self.FunctionResult, start=0):
            if index in self.ExceptionList:
                CurrentIntChar = ord(self.ExceptionList[index])
            else:
                CurrentIntChar = ord(i)
            while True:
                try:
                    CurrentRestoredChar = str(unichr(CurrentIntChar ^ self.EncriptionKey))
                    break
                except UnicodeEncodeError:
                    CurrentRestoredChar = "X"
                    break
            self.WorkingCopyText.append(CurrentRestoredChar)
            print "The letter \"", i, "\"with the integer value of", CurrentIntChar, \
                "was de-encrypted to \"", CurrentRestoredChar, \
                "\"that has the integer value", ord(CurrentRestoredChar), \
                "and has the variable type", type(CurrentRestoredChar)
        self.FunctionResult = ''.join(self.WorkingCopyText)

    def Reset_Values(self):
        self.WorkingCopyText = []
        self.FunctionResult = ''
        self.ExceptionList = {}

    def Reset_Exceptions(self):
        self.ExceptionList = {}

    def Reset_WorkingCopy(self):
        self.WorkingCopyText = []

    def Reset_Result:
        self.FunctionResult = ''
