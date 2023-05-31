from bs4 import BeautifulSoup

html_code = '''
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
'''

soup = BeautifulSoup(html_code, 'html.parser')

table = soup.find('table')
rows = table.find_all('tr')[1:]  # Skip the table header row

colors = []
for row in rows:
    color_data = row.find('td', recursive=False).text
    colors.extend(color_data.split(', '))

most_worn_color = max(set(colors), key=colors.count)
print("The color mostly worn throughout
