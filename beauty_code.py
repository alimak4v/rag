import colorsys


def rainbow(text):
    lines = text.splitlines()
    width = max(map(len, lines))
    result = []
    for line in lines:
        colored_line = []
        for x, char in enumerate(line):
            if char != "░":
                hue = x / max(width - 1, 1)
                red, green, blue = colorsys.hsv_to_rgb(hue, 1.0, 1.0)
                r = round(red * 255)
                g = round(green * 255)
                b = round(blue * 255)
                colored_line.append(f"\033[38;2;{r};{g};{b}m{char}\033[0m")
            else:
                colored_line.append(char)
        result.append("".join(colored_line))
    return "\n".join(result) + "\033[0m"
