#include <iostream>
#include <algorithm> //para usar funciones lower
#include <cctype> // para usar funciones de manipulacion de caracteres std: isalnum y std: tolower.
#include <string> // para manejar caracteres

using namespace std ;

bool esPalindromo(const string& str) {
    string limpio;
    
    //Eliminar caracteres no alfanumericos y convertir a minisculas
    for (char c : str) {
        if (isalnum(c)) {
            limpio += tolower(c);
        }
    }

    //Comprobar si la cadena limpia es un palindromo
    int n = limpio.size();
    for (int i = 0; i < n /2; ++i){
        if (limpio[i] != limpio[n - 1 - i]){
            return false;
        }
    }
    return true;
}

int main(){
    string entrada;
    cout << "Ingresa una cadena de caracteres: ";
    getlinea(cin, entrada);

    if (esPalindromo(entrada)){
        cout << "La cadena es un palindromo.\n ";
    }else{
        cout << "La cadena no es un palindromo.\n ";
    }

    return 0;

}

