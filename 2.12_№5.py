l = ["Oleg Protasov 25", "Max Protasov 19", "Sasha Protasov 46", "Petya Protasov 37"]
print(sorted(l, key = lambda x: int(x[-2:])))
print(sorted(l, key = lambda x: int(x[-2:]))[0])
