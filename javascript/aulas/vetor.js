const vetor = [];
let i;

for (i = 0; i <= 5; i++) {
    const numero = parseInt(prompt(`Digite o ${i + 1}° número:`));
    vetor.push(numero);
}

for (i = 0; i <= 5; i++) {
    console.log(vetor[i]);
}