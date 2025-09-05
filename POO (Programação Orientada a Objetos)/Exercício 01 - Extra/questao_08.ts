class Circulo {
    raio: number;

    constructor(raio:number) {
        this.raio =raio;
    }

    /** 
     * Método para calcular a área do círculo
     * Fórmula: Área = π * raio²
     */
    calcularArea(): number {
        return Math.PI * this.raio * this.raio;
    }
    
    /** 
     * Calcula o perimetro do círculo
     * 
     * @returns perímetro do círculo
     */
    calcularPerimetro(): number {
        return 2 * Math.PI * this.raio;
    }
}

const meuCirculo = new Circulo(10);

const area = meuCirculo.calcularArea();
const perimetro = meuCirculo.calcularPerimetro();

console.log(`Para um círculo com raio ${meuCirculo.raio}:`);
console.log(`A área é: ${area.toFixed(2)}`);
console.log(`O perímetro é: ${perimetro.toFixed(2)}:`);
