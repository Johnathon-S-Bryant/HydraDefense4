class FullyAgnosticBPWeights:
    def __init__(self, headWeight:float, bodyWeight:float, legWeight:float, tailWeight:float):
        assert headWeight + bodyWeight + legWeight + tailWeight == 1
        self.HeadWeight:float = headWeight
        self.BodyWeight:float = bodyWeight
        self.LegWeight:float = legWeight
        self.TailWeight:float = tailWeight
