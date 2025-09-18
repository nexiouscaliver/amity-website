import csv


# template = """

# <tr>
#     <td><span style="font-size: 14px;">
#         {title}</span></td>
#     <td><span style="font-size: 14px;">
#         {author}</span></td>
#     <td><span style="font-size: 14px;">
#         {book_title}</span></td>
#     <td><span style="font-size: 14px;">
#         {year}</span></td>
#     <td><span style="font-size: 14px;">
#         {publisher}</span></td>
#     <td><span style="font-size: 14px;">
#         {issn}</span></td>
# </tr>

# """

template = """


<tr>
<td style="color:black;font-size:15px;font-weight:400;font-style:normal;text-decoration:none;font-family:Helvetica;text-align:justify;vertical-align:middle;border:none;height:86.25pt;width:86pt;"><span style="font-size: 14px;">{author}</span></td>
<td style="color:black;font-size:15px;font-weight:400;font-style:normal;text-decoration:none;font-family:Helvetica;text-align:justify;vertical-align:middle;border:none;width:145pt;"><span style="font-size: 14px;">{book_title}</span></td>
<td style="color:black;font-size:15px;font-weight:400;font-style:normal;text-decoration:none;font-family:Helvetica;text-align:justify;vertical-align:middle;border:none;width:97pt;"><span style="font-size: 14px;">{journal}</span></td>
<td style="color:black;font-size:15px;font-weight:400;font-style:normal;text-decoration:none;font-family:Helvetica;text-align:center;vertical-align:middle;border:none;width:92pt;"><span style="font-size: 14px;">{year}</span></td>
<td style="color:black;font-size:15px;font-weight:400;font-style:normal;text-decoration:none;font-family:Helvetica;text-align:justify;vertical-align:middle;border:none;width:126pt;"><span style="font-size: 14px;">{issn}</span></td>
<td style="color:black;font-size:15px;font-weight:400;font-style:normal;text-decoration:none;font-family:Helvetica;text-align:justify;vertical-align:middle;border:none;width:98pt;"><span style="font-size: 14px;">{country}</span></td>
</tr>


"""
final_html = []
#csv file parser
def csv_parser(csv_file):
    #csv file formate : Name of Author,Book Title,Year of Publication,Publisher Name,ISBN,Country
    global final_html
    with open(csv_file, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)
            filled_template = template.format(author=row[0], book_title=row[1], journal=row[2], year=row[3], issn=row[4], country=row[5])
            print(filled_template)
            final_html.append(filled_template)
    return final_html

csv_parser('ABSNEW(Sheet3).csv')
print(final_html)

with open('ABSNEW(Sheet3).html', 'w') as f:
    for i in final_html:
        f.write(i)
print('HTML file generated successfully')