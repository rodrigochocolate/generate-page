template_HTML = '''<!DOCTYPE html>
<html lang="pt-br">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <link rel="stylesheet" href="reset.css">
  <link rel="stylesheet" href="template.css">
  <title>Template</title>
</head>
<body>
  <header class="header">
  	<h1>Matemática Curiosa</h1>
  </header>

  <main class="main">
    
  </main>

  <footer class="footer">
    
  </footer>
</body>
</html>'''

path_new_page = str(input('Page directory path (current = ENTER): ')) + '/'
name_new_page = str(input('Page name: ')) + '.html'
new_page = ''

# Ensuring that name_new_page has a unique .html
if name_new_page.count('.html') > 1:
  name_new_page.replace('.html', '')
  name_new_page += '.html'

# Fixing bug: When trying to create a file starting with "/" and then its name
if path_new_page == '/':
  path_new_page = './'

new_page = path_new_page + name_new_page

# It will only create the file (new_page) if it doesn't exist yet
try:
	page = open(new_page)
	page.close()
except:
	new_page = open(new_page, 'a')
	new_page.write(template_HTML)
else:
  raise ValueError(f'The {name_new_page} page already exists!')
