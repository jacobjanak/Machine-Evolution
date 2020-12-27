
# prints a tree to the console
def display_tree(tree):
    lines, *_ = display_aux(tree)
    for line in lines:
        print(line)


# returns list of strings, width, height, and horizontal coordinate of the root
def display_aux(node):

    # display value for non-if nodes
    if len(node.children) == 0:
        line = '%s' % node.value
        width = len(line)
        height = 1
        middle = width // 2
        return [line], width, height, middle

    # display if nodes
    else:
        right, m, q, y = display_aux(node.children[1])
        left, n, p, x = display_aux(node.children[0])
        s = '%s?' % (node.value)
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
        second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
        if p < q: left += [n * ' '] * (q - p)
        elif q < p: right += [m * ' '] * (p - q)
        zipped_lines = []
        for i in range(len(left)):
            zipped_lines.append([left[i], right[i]])
        lines = [first_line, second_line]
        for zipped in zipped_lines:
            a, b = zipped[0], zipped[1]
            lines.append(a + u * ' ' + b)
        return lines, n + m + u, max(p, q) + 2, n + u // 2