class rainDrops:
    def __init__(self,n):
        self.n = n

    def pour(self):
        n= self.n
        rain = {3:'i', 5:'a',7:'o'}
        out = [f'Pl{v}ng'*(n%k==0) for k,v in rain.items()]
        return ''.join(out) or str(n)


    # def pour_2(self):
    #     rain = {3:'i', 5:'a',7:'o'}
    #     out = filter(lambda x=d: self%d==0, [f"Pl{r}ng" for d,r in rain])


test = rainDrops(30)
print(test.pour())