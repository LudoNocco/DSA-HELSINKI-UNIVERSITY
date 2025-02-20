def analyze_route(grid):
    righe, colonne = len(grid), len(grid[0])
    
    # Find the starting position of 'R'
    for r in range(righe):
        for c in range(colonne):
            if grid[r][c] == 'R':
                posizione = (r, c)
    
    direzioni = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    direzione_attuale = 0  
    
    visitati = set()
    stati_visti = set()  
    
    while posizione not in stati_visti:
        stati_visti.add(posizione)
        visitati.add(posizione)
        
        r, c = posizione
        dr, dc = direzioni[direzione_attuale]
        nuovo_r, nuovo_c = r + dr, c + dc
        
        if not (0 <= nuovo_r < righe and 0 <= nuovo_c < colonne):
            return (len(visitati), True)  # Exited
        
        if grid[nuovo_r][nuovo_c] == '#':
            direzione_attuale = (direzione_attuale + 1) % 4  
        else:
            posizione = (nuovo_r, nuovo_c) 

    return (len(visitati), False)  
