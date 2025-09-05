class SituacaoFinanceira {
    valorCreditos: number;
    valorDebitos: number;

    constructor(creditos: number, debitos: number) {
        this.valorCreditos = creditos;
        this.valorDebitos = debitos;
    }

    /**
     * Calcula o saldo subtraindo os débitos dos créditos
     */

    calcularSaldo(): number {
        return this.valorCreditos - this.valorDebitos;
    }
}
// Inicia a classe com R$ 5000,00 de créditos e R$ 1850,75 de débitos
const minhasFinancas = new SituacaoFinanceira(5000, 1850.75);

const saldo = minhasFinancas.calcularSaldo();

console.log(`Valor dos Créditos: R$ ${minhasFinancas.valorCreditos.toFixed(2)} `);
console.log(`Valor dos Débitos: R$ ${minhasFinancas.valorDebitos.toFixed(2)} `);
console.log(`Saldo Disponível: R$ ${saldo.toFixed(2)} `);