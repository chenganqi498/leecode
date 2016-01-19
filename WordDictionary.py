#Design a data structure that supports the following two operations:

#void addWord(word)
#bool search(word)

#search(word) can search a literal word or a regular expression string containing only letters a-z or .. A . means it can represent any one letter.

#For example:

#addWord("bad")
#addWord("dad")
#addWord("mad")
#search("pad") -> false
#search("bad") -> true
#search(".ad") -> true
#search("b..") -> true

class WordDictionary:
    # initialize your data structure here.
    def __init__(self):
        self.lt = dict()

    # @param {string} word
    # @return {void}
    # Adds a word into the data structure.
    def addWord(self, word):
        l = len(word)
        if l not in self.lt:
            self.lt[l] = set([word])
        else: self.lt[l].add(word)

    # @param {string} word
    # @return {boolean}
    # Returns if the word is in the data structure. A word could
    # contain the dot character '.' to represent any one letter.
    def search(self, word):
        l = len(word)
        if l not in self.lt: return False
        for tomatch in self.lt[l]:
            matched = self.match(tomatch, word)
            if matched == True: return True
        return False
        
    def match(self, tomatch, word):
        for i in range(len(word)):
            if word[i] != tomatch[i] and word[i] != '.': return False
        return True            

# Your WordDictionary object will be instantiated and called as such:
# wordDictionary = WordDictionary()
# wordDictionary.addWord("word")
# wordDictionary.search("pattern")