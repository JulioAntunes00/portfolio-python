#include <iostream>
using namespace std;

int main()
{
    float nota1;
    float nota2;
    float nota3;
    float nota4;
    float media;
    
    cout << "Qual sua nota 1?: \n";
    cin >> nota1;
    
    cout << "Qual sua nota 2?: \n";
    cin >> nota2;
    
    cout << "Qual sua nota3?: \n";
    cin >> nota3;
    
    cout << "Qual sua nota4?: \n";
    cin >> nota4;
    
    media = (nota1 + nota2 + nota3 + nota4) / 4;
    cout << "Sua media foi de: " << media << "\n";
    
    if (media >= 7)
    {
        cout << "Aprovado";
    }
    
    else if (media >= 5 && media < 7)
    {
        cout << "Ficou de exame";
    }
    
    else
    {
        cout << "Reprovado";
    }
    
    return 0;
    
}
