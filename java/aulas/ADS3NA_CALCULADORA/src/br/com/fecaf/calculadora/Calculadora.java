//package br.com.fecaf.calculadora;
//
//import java.util.Scanner;
//
//public class Calculadora {
//
//	public static void main(String[] args) {
//		// Variáveis de entrada de dados
//		float valor1;
//		float valor2;
//		float resultado;
//		String operador;
//		
//		// Cria o objeto input para manipular as entrada de dados pelo usuário
//		Scanner input = new Scanner(System.in);
//		
//		System.out.println("Digite um primeiro valor");
//		valor1 = input.nextFloat();
//		
//		System.out.println("Digite o segundo valor");
//		valor2 = input.nextFloat();
//		
//		System.out.println("Escolha a uma operação matemática [SOMAR | SUBTRAIR | MULTIPLICAR | DIVIDIR]");
//		operador = input.next();
//		
//		
//		// toUpperCase permite converter o conteúdo de uma string em maiúsculo
//		if(operador.toUpperCase().equals("SOMAR")) {
//			resultado = valor1 + valor2;
//		} else if (operador.toUpperCase().equals("SUBTRAIR")) {
//			resultado = valor1 - valor2;
//		} else if (operador.toUpperCase().equals("MULTIPLICAR")) {
//			resultado = valor1 * valor2;
//		} else if (operador.toUpperCase().equals("DIVIDIR")) {
//			if (valor2 == 0) 
//				System.out.println("ERRO: Não é possível realizar uma divisão por 0.");
//			 else 
//				resultado = valor1 / valor2;
//			
//		} else 
//			System.out.println("ERRO: A Operação escolhida não é válida");
		
		
		switch (tipoCalculo.toUpperCase()) {
		case "SOMAR": 
			resultado = valor1 + valor2;
			break;
		case "SUBTRAIR":	
			resultado = valor1 - valor2;
			break;
		case "MULTIPLICAR":	
			resultado = valor1 * valor2;
			break;
		case "DIVIDIR":
			if (valor2 == 0)
				System.out.println("ERRO: Não é possível realizar uma divisão por 0.");
			else
				resultado = valor1 / valor2;
			break;
			
		default:
			System.out.println("ERRO: A Operação escolhida não é válida");
			break;
		}
		
		System.out.println(resultado);
	}

}
