# List of student scores
scores = [72, 45, 90, 61, 38]

# Initialize variables for running counts and totals
pass_count = 0
fail_count = 0
total_score = 0

# Loop through each score in the list
for score in scores:
    total_score += score
    
    # Determine the grade and update pass/fail counters
    if score >= 80:
        grade = 'A'
        pass_count += 1
    elif score >= 70:
        grade = 'B'
        pass_count += 1
    elif score >= 50:
        grade = 'C'
        pass_count += 1
    else:
        grade = 'F'
        fail_count += 1

    # Print individual score and grade
    print(f"Score: {score} - Grade: {grade}")

# Calculate average score
average = total_score / len(scores)

# Print summary statistics
print(f"\nTotal Passed: {pass_count}")
print(f"Total Failed: {fail_count}")
print(f"Average Score: {round(average, 1)}")