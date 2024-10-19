const data=require('./dados.json')
let faturamento=[];
let j=0;
let menorDia=0;
let maiorDia=0;
let media=0;
let dias=0;
for(let i=0;i<30;i++){
    if(data[i].valor!=0){
        faturamento[j]=data[i].valor;
        j++;
    }
}
menorValor=Math.min(...faturamento)
maiorValor=Math.max(...faturamento)
for(let i=0;i<30;i++){
    if(data[i].valor==menorValor){
        menorDia=data[i].dia;
        break;
    }
}
for(let i=0;i<30;i++){
    if(data[i].valor==maiorValor){
        maiorDia=data[i].dia;
        break;
    }
}
tamanho=Object.keys(faturamento).length
for(let i=0;i<tamanho;i++){
    media+=faturamento[i]
}
media/=21;
console.log('O menor valor é '+menorValor+' no dia '+menorDia+' e o maior é '+maiorValor+' no dia '+maiorDia)
for(let i=0;i<tamanho;i++){
    if(faturamento[i]>media){
        dias++;
    }
}
console.log('Foram '+dias+' de faturamento superior à média mensal.')