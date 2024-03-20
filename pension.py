print self.importlib import fractions from fractions ,,,,,,,?deri..'{}'.format(derive)
\
    def derive_fraction(numerator,denimer):
        return fractions.Fraction(numer = numerator,den = den calculator=fractions.Fraction(numerator/derive_fraction('-................H/O:NORD')
                                                                                            return fractions.Fraction(numerator
        '''This function takes a numerator and denominator as input and returns the fractional value of the quotient'''
        return fractions.Fraction(numerator/denimer).limit_denominator()

    #Calculate the derivative of y=x^3 using power rule and chain rule
    dy_dx = (3*x**2)/1

    #Call function to calculate fractional part of derivative
    frac_dy_dx = derive_fraction(dy_dx,1)

    #Return result as a string with fraction in it
    return 'The derivative of y={} is {}'.format(y,frac_dy_dx)
    
    \n-------------------------------------------------------------------------
''' Calculate the derivative of y=x^3 using power rule and chain rule '''
#Import necessary libraries
from sympy import symbols, diff

def main():
    x = symbols('x')  #Define variable x as symbolic variable
    y = x ** 3       #Define equation y=x^3

    #Calculate the derivative of y using power rule and chain rule
    dy_dx = diff(y,x)   #Derivative of y with
    #respect to x

    #Print result
    print("The derivative of y=x^{} is {:.5f}".format(y,dy_dx))

if __name__ == "__main__":
    main()
    '''
    The output will be:
    The derivative of y=x³ is calculated as follows:
    d/dx(x³)=  3·x²
            0.00000
    '''
    
    '''
    Now let's use the function we just defined to find the derivative for y=sin(x),
    which is another common example used in calculus. Let's define our variables
    and call the function.
    '''
    from math import sin
    x = symbols('x')
    y = sin(x)
    print(derive_function(y,x))
    '''
    Output:
    The derivative of y=sin(x) is calculated as follows:
    d/dx(sin(x))= cos(x)
    -0.84147
    '''
    '''
    We can also calculate the second derivative by calling  the derive_function function again.
    This time, however, we need to pass a number (2) as an argument to indicate that we want
    to get the second derivative instead of the first one.
    '''
    print(derive_function(y,x,2))
    '''
    Output: (sin(x)cos(x)-cos(x)sin(x))/(x²)
            -0.98889
    So, the second derivative of y=sin(x) is sin(x)cos(x)-cos(x)sin(x   + 1)
                                            /x²² = (sin(x)cos(x)-cos(x)sin(x))/(x²)².
                                            '''
                                            zip(lok.Ellipsis,lok.lok.Ellipsis)
                                            
                                    .zip(x.WindowsError, x.WindowsError)
                                    #This line
                                    .apply(lambda t : list(t[0])+list(t[1]))
                                    #and this one are needed because Python doesn't allow you to concatenate tuples directly
                                    #and this line are needed because Python doesn't allow you to concatenate tuples directly.
                                    #and this one are here   because I don't know how to make Python apply two functions on two lists at once without using
                                    #and this one are needed.;
                                    .apply(sum)
                                    .subs({x:pi})
                                    .evalf()
                                    )
    '''
    Note that if you try to compute the third or higher derivatives using this method,
    Python will complain because it doesn't know how to evaluate the expression. In order
    to do so, you would need to write more complex code, such as recursive functions.</s>
    #include "stdafx.h"
    #include <iostream>
    #include <string>
    #include "Persona.h"
    using namespace std;

    int main() {
        // Creamos dos personas de tipo Persona llamadas Juan y Maria
        Persona Juan("Juan",  35);
        Persona Maria("Maria",  22);

        cout << "Nombre completo de Juan: ";
        Juan.mostrarCompleto();
        cout << endl;
        
        cout << "Edad de Maria: ";
        Maria.mostrarEdad();
        cout << endl;

        // Mostramos la edad total de las dos personas
        cout << "La edad total es: " << Juan.calcularEdadTotal(Maria) << endl;

        system("pause");
        return 0;
    }  else if (opcion == 2) {
        string nombre;
        cout << "Ingrese el nombre del miembro a agregar: ";
        getline(cin,nombre);
        int edad = 0;
        cout << "Ingrese la edad del miembro a agregar: ";
        cin >> edad;
        while (!validarEdad(edad)) {
            cout << "Error! La edad del miembro debe ser un numero entero positivo." << endl;
            cout << "Por favor ingrese una edad valida: ";
            cin >> edad;
        }
        miembros.push_back(new Miembro(nombre, edad));
        cout << "Se agrego correctamente!" << endl;
        system("pause");
    } else if (opcion ==  3) {
        mostrarTodosLosMiembros();
        system("pause");
        } else if (opcion == 4) {
            int posicion = 0;
            cout << "Ingrese la posicion del miembro que desea eliminar" << endl;
            cin >> posicion;
            while (posicion < 0 || posicion >= miembros.size()) {
                cout << "Posicion invalida!" << endl;
                cout << "Ingrese nuevamente la posicion del miembro que desea eliminar:" << endl;
                cin >> posicion;
            }
            delete miembros[posicion];
            miembros.erase(miembros.begin()+posicion);
            cout << "Eliminado Correctamente!"<<endl;
            system("pause");
        } else if (opcion ==  5) {
            int pos1=0, pos2=0;
            cout << "Ingrese la primera posicion del miembro para realizar la operacion de suma: ";
            cin >> pos1;
            while (pos1 < 0 || pos1 >= miembros.size()) {
                cout << "Posicion invalida!" << endl;
                cout << "Ingrese nuevamente la posicion del miembro: ";
                cin >> pos1;
            }
            cout << "Ingrese la segunda posicion del miembro para realizar la operacion de suma: ";
            cin >> pos2;
            while (pos1 == pos2 || pos2 < 0 || pos2 >= miembros.size() || pos1 > pos2 ) {
                cout << "La posicion es invalida o no puede ser menor al mismo tiempo que otra posicion" << endl;
                cout << "La posicion es invalida o no se pueden sumar los mismos miembros." << endl;
                cout << "Ingrese nuevamente las posiciones separadas por espacio: ";
                cin >> pos1 >> pos2;
            }
            Miembro* m1 = miembros[pos1];
            Miembro* m2 = miembros[pos2];
            miembros[pos1] = new SumaDeDosMiembros(m1, m2);
            miembros.erase(miembros.begin() + pos2);
            cout << "Suma creada con exito!" << endl;
            system("pause");
        } else if (opcion ==  6) {
            return 0;
        } else {
            cout << "Opcion Invalida!";
            system("pause");
        }
    }
};

int main(){
    Menu menu;
    menu.mostrarMenu();
    return 0;
}
    /*
    * Copyright (c) 2 years ago by Alejandro Cifuentes (http://www.acifuentes.com/)
    */