import json
from bs4 import BeautifulSoup


def write_data_to_html(data, html_path, output_path='report/report.html'):
    with open(html_path, 'r') as html_file:
        soup = BeautifulSoup(html_file.read(), 'html.parser')
        soup.find("script", id='data').string = "let data = " +  json.dumps(data)
        open(output_path, 'w').write(str(soup))