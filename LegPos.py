class LegPos:
    FRONT_LEFT = 1
    FRONT_RIGHT = 2
    BACK_LEFT = 3
    BACK_RIGHT = 4

    @staticmethod
    def StringForm(legPos):
        if legPos == LegPos.FRONT_LEFT:
            return 'Front-Left'
        if legPos == LegPos.FRONT_RIGHT:
            return 'Front-Right'
        if legPos == LegPos.BACK_LEFT:
            return 'Back-Left'
        if legPos == LegPos.BACK_RIGHT:
            return 'Back-Right'
