def seatStudent(seats, students):
  seats.sort()
  students.sort()
  totalMove = 0
  for i in range(len(seats)):
    totalMove += abs(students[i]-seats[i])
  return totalMove

inSeats = list(map(int, input().split()))
inStudents = list(map(int, input().split()))
print(seatStudent(inSeats, inStudents))