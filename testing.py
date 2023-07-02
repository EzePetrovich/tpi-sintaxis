import re
from tokens_scanner import Scanner, TokenType

# <info><title>El titulo del articulo</title><author><firstname>Juan</firstname><surname>Perez</surname></author>

CHARS_OK = ["#", "-", "_", ":", "&", "?", "=", "/", "."]

input_string = """<!DOCTYPE article>
<article> oasfdposajkepojfoqijdas </article>"""

s = Scanner(input_string)
tokens = s.scanAll()
tokens_flat = []
tokens_string = ""

for t in tokens:
    for t_sub in t["tokens"]:
        tokens_flat.append(str(t_sub))
        tokens_string += f" {str(t_sub)} "

# print(tokens_flat)
# print(tokens_string)
# tokens = [t.name for t in tokens["tokens"]]

R_CHARS_OK = f"[#|-|_|:|&|?|=|/|.]"

R_PROTOCOLS = f"(http|https|ftp|ftps)://"

R_DOMAIN = f"([a-z]|[A-Z]|[0-9])+([.]|[a-z]|[A-Z]|[0-9])*"

R_PORT = f":(\d)+"

R_ROUTE = f"/([a-z]|[A-Z]|[.]|/?)*"

R_FRAGMENT = f"#([a-z]|[A-Z]|[0-9]|{R_CHARS_OK})+"

R_URL_OK = f"{R_PROTOCOLS}({R_DOMAIN})({R_PORT})?({R_ROUTE})?({R_FRAGMENT})?"

rule_structure = f"""

                """
# PROG = f"""^\s{str(TokenType.DOCTYPE)}\s+{str(TokenType.ARTICLE_OPEN)}\s+({rule_structure})*\s+{str(TokenType.ARTICLE_CLOSE)}\s$"""

# findAll = re.search(PROG, tokens_string)

findURL = re.fullmatch(R_URL_OK, "https://localhost:5173/image.jpg#fragment")

if findURL:
    print("La URL es válida.")
    print(findURL)
else:
    print("La URL está mal formada.")

# print(findAll)

# print(str(TokenType.ARTICLE_OPEN) == str((tokens[0]["tokens"][0])))

# p = re.compile(r"([a-z]|[A-Z])+")
# p.findall("ahjkfgOIJFEWK12039543")
# print(p)

# for match in secuencia:
#    print(match.group())
