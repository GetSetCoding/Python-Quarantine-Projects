import enchant
from enchant.checker import SpellChecker 
from enchant.tokenize import EmailFilter,URLFilter
dictionary = enchant.request_dict("en_US")
spell=SpellChecker("en-US",filters=[EmailFilter,URLFilter])     
filepath=str(input('Enter file location'))
fileopen=open(filepath)
content=fileopen.read()
spell.set_text(content)
for err in spell:
        print("Misspelled word is: "+err.word+' at position '+ str(err.wordpos)+" "
        +"suggestions"+str(dictionary.suggest(err.word)))  
          
