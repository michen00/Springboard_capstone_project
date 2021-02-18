from re import sub, escape
from num2words import num2words

with open("preprocess", "r") as f:
    f = f.readlines()

noDupesList = lambda x: list(frozenset(x))
convert_nums = lambda x: " ".join(
    [num2words(part) if part.isnumeric() else part for part in x.split()]
)


def clean_most_punc(x):
    for c in "'.,#:!()$":
        x = x.replace(c, "")
    x = x.replace("-", " ")
    return x


def append_converted_nums(x):
    f.append(clean_most_punc(convert_nums(x)))


# initial cleanup
i = len(f) - 1
while i >= 0:
    f[i] = f[i].split(",")[0].replace("&", "and").replace("%", " percent")
    if any(char.isdigit() for char in f[i]):
        f[i] = (
            f[i]
            .replace("1/2", "half")
            .replace("1/3", "third")
            .replace("1/4", "quarter")
        )
        append_converted_nums(f[i])
        f[i] = sub(r"^[^\w]*[0-9]+[\.\/]?[0-9]* (?:oz|lb|in)? ?", "", f[i])
        append_converted_nums(f[i])
    f[i] = clean_most_punc(f[i])
    i -= 1
f = noDupesList(f)


def variants(line_in: str) -> list:
    line_in = line_in.strip()
    holder = []
    subpairs = (
        (
            ("oz", "ounce"),
            ("oz", "ounces"),
            ("ozs", "ounces"),
        ),
        (
            ("lb", "pound"),
            ("lb", "pounds"),
            ("lbs", "pounds"),
        ),
    )
    n = len(subpairs)
    combos = [bin(i)[2:].zfill(n) for i in range(int(n * "1", 2) + 1)]
    patternizer = lambda x: x.join((r"\b", r"\b"))
    substituter = lambda x: [
        sub(patternizer(x[0]), x[1], line_in),
        sub(patternizer(x[1]), x[0], line_in),
    ]
    for combo in combos:
        for i in range(n):
            # assert len(combo) == len(subpairs) == n, "more combinations than elements!"
            if combo[i]:
                subpair = subpairs[i]
                for pattern in subpair:
                    extension = substituter(pattern)
                    if '"' in line_in:
                        extension = [
                            j.replace(patt[0], patt[1])
                            for j in extension
                            for patt in (
                                ('"', " in"),
                                ('"', " inch"),
                                ('"', " inches"),
                                ('"', ""),
                            )
                        ] + [_.split('"')[-1] for _ in extension]
                    if "+" in line_in:
                        extension = [
                            j.replace(patt[0], patt[1])
                            for j in extension
                            for patt in (
                                ("+", " plus"),
                                ("+", ""),
                            )
                        ] + [_.split("+")[-1] for _ in extension]
                holder.extend(extension)
    return noDupesList([_.strip() for _ in holder])


def extend_newlines(x: str) -> None:
    newlines.extend(variants(x))


# add variants
newlines = []
for line in f:
    if "/" in line:
        replacer = lambda x: [
            i.replace("/", "") for i in line.replace("w/out", x).split("w/")
        ]
        for _ in frozenset(
            replacer("without")
            + replacer("w/")
            + [line.replace("w/", "with").replace("/", "")]
        ):
            extend_newlines(_)
    else:
        extend_newlines(line)

# check and write
newlines = sorted(noDupesList(newlines))
for line in newlines:
    if not all([_.isalnum() for _ in line.split()]):
        print("not alphanumeric: " + line)


with open("midprocess", "w") as f:
    f.write("\n".join(newlines))
    f.write("\n")
