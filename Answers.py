from collections import Counter

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

# Question 1: Calculate the mean color
color_count = Counter(color_values)
total_colors = len(color_values)
mean_color = max(color_count, key=lambda x: color_count[x] / total_colors)
print("Mean color of shirts:", mean_color)

# Question 2:  Which color is mostly worn throughout the week?
color_count = Counter(color_values)
# Find the color with the highest count
most_worn_color = max(color_count, key=color_count.get)
print("Color mostly worn throughout the week:", most_worn_color)

# Question 3:  Which color is the median?
color_count = Counter(color_values)
# Sort the colors based on their counts
sorted_colors = sorted(color_count, key=color_count.get)
# Find the color in the middle (median)
median_color = sorted_colors[len(sorted_colors) // 2]
print("Median color:", median_color)

# Question 4: Find the variance
color_count = Counter(color_values)
# Calculate the variance of the color counts
color_counts = list(color_count.values())
variance = statistics.variance(color_counts)
print("Variance of color counts:", variance)

# Question 5: 
