import ply.yacc as yacc
import ply.lex as lex
import os
import codecs
import re
from sys import stdin
from tkinter import Entry, Frame, Label, Tk, Text, filedialog, ttk, messagebox


tokens = [
    "TEXT",
    "NUMERO",
    "CHANNEL1",
    "CHANNEL2",
    "ITEM1",
    "ITEM2",
    "ENCODING",
    "TITLE1",
    "TITLE2",
    "LINK1",
    "LINK2",
    "URL1",
    "URL2",
    "IMAGE2",
    "DESCRIPTION1",
    "DESCRIPTION2",
    "CATEGORY1",
    "CATEGORY2",
    "COPYRIGHT1",
    "COPYRIGHT2",
    "IMAGE1",
    "WIDTH1",
    "WIDTH2",
    "HEIGHT1",
    "HEIGHT2",
    "RSS2",
    "RSS1",
    "XML",
    "TOKENURL",
    "VERSION1",
    "VERSION2",
]
H = 0
a = 0
head = 0
band_text = 0
band_im = 0
file = ""


def t_newline(t):
    r"\n+"
    global lineas
    t.lexer.lineno += len(t.value)
    file.write(os.linesep)


def t_CHANNEL1(t):
    r"<channel>"
    file.write("<head>")
    return t


def t_CHANNEL2(t):
    r"</channel>"
    return t


def t_ITEM1(t):
    r"<item>"
    global head
    if head == 0:
        file.write("</head>\n<body>")
    head = +1
    return t


def t_ITEM2(t):
    r"</item>"
    return t


def t_TITLE1(t):
    r"<title>"
    global band_text
    band_text = 1
    global H
    global band_im
    if H <= 1:
        file.write("<H1>")
        H += 1
    else:
        if band_im == 0:
            file.write("<H3>")
    return t


def t_TITLE2(t):
    r"</title>"
    global band_text
    band_text = 0
    global H
    global band_im
    if H <= 1:
        file.write("</H1>")
        H += 1
    else:
        if band_im == 0:
            file.write("</H3>")
    return t


def t_LINK1(t):
    r"<link>"
    global a
    if a <= 1:
        file.write("<a>")
        a += 1
    return t


def t_LINK2(t):
    r"</link>"
    global a
    if a <= 1:
        file.write("</a>")
        a += 1
    return t


def t_URL1(t):
    r"<url>"
    return t


def t_URL2(t):
    r"</url>"
    return t


def t_TOKENURL(t):
    r"(https|http|ftps|ftp)\://([a-zA-Z]+|ñ|á|é|í|ó|ú|Á|É|Í|Ó|Ú|[0-9]+|\?+|\=+|;|&|\-+|_+|\.+)+(\:[0-9]+|)(/([a-zA-Z]+|ñ|á|é|í|ó|ú|Á|É|Í|Ó|Ú|[0-9]+|\-+|_+|\?+|\=+|;|&|\.+|/+)+|)(\#([a-zA-Z]+|ñ|á|é|í|ó|ú|Á|É|Í|Ó|Ú|[0-9]+|\-+|_+|\?+|\=+|;|&|\.+|/+)+|)"
    if a == 1:
        file.write(t.value)
    return t


def t_DESCRIPTION1(t):
    r"<description>"
    global band_text
    band_text = 1
    file.write("<p>")
    return t


def t_DESCRIPTION2(t):
    r"</description>"
    global band_text
    band_text = 0
    file.write("</p>")
    return t


def t_CATEGORY1(t):
    r"<category>"
    return t


def t_CATEGORY2(t):
    r"</category>"
    return t


def t_COPYRIGHT1(t):
    r"<copyright>"
    return t


def t_COPYRIGHT2(t):
    r"</copyright>"
    return t


def t_IMAGE1(t):
    r"<image>"
    global band_im
    band_im = 1
    return t


def t_IMAGE2(t):
    r"</image>"
    global band_im
    band_im = 0
    return t


def t_WIDTH1(t):
    r"<width>"
    return t


def t_WIDTH2(t):
    r"</width>"
    return t


def t_HEIGHT1(t):
    r"<height>"
    return t


def t_HEIGHT2(t):
    r"</height>"
    return t


def t_XML(t):
    r"<\?xml"
    file.write("<!DOCTYPE html>")
    return t


def t_VERSION2(t):
    r'version="\d+\.\d+">'
    return t


