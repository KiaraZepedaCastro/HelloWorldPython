from pathlib import Path

# Absolute path
#    c:\Program Files\Microsoft
#    /usr/local/bin
# Relative path


path = Path("ecommerce")
print(path.exists())

path = Path("email")
# print(path.mkdir())   makes
# print(path.rmdir()) removes

path = Path()
for file in path.glob('*.*'):
    print(file)
#*, *.*, *.py
