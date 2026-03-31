class Solution:
    delimiter = chr(0)
    start= chr(1)
    end = chr(2)
    def encode(self, strs: List[str]) -> str:
        # print(self.delimiter.join(strs))
        if len(strs)==0:
            return ''
        elif strs==[""]:
            return self.start + self.end
        return self.start + self.delimiter.join(strs) + self.end

    def decode(self, s: str) -> List[str]:
        if s=='':
            return []
        s = s[1:-1]
        return s.split(self.delimiter)