def t_VERSION1(t):
    r'version="\d+\.\d+"'
    return t


def t_RSS1(t):
    r"<rss"
    file.write("<html>")
    return t


def t_RSS2(t):
    r"</rss>"
    global head
    if head == 0:
        file.write("</head>\n<body>")

    file.write("</body>\n</html>")
    return t


def t_ENCODING(t):
    r'encoding="((UTF|utf)\-\d+|(ISO|iso)\-\d+\-\d+)"(|\ +)\?>'
    return t


def t_NUMERO(t):
    r"\d+"
    t.value = int(t.value)
    return t


def t_tabulado(t):
    r"\t"
    file.write("\t")
    pass


def t_espacio(t):
    r"\ "
    file.write(" ")
    pass


t_ignore = "\r"


def t_TEXT(t):
    r'([a-zA-Z]+|ñ+|[0-9]+|á|é|í|ó|ú|Á|É|Í|Ó|Ú|\-|_|\#|&|\(|\)|\?|\¿|!|¡|\,|\=|\.|/+|"|;|:|\ +)+'
    if band_text == 1 and band_im == 0:
        file.write(t.value)
    return t


def t_error(t):
    t.lexer.skip(1)


lexer = lex.lex()

# PARSER: declaración de las producciones


def p_sigma(p):
    """sigma : XML VERSION1 ENCODING RSS1 VERSION2 CHANNEL1 main cuerpo CHANNEL2 RSS2
    | XML VERSION2 RSS1 VERSION2 CHANNEL1 main cuerpo CHANNEL2 RSS2"""


def p_x(p):
    """main : TITLE1 tn TITLE2 LINK1 TOKENURL LINK2 DESCRIPTION1 tn DESCRIPTION2
    | TITLE1 tn TITLE2 DESCRIPTION1 tn DESCRIPTION2 LINK1 TOKENURL LINK2
    | TITLE1 tn TITLE2 LINK1 TOKENURL LINK2 CATEGORY1 tn CATEGORY2 DESCRIPTION1 tn DESCRIPTION2
    | TITLE1 tn TITLE2 DESCRIPTION1 tn DESCRIPTION2 CATEGORY1 tn CATEGORY2 LINK1 TOKENURL LINK2
    | TITLE1 tn TITLE2 DESCRIPTION1 tn DESCRIPTION2 LINK1 TOKENURL LINK2 CATEGORY1 tn CATEGORY2
    | TITLE1 tn TITLE2 CATEGORY1 tn CATEGORY2 LINK1 TOKENURL LINK2 DESCRIPTION1 tn DESCRIPTION2
    | TITLE1 tn TITLE2 CATEGORY1 tn CATEGORY2 DESCRIPTION1 tn DESCRIPTION2 LINK1 TOKENURL LINK2
    | TITLE1 tn TITLE2 LINK1 TOKENURL LINK2 DESCRIPTION1 tn DESCRIPTION2 CATEGORY1 tn CATEGORY2
    | LINK1 TOKENURL LINK2 TITLE1 tn TITLE2 DESCRIPTION1 tn DESCRIPTION2
    | LINK1 TOKENURL LINK2 DESCRIPTION1 tn DESCRIPTION2 TITLE1 tn TITLE2
    | LINK1 TOKENURL LINK2 TITLE1 tn TITLE2 DESCRIPTION1 tn DESCRIPTION2 CATEGORY1 tn CATEGORY2
    | LINK1 TOKENURL LINK2 TITLE1 tn TITLE2 CATEGORY1 tn CATEGORY2 DESCRIPTION1 tn DESCRIPTION2
    | LINK1 TOKENURL LINK2 DESCRIPTION1 tn DESCRIPTION2 TITLE1 tn TITLE2 CATEGORY1 tn CATEGORY2
    | LINK1 TOKENURL LINK2 DESCRIPTION1 tn DESCRIPTION2 CATEGORY1 tn CATEGORY2 TITLE1 tn TITLE2
    | LINK1 TOKENURL LINK2 CATEGORY1 tn CATEGORY2 TITLE1 tn TITLE2 DESCRIPTION1 tn DESCRIPTION2
    | LINK1 TOKENURL LINK2 CATEGORY1 tn CATEGORY2 DESCRIPTION1 tn DESCRIPTION2 TITLE1 tn TITLE2
    | DESCRIPTION1 tn DESCRIPTION2 TITLE1 tn TITLE2 LINK1 TOKENURL LINK2
    | DESCRIPTION1 tn DESCRIPTION2 LINK1 TOKENURL LINK2 TITLE1 tn TITLE2
    | DESCRIPTION1 tn DESCRIPTION2 TITLE1 tn TITLE2 LINK1 TOKENURL LINK2 CATEGORY1 tn CATEGORY2
    | DESCRIPTION1 tn DESCRIPTION2 TITLE1 tn TITLE2 CATEGORY1 tn CATEGORY2 LINK1 TOKENURL LINK2
    | DESCRIPTION1 tn DESCRIPTION2 LINK1 TOKENURL LINK2 TITLE1 tn TITLE2 CATEGORY1 tn CATEGORY2
    | DESCRIPTION1 tn DESCRIPTION2 LINK1 TOKENURL LINK2 CATEGORY1 tn CATEGORY2 TITLE1 tn TITLE2
    | DESCRIPTION1 tn DESCRIPTION2 CATEGORY1 tn CATEGORY2 TITLE1 tn TITLE2 LINK1 TOKENURL LINK2
    | DESCRIPTION1 tn DESCRIPTION2 CATEGORY1 tn CATEGORY2 LINK1 TOKENURL LINK2 TITLE1 tn TITLE2
    | CATEGORY1 tn CATEGORY2 TITLE1 tn TITLE2 LINK1 TOKENURL LINK2 DESCRIPTION1 tn DESCRIPTION2
    | CATEGORY1 tn CATEGORY2 TITLE1 tn TITLE2 DESCRIPTION1 tn DESCRIPTION2 LINK1 TOKENURL LINK2
    | CATEGORY1 tn CATEGORY2 LINK1 TOKENURL LINK2 TITLE1 tn TITLE2 DESCRIPTION1 tn DESCRIPTION2
    | CATEGORY1 tn CATEGORY2 LINK1 TOKENURL LINK2 DESCRIPTION1 tn DESCRIPTION2 TITLE1 tn TITLE2
    | CATEGORY1 tn CATEGORY2 DESCRIPTION1 tn DESCRIPTION2 TITLE1 tn TITLE2 LINK1 TOKENURL LINK2
    | CATEGORY1 tn CATEGORY2 DESCRIPTION1 tn DESCRIPTION2 LINK1 TOKENURL LINK2 TITLE1 tn TITLE2
    """


