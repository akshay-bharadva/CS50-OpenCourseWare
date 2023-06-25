def meow(n: int) -> str:
    return "meow " * n


number: int = int(input("Number: ").strip())
meows: str = meow(number)
print(meows)
