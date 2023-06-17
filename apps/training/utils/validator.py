import re

class ValidatorField():

    def isNumber(self,data):
        
        result=False
        if type(data)  in (int, float):
            result=True
        
        return result

    def isFormatEmail(data):
        
        result=False
        
        patron = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        if re.match(patron, data):
            result= True
        
        return result

    def isValidGender(data):
        result=False
        if (data in('M','F')):
            result=True
        
        return result

    def isPositiveNumber(data):
        
        result=False
        if ((type(data)  in (int, float)) and data>0):
            result=True
        
        return result
    
    def RangeScores(data):
        result=False

        if  (type(data)  in (int,float)) and (0<data and data<=5) :
            result=True
        
        return result