def p_l(p):
    """tn : TEXT
    | NUMERO TEXT"""


def p_y(p):
    """cuerpo : item
    | copyright item
    | image item
    | item image
    | copyright image item
    | copyright item image
    | image copyright item
    | image item copyright
    | item image copyright
    | item copyright image"""


def p_j(p):
    """item : ITEM1 main ITEM2
    | ITEM1 main ITEM2 item"""


def p_cop(p):
    """copyright : COPYRIGHT1 tn COPYRIGHT2"""


def p_imag(p):
    """image : IMAGE1 URL1 TOKENURL URL2 TITLE1 tn TITLE2 LINK1 TOKENURL LINK2 wh IMAGE2
    | IMAGE1 URL1 TOKENURL URL2 LINK1 TOKENURL LINK2 TITLE1 tn TITLE2 wh IMAGE2
    | IMAGE1 TITLE1 tn TITLE2 URL1 TOKENURL URL2 LINK1 TOKENURL LINK2 wh IMAGE2
    | IMAGE1 TITLE1 tn TITLE2 LINK1 TOKENURL LINK2 URL1 TOKENURL URL2 wh IMAGE2
    | IMAGE1 LINK1 TOKENURL LINK2 TITLE1 tn TITLE2 URL1 TOKENURL URL2 wh IMAGE2
    | IMAGE1 LINK1 TOKENURL LINK2 URL1 TOKENURL URL2 TITLE1 tn TITLE2 wh IMAGE2
    | IMAGE1 URL1 TOKENURL URL2 TITLE1 tn TITLE2 LINK1 TOKENURL LINK2 IMAGE2
    | IMAGE1 URL1 TOKENURL URL2 LINK1 TOKENURL LINK2 TITLE1 tn TITLE2 IMAGE2
    | IMAGE1 TITLE1 tn TITLE2 URL1 TOKENURL URL2 LINK1 TOKENURL LINK2 IMAGE2
    | IMAGE1 TITLE1 tn TITLE2 LINK1 TOKENURL LINK2 URL1 TOKENURL URL2 IMAGE2
    | IMAGE1 LINK1 TOKENURL LINK2 TITLE1 tn TITLE2 URL1 TOKENURL URL2 IMAGE2
    | IMAGE1 LINK1 TOKENURL LINK2 URL1 TOKENURL URL2 TITLE1 tn TITLE2 IMAGE2"""


