class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        total_laser = 0
        devices_count = []
        for i in range(len(bank)):
            device = 0
            for cell in bank[i]:
                if cell == '1':
                    device += 1
            devices_count.append(device)

        before_row = devices_count[0]
        for i in range(1, len(devices_count)):
            if before_row == 0 and devices_count[i] != 0:
                before_row = devices_count[i]
                continue
            if before_row != 0:
                if devices_count[i] == 0:
                    continue
                else:
                    total_laser += (before_row * devices_count[i])
                    before_row = devices_count[i]

        return total_laser