# Problem: Remove Comments - https://leetcode.com/problems/remove-comments/



class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        result = []
        in_block_comment = False
        current_line = []

        for line in source:
            i = 0
            while i < len(line):
                if in_block_comment:
                    if line[i:i+2] == "*/":
                        in_block_comment = False
                        i += 1 
                else:
                    if line[i:i+2] == "//":
                        break  
                    elif line[i:i+2] == "/*":
                        in_block_comment = True
                        i += 1 
                    else:
                        current_line.append(line[i])

                i += 1

            if not in_block_comment and current_line:
                result.append("".join(current_line))
                current_line = []

        return result

        