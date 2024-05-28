INF = 10**9

for _ in range(int(input())):
    N, W = map(int, input().split())
    won = [([0]+list(map(int, input().split()))),([0]+list(map(int, input().split())))]
    DP = [[INF]*3 for i in range(N+1)]
    ans = INF
    if N == 1:
        if won[1][1]+won[0][1]<=W:
            print(1)
        else:
            print(2)
    else:
        #case1
        DP[0][0] = 0
        if won[1][1]+won[0][1]<=W:
            DP[1][0] = 1
        else:
            DP[1][0] = 2
        DP[1][1] = 1
        DP[1][2] = 1
        
        for i in range(2, N+1):
            #DP[i][0]
            if won[0][i]+won[1][i] <= W:
                DP[i][0] = min(DP[i][0], DP[i-1][0]+1)
            else:
                DP[i][0] = min(DP[i][0], DP[i-1][0]+2)
            if won[0][i-1]+won[0][i] <= W and won[1][i-1]+won[1][i] <= W:
                DP[i][0] = min(DP[i][0], DP[i-2][0]+2)
            elif won[0][i-1]+won[0][i] <= W:
                DP[i][0] = min(DP[i][0], DP[i-1][2]+2)
            elif won[1][i-1]+won[1][i] <= W:
                DP[i][0] = min(DP[i][0], DP[i-1][1]+2)
            
            #DP[i][1]
            DP[i][1] = min(DP[i][1], DP[i-1][0]+1)
            if won[0][i-1]+won[0][i] <= W:
                DP[i][1] = min(DP[i][1], DP[i-1][2]+1)
            
            #DP[i][2]
            DP[i][2] = min(DP[i][2], DP[i-1][0]+1)
            if won[1][i-1]+won[1][i] <= W:
                DP[i][2] = min(DP[i][2], DP[i-1][1]+1) 
        ans = min(ans, DP[N][0])
        
        #case 2: inner combine(ㅗ)
        if won[0][1]+won[0][N] <= W:
            DP = [[INF]*3 for i in range(N+1)]
            DP[0][0] = INF
            DP[1][0] = 2
            DP[1][1] = min(1, DP[1][1])
            DP[1][2] = INF
            for i in range(2, N+1):
                if i != N:
                    #DP[i][1]
                    if won[0][i]+won[1][i] <= W:
                        DP[i][0] = min(DP[i][0], DP[i-1][0]+1)
                    else:
                        DP[i][0] = min(DP[i][0], DP[i-1][0]+2)
                    if won[0][i-1]+won[0][i] <= W and won[1][i-1]+won[1][i] <= W:
                        DP[i][0] = min(DP[i][0], DP[i-2][0]+2)
                    elif won[0][i-1]+won[0][i] <= W:
                        DP[i][0] = min(DP[i][0], DP[i-1][2]+2)
                    elif won[1][i-1]+won[1][i] <= W:
                        DP[i][0] = min(DP[i][0], DP[i-1][1]+2)
                    
                    #DP[i][1]
                    DP[i][1] = min(DP[i][1], DP[i-1][0]+1)
                    if won[0][i-1]+won[0][i] <= W:
                        DP[i][1] = min(DP[i][1], DP[i-1][2]+1)
                
                #DP[i][2]
                DP[i][2] = min(DP[i][2], DP[i-1][0]+1)
                if won[1][i-1]+won[1][i] <= W:
                    DP[i][2] = min(DP[i][2], DP[i-1][1]+1)
            ans = min(ans, DP[N][2])
        #case 3: outer combination(ㅜ)
        if won[1][1]+won[1][N] <= W:
            DP = [[INF]*3 for i in range(N+1)]
            DP[0][0] = INF
            DP[1][0] = 2
            DP[1][2] = min(1, DP[1][2])
            DP[1][1] = INF
            for i in range(2, N+1):
                if i != N:
                    #DP[i][1]
                    if won[0][i]+won[1][i] <= W:
                        DP[i][0] = min(DP[i][0], DP[i-1][0]+1)
                    else:
                        DP[i][0] = min(DP[i][0], DP[i-1][0]+2)
                    if won[0][i-1]+won[0][i] <= W and won[1][i-1]+won[1][i] <= W:
                        DP[i][0] = min(DP[i][0], DP[i-2][0]+2)
                    elif won[0][i-1]+won[0][i] <= W:
                        DP[i][0] = min(DP[i][0], DP[i-1][2]+2)
                    elif won[1][i-1]+won[1][i] <= W:
                        DP[i][0] = min(DP[i][0], DP[i-1][1]+2)
                    
                #DP[i][1]
                DP[i][1] = min(DP[i][1], DP[i-1][0]+1)
                if won[0][i-1]+won[0][i] <= W:
                    DP[i][1] = min(DP[i][1], DP[i-1][2]+1)
                
                if i != N:
                    #DP[i][2]
                    DP[i][2] = min(DP[i][2], DP[i-1][0]+1)
                    if won[1][i-1]+won[1][i] <= W:
                        DP[i][2] = min(DP[i][2], DP[i-1][1]+1)
            ans = min(ans, DP[N][1])  
        #case 4: both combination(=)
        if won[0][1]+won[0][N] <= W and won[1][1]+won[1][N] <= W:
            DP = [[INF]*3 for i in range(N+1)]
            DP[0][0] = INF
            DP[1][0] = 2
            DP[1][2] = INF
            DP[1][1] = INF
            for i in range(2, N):
                #DP[i][1]
                if won[0][i]+won[1][i] <= W:
                    DP[i][0] = min(DP[i][0], DP[i-1][0]+1)
                else:
                    DP[i][0] = min(DP[i][0], DP[i-1][0]+2)
                if won[0][i-1]+won[0][i] <= W and won[1][i-1]+won[1][i] <= W:
                    DP[i][0] = min(DP[i][0], DP[i-2][0]+2)
                elif won[0][i-1]+won[0][i] <= W:
                    DP[i][0] = min(DP[i][0], DP[i-1][2]+2)
                elif won[1][i-1]+won[1][i] <= W:
                    DP[i][0] = min(DP[i][0], DP[i-1][1]+2)
                    
                #DP[i][1]
                DP[i][1] = min(DP[i][1], DP[i-1][0]+1)
                if won[0][i-1]+won[0][i] <= W:
                    DP[i][1] = min(DP[i][1], DP[i-1][2]+1)
                else:
                    DP[i][1] = min(DP[i][1], DP[i-1][2]+2)
                
                #DP[i][2]
                DP[i][2] = min(DP[i][2], DP[i-1][0]+1)
                if won[1][i-1]+won[1][i] <= W:
                    DP[i][2] = min(DP[i][2], DP[i-1][1]+1)
                else:
                    DP[i][2] = min(DP[i][2], DP[i-1][1]+2) 
            ans = min(ans, DP[N-1][0]) 
        print(ans)