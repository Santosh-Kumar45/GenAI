
# PROBLEM 5
# Two teams have the following skills:
#
# team_a = {"Python", "SQL", "Git", "Docker"}
# team_b = {"Python", "Git", "AWS", "GenAI"}
#
# Find:
# 1. Skills both teams have
# 2. Skills only team A has
# 3. All unique skills across both teams

team_a = {"Python", "SQL", "Git", "Docker"}
team_b = {"Python", "Git", "AWS", "GenAI"}

print("skills both team : ", team_a & team_b)
print("skills only team A : ", team_a - team_b)
print("unique skills in both team : ", team_a | team_b)