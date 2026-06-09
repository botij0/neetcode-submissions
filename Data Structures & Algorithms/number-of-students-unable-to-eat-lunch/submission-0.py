from collections import deque

class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        studentQueue = deque(students)

        r = 0
        counter = len(studentQueue)
        indexSandwich = 0
        nSandwiches = len(sandwiches)

        while counter > 0 and indexSandwich < nSandwiches:
            currentStudent = studentQueue.popleft()

            if currentStudent == sandwiches[indexSandwich]:
                indexSandwich += 1
                counter = len(studentQueue)
            else:
                studentQueue.append(currentStudent)
                counter -=1
        
        return len(studentQueue)