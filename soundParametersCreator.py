class soundParametersCreator:
    start = 0
    def createParameter(self, text, levelOfNarcoticness):
        listOfParamters = []
        currentParameter = []
        i = 0
        while i < len(text):
            currentParameter.append(self.start)
            currentParameter.append(ord(text[i])% 10 + (10 - levelOfNarcoticness)*10)
            currentParameter.append(100)
            currentParameter.append(2) #duration
            listOfParamters.append(currentParameter)
            currentParameter=[]
            self.start+=1
            i+=1
        return listOfParamters


