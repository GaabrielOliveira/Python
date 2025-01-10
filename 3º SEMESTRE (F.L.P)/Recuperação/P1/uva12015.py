caso_teste = int(input())

for i in range(1, caso_teste + 1):
    sites = {}
    maior_relevacia = 0  
    
    for _ in range(10):
        site, relevance = input().split()
        relevancia = int(relevancia)
        sites[site] = relevancia 
        
        if relevancia > maior_relevacia:
            maior_relevacia = relevancia
    
    print(f"Case #{i}:")  
    for site, relevancia in sites.items():
        if relevancia == maior_relevacia:
            print(site)