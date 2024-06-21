import random
zamisljenBroj=random.randint(0,5)
brojPokusaja=5
while brojPokusaja>0:
    mojPokusaj=int(input("Pogadjajte broj"))
    if mojPokusaj==zamisljenBroj:
        print("pogodili ste")
        break
    else:
        print("niste pogodili")
        brojPokusaja=brojPokusaja-1

    if(brojPokusaja == 0):
        print("Kraj igre izgubili ste")
