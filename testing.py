import re
from tokens_scanner import Scanner, TokenType

input_string = """
                <!DOCTYPE article>
                <article>
                    <info>
                    <title>El titulo del articulo</title>
                    <author>
                        <firstname>Juan</firstname>
                        <surname>Perez</surname>
                    </author>
                </article>
                """
s = Scanner(input_string)
tokens = s.scanAll()

rule = r"^()$"

findAll = re.search(rule, input_string)

# print(findAll)

# print(tokens)

# p = re.compile(r"([a-z]|[A-Z])+")
# p.findall("ahjkfgOIJFEWK12039543")
# print(p)

# for match in secuencia:
#    print(match.group())
