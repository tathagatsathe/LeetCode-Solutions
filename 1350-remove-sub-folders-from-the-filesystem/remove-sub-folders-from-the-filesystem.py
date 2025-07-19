class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        folder.sort()
        i=1
        fldr = folder[0] 
        while(i<len(folder)):
            if(fldr+'/'==folder[i][:len(fldr)+1]):
                folder.pop(i)
            else:
                fldr = folder[i]
                i+=1


        return folder
        