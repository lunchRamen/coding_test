#include <iostream>
#include<vector>
using namespace std;

int solution(vector<vector<int>> board)
{
    int ans=board[0][0];
    int sero=board.size();
    int garo=board[0].size();
    
    for(int i=1;i<sero;i++){
        for(int j=1;j<garo;j++){
            if(board[i][j]==1){
                board[i][j]=min(board[i][j-1],min(board[i-1][j],board[i-1][j-1]))+1;
                ans=max(ans,board[i][j]);
            }
        }
    }
    return ans*ans;
}
