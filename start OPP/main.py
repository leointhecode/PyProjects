from prettytable import PrettyTable

table = PrettyTable()

table.add_column("Pokemon name", ["breloom", "Toxapex", "Arcanine"])
table.add_column("type", ["plant", "water", "fire"])
table.align = "l"

print(table)
