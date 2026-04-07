class Robot:

    def __init__(self, width: int, height: int):
        self.w = width
        self.h = height
        self.perimeter = 2 * (width + height - 2) # (중복되는 모서리 계산 제외)
        self.pos = 0  # 0부터 perimeter-1 까지의 현재 위치 수치화
        self.moved = False # 한 번이라도 움직였는지 확인

    def step(self, num: int) -> None:
        self.moved = True
        self.pos = (self.pos + num) % self.perimeter

    def getPos(self) -> List[int]:
        p = self.pos
        # 하단 변 (East 방향 구간)
        if 0 <= p <= self.w - 1:
            return [p, 0]
        # 우측 변 (North 방향 구간)
        elif p <= (self.w - 1) + (self.h - 1):
            return [self.w - 1, p - (self.w - 1)]
        # 상단 변 (West 방향 구간)
        elif p <= 2 * (self.w - 1) + (self.h - 1):
            return [self.w - 1 - (p - (self.w - 1) - (self.h - 1)), self.h - 1]
        # 좌측 변 (South 방향 구간)
        else:
            return [0, self.perimeter - p]

    def getDir(self) -> str:
        p = self.pos
        # 한 번도 움직이지 않은 상태는 항상 East
        if not self.moved or p == 0:
            # 하지만 한 바퀴 돌아서 0으로 온 경우 방향은 South여야 함
            return "South" if self.moved else "East"
            
        if 1 <= p <= self.w - 1:
            return "East"
        elif p <= (self.w - 1) + (self.h - 1):
            return "North"
        elif p <= 2 * (self.w - 1) + (self.h - 1):
            return "West"
        else:
            return "South"


# Your Robot object will be instantiated and called as such:
# obj = Robot(width, height)
# obj.step(num)
# param_2 = obj.getPos()
# param_3 = obj.getDir()