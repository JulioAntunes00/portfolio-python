#include <iostream>
#include <cstdlib>
using namespace std;

int main()
{
    float nota1;
    float nota2;
    float media;
    
    cout<<"Qual sua nota 1?: \n";
    cin>>nota1;
    
    cout<<"Qual sua nota 2?: \n";
    cin>>nota2;
    
    media = (nota1 + nota2) / 2;
    cout<<"Sua média foi de: "<<media<<"\n";
    
    if (media>=7)
        {
            cout<<"Aprovado";
        }
    else
        {
            cout<<"Reprovado";
        }
    
    system("PAUSE");
    return 0;
    
}
