class EncryptedText(object):

    WorkingCopyEncText = []
    ReturnedEncryptedText = ''
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
            self.WorkingCopyEncText.append(CurrentEncryptedChar)
            print "The letter \"", i, "\"with the integer value of", CurrentIntChar, \
                "was encrypted into \"", CurrentEncryptedChar, \
                "\"that has the integer value", ord(CurrentEncryptedChar), \
                "and has the variable type", type(CurrentEncryptedChar)
        self.ReturnedEncryptedText = ''.join(self.WorkingCopyEncText)

    def Resolve_Text(self):
