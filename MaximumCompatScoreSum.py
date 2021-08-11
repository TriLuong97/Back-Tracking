#Problem 1947. Maximum Compatibility Score Sum

'''
There is a survey that consists of n questions where each question's answer is either 0 (no) or 1 (yes).

The survey was given to m students numbered from 0 to m - 1 and m mentors numbered from 0 to m - 1. The answers of the students are represented by a 2D integer array students where students[i] is an integer array that contains the answers of the ith student (0-indexed). The answers of the mentors are represented by a 2D integer array mentors where mentors[j] is an integer array that contains the answers of the jth mentor (0-indexed).

Each student will be assigned to one mentor, and each mentor will have one student assigned to them. The compatibility score of a student-mentor pair is the number of answers that are the same for both the student and the mentor.

For example, if the student's answers were [1, 0, 1] and the mentor's answers were [0, 0, 1], then their compatibility score is 2 because only the second and the third answers are the same.
You are tasked with finding the optimal student-mentor pairings to maximize the sum of the compatibility scores.

Given students and mentors, return the maximum compatibility score sum that can be achieved.

 

Example 1:

Input: students = [[1,1,0],[1,0,1],[0,0,1]], mentors = [[1,0,0],[0,0,1],[1,1,0]]
Output: 8
Explanation: We assign students to mentors in the following way:
- student 0 to mentor 2 with a compatibility score of 3.
- student 1 to mentor 0 with a compatibility score of 2.
- student 2 to mentor 1 with a compatibility score of 3.
The compatibility score sum is 3 + 2 + 3 = 8.
Example 2:

Input: students = [[0,0],[0,0],[0,0]], mentors = [[1,1],[1,1],[1,1]]
Output: 0
Explanation: The compatibility score of any student-mentor pair is 0.
 

Constraints:

m == students.length == mentors.length
n == students[i].length == mentors[j].length
1 <= m, n <= 8
students[i][k] is either 0 or 1.
mentors[j][k] is either 0 or 1.

 	      0    1      2
students = [[0,0],[0,0],[0,0]]
            0      1     2
mentors = [[1,1],[1,1],[1,1]]

Return: the biggest compatibility sum between the students and tutors. 

Observation: 
- To retrieve the maximum sum of the score, we must choose the biggest sum of score of each pairing
_ Any students can be paired with any tutors, as long as the pairing return the highest compatibility sum 


Solution: 
check the combatibilty of each student with each metors
 
student -0: mentor 0, 1, 2 => max(compatibleScore)
student -1: mentor 0 ,1, 2 => max(compatibleScore)
student -2: mentor 0 ,1, 2 => max(compatibleScore)

at student  0 with mentor 0
n questions in both arrays

backtracking: 

student 0 -> [mentor 


Time complexity: O(m^2) 
Space complexity: O(1)


'''
class Solutions:
	def maxCompatibilitySum(self, students, mentors):
		'''
		:type students: List[List[int]]
			:type mentors: List[List[int]]
			:rtype: int
		'''
		self.maxScore = 0
		self.backtracking(set(), students, mentors, 0, 0)
		return self.maxScore


	#Helper method to find the sum of the highest possible score using backtracking
	def backtracking(self, visited, students, mentors, current_score, anchor_pos):
		#check to see if the current score is greater than the max score or not
		if anchor_pos == len(mentors):
			if(current_score > self.maxScore):
				self.maxScore = current_score
			return
		#check the score of each pairing
		for i in range(len(mentors)):
			#check to see if this pairing has been scored or not
			if i in visited:
				continue

			visited.add(i)
			current_score += self.score(students[anchor_pos], mentors[i])
			#run backtracking with the current student on the next set of mentors
			self.backtracking(visited, students, mentors, current_score, anchor_pos+1)
			#reset the visited set because the next mentor will need to be matched with other students
			current_score -= self.score(students[anchor_pos], mentors[i])
			visited.remove(i)

	#Helper method to check for the compatibility score
	def score(self, student, mentor):
		result = 0
		for i in range(len(student)):
			#if there is a match in the answers, then we increment the score by 1
			if(student[i] == mentor[i]):
				result += 1
		return result

#Main function to run the test cases: 
def main():
	print("TESTING Maximum Compatibility Score Sum...")
	#Test cases: 
	students = [[1,1,0],[1,0,1],[0,0,1]]
	mentors = [[1,0,0],[0,0,1],[1,1,0]]
	solutions = Solutions()
	print(solutions.maxCompatibilitySum(students, mentors))
	print("END OF TESTING...")


main()

