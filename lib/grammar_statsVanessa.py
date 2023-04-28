# # user_string => "Hello! There! Friend!"
# # percentage good => 100%
# # check with more than one text input

# # if 3 of 4 texts entered are valid => 75%
# import string
# import re

# class GrammarStats():
    
#     def __init__(self):
#         pass

#     def check(self, text):
#         self.text = text
#         capital = text[0]
#         last_letter = text[-1]
#         punctuation = string.punctuation
#         hasPunc = False
#         for char in punctuation:
#             if last_letter == char:
#                 hasPunc = True
#         if (capital.isupper() and hasPunc):
#             return True
#         else:
#             return False
        
#     def percentage_good(self):
#         regex = re.compile('[!.?]')
#         list = []
#         i = 0
#         percentage = 0.0
#         self.sentence = self.text.split(" ")
#         print(self.sentence)
#         #capital = sentence[0]
#         #last_letter = sentence[-1]
#         #punctuation = string.punctuation
#         print(regex)
#         for word in self.sentence:
#             print(word)
#             print(word[0] + " here")
#             print(word[-1])
#             i += 1
#             if word[0].isupper() and word[-1] == regex:
#             #if (capital.isupper() and last_letter == punctuation):
#                 print(word[0] + "aqui")
#                 print(word[-1])
#                 i += 1
#                 print(i)
#                 #list.append(word)
#                 print(len(list) + "outro")                       
#         percentage =  int(i / len(self.sentence)) * 100 
#         print(percentage)
            

#         return  percentage

# grammar = GrammarStats()
# grammar.check("Hello There! Friend!")
# grammar.percentage_good()

# # vanessafcosta