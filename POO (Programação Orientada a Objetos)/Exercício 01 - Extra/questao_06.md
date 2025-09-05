**Jogo Escolhido: RPG de Fantasia**

Aqui estão alguns objetos que poderíamos encontrar nesse tipo de jogo:

* **Objeto: `Heroi`**
    * **Atributos:** nome, nivel, pontosDeVida, pontosDeMana, forca, defesa, inventario (uma lista de Itens).
    * **Métodos:** `atacar(alvo)`, `usarItem(item)`, `lancarMagia(magia)`, `ganharExperiencia()`.

* **Objeto: `Inimigo`**
    * **Atributos:** tipo (ex: "Goblin", "Dragão"), pontosDeVida, ataque, defesa, itensDeRecompensa.
    * **Métodos:** `atacar(alvo)`, `sofrerDano(dano)`, `morrer()`.

* **Objeto: `Item`**
    * **Atributos:** nome, tipo (ex: "Poção", "Arma", "Armadura"), efeito (ex: cura, aumento de ataque), valor.
    * **Métodos:** `serUsado(alvo)`, `serEquipado()`.

* **Objeto: `Magia`**
    * **Atributos:** nome, custoDeMana, dano, tipoDeEfeito (ex: "Fogo", "Cura", "Gelo").
    * **Métodos:** `lancar(caster, alvo)`.

* **Objeto: `Missao` (Quest)**
    * **Atributos:** titulo, descricao, objetivo (ex: "Derrote o Dragão"), recompensa (ouro, item), status (ex: "ativa", "concluída").
    * **Métodos:** `iniciar()`, `verificarProgresso()`, `completar()`.