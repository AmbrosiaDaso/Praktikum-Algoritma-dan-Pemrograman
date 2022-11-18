data = "ini adalah string"
print (data)
print(type(data))

#1. cara menghitung string
'''
1.dengan menggunakan single quote '...'
2.dwngan menggunakan double quote "..."
'''

data = 'Menggunakan single quote'
print(data)

data = "Menggunakan double quote"
print(data)
print("'Hallo,apa kabar?'")
print("'Hallo,apa kabar?'")
print("ini adalah hari jumat")


#2.Menggunakan tanda\

#membuat tanda 'menjadi string
print('mari shalat jum\'at')
print('g\'day,isn\'t it?')

#backlash
print("C:\\user\\Ucup")

#tab
print("ucup\t\t\totong,semakin jauhan")

#backspace
print("ucup \botong,jadi deketan")

#newline
print("baris pertama.\nbaris kedua.") # LF -> line feed -> unix,macos,linux
print("baris pertama.\rbaris kedua.") # CR -> carriage return -> commodore,acorn,lisp


print("baris pertama.\r\nbaris kedua.") # CRLF -> line feed carriage retirn -> dipakai oleh windows

# 3. String literal atau raw

# hati-hati
print('C:\new folder')# akan salah pathnya

#menggunakan raw string
print(r'C:\new folder')

# multiline literal string
print("""
Nama : Ucup
Kelas : 3 SD
""")
# multiline literal string dan RAW
print(""" 
Nama : Ucup
Kelas : 3 SD\nnew normal
Website : www.ucup.com/newID
""")