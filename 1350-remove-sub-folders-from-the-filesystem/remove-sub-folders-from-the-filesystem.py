class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        folder.sort()
        result = []

        result.append(folder[0])
        current_parent = folder[0]

        for i in range(1, len(folder)):
            current_folder = folder[i]

            if not current_folder.startswith(current_parent + '/'):
                result.append(current_folder)
                current_parent = current_folder
            
        return result