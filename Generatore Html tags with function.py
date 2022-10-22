paragrah1 = 'THis is paragraph 1'
paragrah2 = 'THis is paragraph 2'
paragrah3 = 'THis is paragraph 3'
paragrah4 = 'THis is paragraph 4'

paragrah1_html = f'<p>His is {paragrah1}</p>'
paragrah2_html = f'<p>His is {paragrah2}</p>'
paragrah3_html = f'<p>His is {paragrah3}</p>'
paragrah4_html = f'<p>His is {paragrah4}</p>'

# def paragraph_html(paragraph):
#     c = f'<p>His is {paragraph}</p>'
#     return c
# b = paragraph_html(paragrah2)
# print(b)


def heading(h2):
    text = f'<h2>{h2.title()}</h2>'
    return text
x = heading('top ten Best snorkel mask')
print(x)
