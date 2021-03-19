class Solution:
    def groupAnagrams(self, strs):
        result = []
        word_dic = {} 
        for i in range(len(strs)):
            word = sorted(strs[i])
            word = ''.join(word)
            if word in word_dic:
                word_dic[word].append(i)
            else:
                word_dic[word] = [i]
        for word in word_dic.values():
            for i in range(len(word)):
                word[i] = strs[word[i]]
            result.append(word)
        return result
            
        