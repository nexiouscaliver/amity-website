import csv


template = """

<tr>
    <td><span style="font-size: 14px;">
        {title}</span></td>
    <td><span style="font-size: 14px;">
        {author}</span></td>
    <td><span style="font-size: 14px;">
        {book_title}</span></td>
    <td><span style="font-size: 14px;">
        {year}</span></td>
    <td><span style="font-size: 14px;">
        {publisher}</span></td>
    <td><span style="font-size: 14px;">
        {issn}</span></td>
</tr>

"""
final_html = []
#csv file parser
def csv_parser(csv_file):
    #csv file formate : Name of Author,Book Title,Year of Publication,Publisher Name,ISBN
    global final_html
    with open(csv_file, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)
            filled_template = template.format(title=row[0], author=row[1], book_title=row[2], year=row[3], publisher=row[4], issn=row[5])
            print(filled_template)
            final_html.append(filled_template)
    return final_html

csv_parser('ABSBooksChaptersNew.csv')
print(final_html)

with open('ABSChaptersNew.html', 'w') as f:
    for i in final_html:
        f.write(i)
print('HTML file generated successfully')