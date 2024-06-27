#include <iostream>
using namespace std;

//Funcion para realizar el algoritmo de ordenamiento burbuja 
void ordenamiento(int arr[], int n){
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n - 1 ; j++) {
            if (arr[j] > arr[j + 1]){
                // Intercambiar elementos si estan desordenados
                int aux = arr[j];
                arr[j] = arr[j + 1];
                arr[j+1] = aux;
                
            }
        }
    }
    for (int i = 0; i < n; i++) {
        cout <<arr[i] << " ";
    }
    cout << endl;
}

//Funcion para imprimir el array
void imprimir_Array(int arr[], int n){
    for (int i = 0; i < n; i++) {
        cout <<arr[i] << " ";
    }
    cout << endl;
}

int main(){
   //definir el tamanho del array
    int n;
    cout <<"Ingrese el tamanho del array: ";
    cin >> n;
    
    //definir el array con el tamanho ingresado
    int *arr = new int [n] ;

    //Llenar el array con los elementos ingresados por el usuario
    cout << "Ingrese los elementos del array: ";
    for (int i = 0; i <  n ; i++){
        cin >> arr[i];
    }
    
    //imprimir array original
    cout << "Array original: ";
    imprimir_Array(arr, n);

    //ordenar el array usando ordenamiento burbuja
    //Imprimir el array ordenado
    cout << "Array ordenado: ";
    ordenamiento(arr, n);

    return 0;
}
