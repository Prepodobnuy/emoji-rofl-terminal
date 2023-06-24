class Config():
    def __init__(self, name:str='config'):
        self.name = name

    def GetConfig(self) -> list:
        
        with open(self.name) as config:
            return config.read().split('\n')

    def TimeDelay(self) -> int:
        return int(self.GetConfig()[0].split(' ')[1])

    def EmojiName(self) -> str:
        return self.GetConfig()[1].split(' ')[1]

    def TextName(self) -> str:
        return self.GetConfig()[2].split(' ')[1]
