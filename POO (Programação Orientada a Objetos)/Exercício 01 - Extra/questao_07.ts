// Definição da classe Retangulo
class Retangulo {
    // Atributos
    largura: number;
    altura: number;

    // O construtor é um método especial para criar e inicializar um objeto da classe
    constructor(largura: number, altura: number) {
        this.largura = largura;
        this.altura = altura;
    }

    // Método para calcular a área
    calcularArea(): number {
        return this.largura * this.altura;
    }

    // --- NOVO MÉTODO ---
    // Método para calcular o perímetro
    calcularPerimetro(): number {
        return 2 * (this.largura + this.altura);
    }
}

// --- TESTANDO A CLASSE ---

// 1. Instanciando um objeto da classe Retangulo
const meuRetangulo = new Retangulo(10, 5);

// 2. Chamando os métodos e armazenando os resultados
const area = meuRetangulo.calcularArea();
const perimetro = meuRetangulo.calcularPerimetro();

// 3. Exibindo os resultados no console
console.log(`Dados do Retângulo:`);
console.log(`Largura: ${meuRetangulo.largura}`);
console.log(`Altura: ${meuRetangulo.altura}`);
console.log(`Área: ${area}`);
console.log(`Perímetro: ${perimetro}`);