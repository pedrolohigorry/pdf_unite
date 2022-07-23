import PyPDF2

# Los archivos deben estar en la misma carpeta que el programa
# Los archivos se deben llamar "file1.pdf", "file2.pdf", ...,  "filen.pdf"
# donde n es la cantidad total de archivos

# We create an object of the PdfFileMerger class and assign it to mergeFile
mergeFile = PyPDF2.PdfFileMerger()

# Pedimos el número de archivo inicial y final
i = int(input("Ingresar el número de archivo incial = "))
n = int(input("Ingresar el número de archvio final = "))

# Se van agregando los archivos de forma incremental, primero el 1, luego el 2, ..., hasta el n.
while i <= n :
    ind = str(i)
    file = "file" + ind + ".pdf"
    print(file)
    mergeFile.append(file, bookmark=None, pages=None, import_bookmarks=False)
    i = i + 1

# Se escribe el archivo final en la carpeta
mergeFile.write("archivofinal.pdf")

print("El archivofinal.pdf fue creado con éxito.")
