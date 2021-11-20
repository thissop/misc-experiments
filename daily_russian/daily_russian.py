class DailyRussian: 
    def __init__(self, instance_name):
        self.instance_name = instance_name

    def return_image_information(self): 
        import requests
        from bs4 import BeautifulSoup

        r = requests.get('http://masterrussian.com/').text.split('\n')

        base_index = 0
        for line_index, line in enumerate(r): 
            if "<img src=/graphics/signs" in line: 
                image_line = line

                line_text = BeautifulSoup(image_line, features='lxml').text
                
                for char_index, char in enumerate(image_line): 
                    if char == '=': 
                        link_start_index = char_index+1
                    elif char == '>':
                        link_end_index = char_index
                        break
                        
                image_link = 'http://masterrussian.com'+image_line[link_start_index:link_end_index]
                

                russian_start_index = line_text.index('Russian')
                russian_end_index = line_text.index('English')

                russian_text = line_text[russian_start_index:russian_end_index]
                english_text = line_text[russian_end_index:]

                break 

        return russian_text, english_text, image_link
    