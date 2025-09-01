let a  = 'Hello Wolrd';
console.log(a);

class retangulo {
    //atributos
    lado1: number = 0;
    lado2: number = 0;

    //método
    calcularArea() {
        return this.lado1 * this.lado2;
    }
}

let retangulo1 = new retangulo();

retangulo1.lado1 = 10;
retangulo1.lado2 = 20;

console.log(retangulo1.calcularArea()); 

let retangulo2 = new retangulo();

retangulo1.lado1 = 5;
retangulo1.lado2 = 10;

console.log(retangulo1.calcularArea());