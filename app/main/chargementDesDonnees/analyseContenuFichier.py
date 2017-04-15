lignes = [ ["Mazda","RX7"], ["Audi","A3","2.0 TDI"] ]

col = {}
col["marque"] = []
col["modele"] = []
i = 0
while i < len(lignes):
	col["marque"].append(lignes[i][0])
	col["modele"].append(lignes[i][1])
	i+=1

print(col)

if __name__ == "__main__":
	input("Appuyez sur une touche pour quitter...")