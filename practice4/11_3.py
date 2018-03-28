# minzhou@bu.edu

def main():
    # Students' answers to the questions
    answers = [
                ['A', 'B', 'A', 'C', 'C', 'D', 'E', 'E', 'A', 'D'],
                ['D', 'B', 'A', 'B', 'C', 'A', 'E', 'E', 'A', 'D'],
                ['E', 'D', 'D', 'A', 'C', 'B', 'E', 'E', 'A', 'D'],
                ['C', 'B', 'A', 'E', 'D', 'C', 'E', 'E', 'A', 'D'],
                ['A', 'B', 'D', 'C', 'C', 'D', 'E', 'E', 'A', 'D'],
                ['B', 'B', 'E', 'C', 'C', 'D', 'E', 'E', 'A', 'D'],
                ['B', 'B', 'A', 'C', 'C', 'D', 'E', 'E', 'A', 'D'],
                ['E', 'B', 'E', 'C', 'C', 'D', 'E', 'E', 'A', 'D']]
    # Key to the questions
    keys = ['D', 'B', 'D', 'C', 'C', 'D', 'A', 'E', 'A', 'D']
    pairs = []
    # Grade all answers
    for i in range(len(answers)):
        # Grade one student
        correctCount = 0
        for j in range(len(answers[i])):
            if answers[i][j] == keys[j]:
                correctCount += 1
        pairs.append((i, correctCount))
    
    pairs.sort(key = lambda x: x[1])
    for i in range(len(pairs)):
        print("Student", pairs[i][0], "'s correct count is", pairs[i][1])

main()
