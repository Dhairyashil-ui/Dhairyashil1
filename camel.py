def word_break(word):
    result = []
    for char in word:
        if char.isupper() and result:
            result.append('_')
        result.append(char.lower())
    return ''.join(result)
def main():
    name = input("camelCase: ")
    result = word_break(name)
    print("snake_case:",result)

main()
