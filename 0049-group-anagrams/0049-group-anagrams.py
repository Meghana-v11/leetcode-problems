class Solution(object):
    def groupAnagrams(self, strs):
        groups = {}
        for strr in strs:
            key = ''.join(sorted(strr))
            if key in groups:
                groups[key].append(strr)
            else:
                groups[key] = [strr]
        return list(groups.values())
    
        