def échequier():   
    graine = 0 
    print("voici le resultat:")
    for i in range(64):
        graine_case = 2 ** i
        graine += graine_case
        print(f"Case{i+1}: {graine_case} grains de riz")
    return graine
total = échequier()
print(f"\n le nombre total des grains de riz est :",total)


