print("Hello, welcome to ExamToday. \n Please answer the questions below.")
score = 0
print("Question n.1 \n What is the boiling point of water? \n A. 10 degrees celcius. \n B. 100 degrees celcius. \n C. 85 degrees celcius.")
ans1 = input()
if ans1 == "B" or ans1 == "b":
    print("Correct, good job!")
    score += 1
elif ans1 == "A" or ans1 == "a":
    print("Incorrect. The correct answer is B")
elif ans1 == "C" or ans1 == "c":
    print("Incorrect. The correct answer is B")

print("Question n.2 \n What does PEMDAS stand for? \n A. Parenthesis, Exponents, Multiplication, Division, Addition, Subtraction. \n B. Parenthesis, Equations, Multiplication, Division, Addition, Subtraction. \n C. Parenthesis, Exponents, Division, Multiplication, Addition, Subtraction.")
ans2 = input()
if ans2 == "A" or ans2 == "a":
    print("Correct, good job!")
    score += 1
else:
    print("Incorrect. The correct answer is A")

print(" Question n.3 \n What is the process by which plants make their own food? \n A. Resperation \n B. Photosynthesis \n C. Fermentation")
ans3 = input()
if ans3 == "B" or ans3 == "b":
    print("Correct, good job!")
    score += 1
elif ans3 == "A" or "a":
    print("Incorrect. The correct answer is B")
elif ans3 == "C" or "c":
    print("Incorrect. The correct answer is B")

print("Question n.4 \n What is the value of π (pi) to two decimal places? \n A. 3.12 \n B. 2.22 \n C. 3.14")
ans4 = input()
if ans4 == "C" or ans4 == "c":
    print("Correct, good job!")
    score += 1
elif ans4 == "A" or ans4 == "a":
    print("Incorrect. The correct answer is C")
elif ans4 == "B" or ans4 == "b":
    print("Incorrect. The correct answer is C")

print("Question n.5 \n Who is known as the 'Father of Mathematics'? \n A. Galileo Galilei \n B. Isaac Newton \n C. Archimedes")
ans5 = input()
if ans5 == "C" or ans5 == "c":
    print("Correct, good job!")
    score += 1
elif ans5 == "A" or ans5 == "a":
    print("Incorrect. The correct answer is C")
elif ans5 == "B" or ans5 == "b":
    print("Incorrect. The correct answer is C")

print("Question n.6 \n What is the smallest unit of matter? \n A. Atom \n B. Cell \n C. Molecule")
ans6 = input()
if ans6 == "A" or ans6 == "a":
  print("Correct, good job!")
  score += 1
elif ans6 == "B" or ans6 == "b":
  print("Incorrect. The correct answer is A")

print("Question n.7 \n What is the name of the longest river in the world? \n A. Nile \n B. Amazon \n C. Mississippi")
ans7 = input()
if ans7 == "A" or ans7 == "a":
  print("Correct, good job!")
  score += 1
elif ans7 == "B" or ans7 == "b":
  print("Incorrect. The correct answer is A")
elif ans7 == "C" or ans7 == "c":
  print("Incorrect. The correct answer is A")

print("Question n.8 \n What is the freezing point of water in Fahrenheit? \n A. 0 degrees Fahrenheit \n B. 32 degrees Fahrenheit \n C. 100 degrees Fahrenheit")
ans8 = input()
if ans8 == "B" or ans8 == "b":
  print("Correct, good job!")
  score += 1
elif ans8 == "A" or ans8 == "a":
  print("Incorrect. The correct answer is B")
elif ans8 == "C" or ans8 == "c":
  print("Incorrect. The correct answer is B")

print("Question n.9 \n Which gas do humans breathe in for survival? \n A. Oxygen \n B. Carbon Dioxide \n C. Nitrogen")
ans9 = input()
if ans9 == "A" or ans9 == "a":
  print("Correct, good job!")
  score += 1
elif ans9 == "B" or ans9 == "b":
  print("Incorrect. The correct answer is A")
elif ans9 == "C" or ans9 == "c":
  print("Incorrect. The correct answer is A")

print("Question n.10 \n What is the chemical formula for salt? \n A. H2SO4 \n B. NaCl \n C. CO2")
ans10 = input()
if ans10 == "B" or ans10 == "b":
  print("Correct, good job!")
elif ans10 == "A" or ans10 == "a":
  print("Incorrect. The correct answer is A")
elif ans10 == "C" or ans10 == "c":
  print("Incorrect. The correct answer is A")

print(f"You have completed the exam. Your score is {score}/10.")