from collections import Counter
import statistics
import psycopg2
import random



html_code = """
<html>
<head>
<title>Our Python Class exam</title>

<style type="text/css">
	
	body{
		width:1000px;
		margin: auto;
	}
	table,tr,td{
		border:solid;
		padding: 5px;
	}
	table{
		border-collapse: collapse;
		width:100%;
	}
	h3{
		font-size: 25px;
		color:green;
		text-align: center;
		margin-top: 100px;
	}
	p{
		font-size: 18px;
		font-weight: bold;
	}
</style>

</head>
<body>
<h3>TABLE SHOWING COLOURS OF DRESS BY WORKERS AT BINCOM ICT FOR THE WEEK</h3>
<table>
	
	<thead>
		<th>DAY</th><th>COLOURS</th>
	</thead>
	<tbody>
	<tr>
		<td>MONDAY</td>
		<td>GREEN, YELLOW, GREEN, BROWN, BLUE, PINK, BLUE, YELLOW, ORANGE, CREAM, ORANGE, RED, WHITE, BLUE, WHITE, BLUE, BLUE, BLUE, GREEN</td>
	</tr>
	<tr>
		<td>TUESDAY</td>
		<td>ARSH, BROWN, GREEN, BROWN, BLUE, BLUE, BLEW, PINK, PINK, ORANGE, ORANGE, RED, WHITE, BLUE, WHITE, WHITE, BLUE, BLUE, BLUE</td>
	</tr>
	<tr>
		<td>WEDNESDAY</td>
		<td>GREEN, YELLOW, GREEN, BROWN, BLUE, PINK, RED, YELLOW, ORANGE, RED, ORANGE, RED, BLUE, BLUE, WHITE, BLUE, BLUE, WHITE, WHITE</td>
	</tr>
	<tr>
		<td>THURSDAY</td>
		<td>BLUE, BLUE, GREEN, WHITE, BLUE, BROWN, PINK, YELLOW, ORANGE, CREAM, ORANGE, RED, WHITE, BLUE, WHITE, BLUE, BLUE, BLUE, GREEN</td>
	</tr>
	<tr>
		<td>FRIDAY</td>
		<td>GREEN, WHITE, GREEN, BROWN, BLUE, BLUE, BLACK, WHITE, ORANGE, RED, RED, RED, WHITE, BLUE, WHITE, BLUE, BLUE, BLUE, WHITE</td>
	</tr>

	</tbody>
</table>

<p>Examine the sequence below very well, you will discover that for every 1s that appear 3 times, the output will be one, otherwise the output will be 0.</p>
<p>0101101011101011011101101000111 <span style="color:orange;">Input</span></p>
<p>0000000000100000000100000000001 <span style="color:orange;">Output</span></p>
<p>
</body>
</html>
"""

# Extract the color values from the HTML code
start_index = html_code.find("<td>MONDAY</td>") + len("<td>MONDAY</td>")
end_index = html_code.find("</table>")
table_data = html_code[start_index:end_index]
color_values = table_data.split(", ")
color_count = Counter(color_values)

# Question 1: Calculate the mean color
total_colors = len(color_values)
mean_color = max(color_count, key=lambda x: color_count[x] / total_colors)
print("Mean color of shirts:", mean_color)

# Question 2:  Which color is mostly worn throughout the week?
# Find the color with the highest count
most_worn_color = max(color_count, key=color_count.get)
print("Color mostly worn throughout the week:", most_worn_color)

# Question 3:  Which color is the median?
# Sort the colors based on their counts
sorted_colors = sorted(color_count, key=color_count.get)
# Find the color in the middle (median)
median_color = sorted_colors[len(sorted_colors) // 2]
print("Median color:", median_color)

# Question 4: Find the variance
# Calculate the variance of the color counts
color_counts = list(color_count.values())
variance = statistics.variance(color_counts)
print("Variance of color counts:", variance)

# Question 5:  if a colour is chosen at random, what is the probability that the color is red?
# Calculate the total number of colors
total_colors = sum(color_count.values())
# Calculate the probability of choosing the color "red"
red_probability = color_count.get("RED", 0) / total_colors
print("Probability of choosing the color red:", red_probability)

# Question 6:Save the colours and their frequencies in postgresql database
values)
# Connect to the PostgreSQL database
conn = psycopg2.connect(
    host="your_host",
    database="your_database",
    user="your_user",
    password="your_password"
)

# Create a cursor object to execute SQL queries
cursor = conn.cursor()

# Iterate over the colors and their frequencies, and insert them into the database
for color, frequency in color_count.items():
    query = "INSERT INTO colors (color, frequency) VALUES (%s, %s)"
    cursor.execute(query, (color, frequency))

# Commit the changes and close the connection
conn.commit()
cursor.close()
conn.close()

# Question 7: write a recursive searching algorithm to search for a number entered by user in a list of numbers.
def recursive_search(number, lst, start_index=0):
    if start_index >= len(lst):
        return False

    if lst[start_index] == number:
        return True

    return recursive_search(number, lst, start_index + 1)

# Example usage
numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90]
search_number = int(input("Enter a number to search: "))

found = recursive_search(search_number, numbers)

if found:
    print("Number found in the list.")
else:
    print("Number not found in the list.")

# Question 8: Write a program that generates random 4 digits number of 0s and 1s and convert the generated number to base 10.
import random

def generate_random_binary():
    binary_digits = [str(random.randint(0, 1)) for _ in range(4)]
    binary_number = "".join(binary_digits)
    return binary_number

def binary_to_decimal(binary):
    decimal = int(binary, 2)
    return decimal

# Generate a random binary number
random_binary = generate_random_binary()
print("Random Binary Number:", random_binary)

# Convert the binary number to decimal
decimal = binary_to_decimal(random_binary)
print("Decimal Equivalent:", decimal)

# Question 9:    Write a program to sum the first 50 fibonacci sequence.
def fibonacci_sum(n):
    fib_sequence = [0, 1]  # Starting Fibonacci sequence
    for i in range(2, n):
        fib_sequence.append(fib_sequence[i-1] + fib_sequence[i-2])  # Calculate the next Fibonacci number

    sum_fibonacci = sum(fib_sequence[:n])  # Sum the first n Fibonacci numbers
    return sum_fibonacci

# Calculate the sum of the first 50 Fibonacci numbers
sum_first_50 = fibonacci_sum(50)
print("Sum of the first 50 Fibonacci numbers:", sum_first_50)
