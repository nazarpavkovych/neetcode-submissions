class Solution:

    def encode(self, strs: List[str]) -> str:
        zoznam = list(strs)
        number = 0
        while zoznam:
            zoznam.pop()
            number+=1
        if number==0:
            return 'min'
        
        return 'max'.join(strs)

    def decode(self, s: str) -> List[str]:
        if s == 'min':
            return []
        return s.split('max')


