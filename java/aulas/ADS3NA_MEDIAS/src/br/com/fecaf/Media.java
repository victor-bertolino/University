package br.com.fecaf;

import java.util.*;

public class Media {
	
	public static void main (String[]args) {
	
	Scanner scanner = new Scanner(System.in);
	System.out.print("Digite a primeira nota: ");
	float nota1 = scanner.nextFloat();
	System.out.print("Digite a segunda nota: ");
	float nota2 = scanner.nextFloat();
	System.out.print("Digite a terceira nota: ");
	float nota3 = scanner.nextFloat();
	System.out.print("Digite a quarta nota: ");
	float nota4 = scanner.nextFloat();
	float media;
	
	
	media = (nota1 + nota2 + nota3 + nota4) / 4;	
	
	}
}


/*
 * Operadores Lógicos
 * AND  &&
 * OR || (pipe)
 * NOT !
 */