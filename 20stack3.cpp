#include<bits/stdc++.h>
#include<stack>
using namespace std;
int pre(char c){
    int p;
    if(c=='^') p=3;
    else if(c=='*' || c=='/') p=2;
    else if(c=='+' || c=='-') p=1;
    else p=-1;
    return p;
}
void postfixtoinfix(){
    
}

int main(){
    string stri;

    cout<<"enter input : ";
    cin>>stri;
    
    infix_to_prefix(stri);
    cout<<endl;
    cout<<parenthis(stri);

}