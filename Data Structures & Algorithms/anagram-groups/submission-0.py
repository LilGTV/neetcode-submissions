class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        exists = {}
        for s in strs:
            ordered = ''.join(sorted(s))
            if ordered in exists.keys():
                    exists[ordered].append(s)
            else:
                exists[ordered] = [s]
        
        response = []
        for j in exists.keys():
            response.append(exists[j])
        return response