def p_wehi(p):
    """wh : HEIGHT1 NUMERO HEIGHT2
    | WIDTH1 NUMERO WIDTH2
    | HEIGHT1 NUMERO HEIGHT2 WIDTH1 NUMERO WIDTH2
    | WIDTH1 NUMERO WIDTH2 HEIGHT1 NUMERO HEIGHT2"""


def p_error(p):
    global correcto
    correcto = 1
    pantalla1.insert(
        "1.0",
        "Error de sintaxis en la línea "
        + str(p.lineno)
        + "\nVerifique la cadena "
        + str(p.value)
        + "\n\n",
    )


parser = yacc.yacc()

# INTERFAZ GRAFICA
NombreArch = "Escrito.rss"
correcto = 0

ventana_principal = Tk()
ventana = Frame(ventana_principal)
ventana_principal.config(bg="thistle4")
ventana_principal.resizable(0, 0)

codigo = ""


# Funcion abrir archivo
def copiar():
    global codigo, file, correcto
    codigo = pantalla.get("1.0", "end-1c")
    file = open(NombreArch.replace(".rss", ".html"), "w")
    lexer.lineno = 1
    correcto = 0
    parser.parse(codigo)
    file.close()
    if codigo != "":
        if correcto == 0:
            messagebox.showinfo(":)", "Compilación Exitosa")


# Funcion abrir archivo
def abrirarchivo():
    global NombreArch
    NombreArch = filedialog.askopenfilename(
        initialdir="/./prueba",
        title="Select a File",
        filetypes=(
            ("Rss files", "*.rss*"),
            ("Text files", "*.txt*"),
            ("all files", "*.*"),
        ),
    )
    Archivo = open(NombreArch, "r", encoding="utf-8")
    pantalla.delete("1.0", "end")
    pantalla.insert("1.0", Archivo.read())


# Inicilizar la ventana con un titulo
ventana_principal.title("Analizador Léxico-Sintáctico")

# Texto
Label_text = Entry(ventana)
Label_text = Label(text="Analizador RSS")
Label_text.config(
    font=("Helvetica 25 bold"), background="thistle4", foreground="gray10"
)
Label_text.grid(row=0, column=0, columnspan=5, pady=20)

# Caja de texto
pantalla = Entry(ventana)
pantalla = Text(
    state="normal",
    width=100,
    height=20,
    background="gray90",
    foreground="black",
    font=("Helvetica", 10),
)
# Ubicar caja
pantalla.grid(row=1, column=0, columnspan=4, padx=10, pady=10)

# Caja de texto1
pantalla1 = Entry(ventana)
pantalla1 = Text(
    state="normal",
    width=100,
    height=10,
    background="gray90",
    foreground="black",
    font=("Helvetica", 10),
)
# Ubicar caja1
pantalla1.grid(row=2, column=0, columnspan=4, padx=10, pady=10)

# Botones
style = ttk.Style()
style.configure(
    "W.TButton",
    font=("calibri", 10, "bold", "underline"),
    border=5,
    borderwidth=5,
    background="#ab28bd",
    bd=5,
)
# Boton Abrir archivo
ventana.boton_abrirarchivo = ttk.Button(
    text="Abrir Archivo", command=abrirarchivo, style="W.TButton", width=20
).grid(row=3, column=0, pady=15, columnspan=2)
# Boton compilar
ventana.boton_compilar = ttk.Button(
    text="Compilar", command=copiar, style="W.TButton", width=20
).grid(row=3, column=1, padx=10, pady=15, columnspan=2)
# Boton Exit
ventana.boton_cerrar = ttk.Button(
    ventana_principal,
    text="Exit",
    command=lambda: ventana_principal.quit(),
    style="W.TButton",
    width=20,
).grid(row=3, column=2, pady=15, columnspan=2)
ventana_principal.mainloop()
