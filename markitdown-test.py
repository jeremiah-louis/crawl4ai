from markitdown import MarkItDown

md = MarkItDown(enable_plugins=False) # Set to True to enable plugins
result = md.convert("https://en.m.wikipedia.org/wiki/The_World's_Billionaires")
print(result.text_content)