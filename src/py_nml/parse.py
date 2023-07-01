from dataclasses import dataclass


@dataclass
class Keyword:
    name: str
    arguments: list[str]


def parse(text: str) -> list[Keyword]:
    result: list[Keyword] = []
    lines = text.splitlines()

    for line in lines:
        words = line.split()

        if len(words) == 1:
            result.append(Keyword(name=words[0], arguments=[]))
        elif len(words) > 1:
            result.append(Keyword(name=words[0], arguments=words[1:]))

    return result
