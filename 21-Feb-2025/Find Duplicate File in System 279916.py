# Problem: Find Duplicate File in System - https://leetcode.com/problems/find-duplicate-file-in-system/

class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        content_map = defaultdict(list)

        for path in paths:
            parts = path.split(' ')
            directory = parts[0]
            files = parts[1:]

            for file in files:
                file_name, content = file.split('(')
                content = content[:-1]  
                full_path = directory + '/' + file_name
                content_map[content].append(full_path)

       
        result = [files for files in content_map.values() if len(files) > 1]
        return result
