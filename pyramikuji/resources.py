import random
class Mikuji:
    texts = ['大凶', '凶', '末吉', '小吉', '中吉', '吉', '大吉']
    threshold = [0.05, 0.175, 0.35, 0.65, 0.825, 0.95, 1.0]

    def __init__(self):
        self.value = random.random()

    @property
    def text(self):
        for i, v in enumerate(self.threshold):
            if self.value <= v:
                return self.texts[i]
        return self.texts[-1]
        

    def __json__(self, request):
        return {'text': self.text}

def mikuji_factory(request):
    return Mikuji()
