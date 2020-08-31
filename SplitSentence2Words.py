#Given a dictionary of words, split the input string into valid words. Return the list of valid words, or null if there are unknown words

#dict = {“a”, “app”, “apple”, “lemon”, “day”, “monday”}

#input = “applemonday”

#output = [“app”, “lemon”, “day”]

#also possible: [“apple”, “monday”]

class CodingTask:
    def SplitSentence2Words(self, preprocc, dictionary, sentence, out):
        if len(sentence) == 0:
            print(out)
            return
        
        for index in range(1, len(sentence) + 1):
            prefix = sentence[0:index]
            
            # small optimization to skip redundant words before processing
            if not prefix[0] in preprocc:
                return

            if prefix in dictionary:
                result = ' '.join(filter(None, [out, prefix]))
                self.SplitSentence2Words(preprocc, dictionary, sentence[index:], result)

task = CodingTask()
dictionary = ['a', 'app', 'apple', 'lemon', 'day', 'monday']
preproccessing = []
for el in dictionary:
    preproccessing.append(el[0])
task.SplitSentence2Words(preproccessing, dictionary, 'applemonday', '')