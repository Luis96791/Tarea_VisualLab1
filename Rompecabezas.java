package LabProgramacion2015;

//import java.util.Scanner;
import javax.swing.JOptionPane;

/**
 *
 * @author LEFF
 */
public class Rompecabezas {
    public static void main(String[] args) {
       // Scanner sc = new Scanner(System.in);
        
        //Los valores con los que va a comenzar el puzzle estan asignados a cada variable y
        // estan sujetos a modificaciones...
       
            int var11 = 4, var12 = 1, var13 = 8, 
                var21 = 2, var22 = 0, var23 = 6, 
                    var31 = 5, var32 = 7, var33 = 3;
        
        /**
         * Los JOptionPane funcionan a partir de la libreria Swing que fue importada en las primeras lineas del programa
         * Con esto NO es necesaria la librería Scanner...
         * Este JOptionPane muestra un mensaje de las teclas a usar en el juego..
         * Si en algún momento presionamos cancelar el juego termina y la aplicacion tambien es detenida
         * Mostrando un error en tiempo de ejecución-...
         */
        JOptionPane.showMessageDialog(null,"El Puzzle debe verse de la siguiente manera:\n\t |  1  |  2  |  3\n\t------------------\n\t |  4  |  5  |  6\n\t------------------\n\t |  7  |  8  |  0");
        JOptionPane.showMessageDialog(null,"Antes de Comenzar:\n W = Arriba\n S = Abajo\n A = Izquierda\n D = Derecha");
        
        // En el ciclo while se definen los valores con los que se quiere que termine cada variable
        // El while esta sujeto a un operador de negación que me analiza el valor que tiene cada variable
        // Si una variable no tiene el valor que le corresponde el ciclo continúa...
        
        while(!(var11 == 1 && var12 == 2 && var13 == 3
                && var21 == 4 && var22 == 5 && var23 == 6
                && var31 == 7 && var32 == 8 && var33 == 0)){
            
               System.out.println("**       PUZZLE EN JAVA      **");
               System.out.println("\t | " + var11 + " | " + var12 + " | " + var13 +"\n\t-------------");
               System.out.println("\t | " +var21 + " | " +var22 + " | " +var23 +"\n\t-------------");
               System.out.println("\t | " + var31 + " | " +var32 + " | " +var33 +"\n\n");
        
        String opcion = JOptionPane.showInputDialog("Ingrese una Letra (W, S, A, D): ");
        
        if (opcion.equalsIgnoreCase("w")) {
            //Columna 3 vertical hacia arriba
            if(var33 == 0){
               var33 = var23;
               var23 = 0;
            }
            
            else if(var23 == 0){
                var23 = var13;
                var13 = 0;
            }
             //Columna 2 vertical hacia arriba
            else if (var32 == 0) {
                var32 = var22;
                var22 = 0;
            }
            
            else if (var22 == 0) {
                var22 = var12;
                var12 = 0;
            }
            //Columna 1 vertical hacia arriba
            else if (var31 == 0) {
                var31 = var21;
                var21 = 0;
            }
            
            else if (var21 == 0) {
                var21 = var11;
                var11 = 0;
            }
        }else if (opcion.equalsIgnoreCase("a")) {
                    //Fila 3 horizontal hacia la izquierda
            if (var33 == 0) {
                var33 = var32;
                var32 = 0;   
                }
                        
                else if (var32 == 0) {
                    var32 = var31;
                    var31 = 0;
                }
                    //Fila 2 horizontal hacia la izquierda
                else if (var23 == 0) {
                    var23 = var22;
                    var22 = 0;
                }
                    
                else if (var22 == 0) {
                    var22 = var21;
                    var21 = 0;
                }
                //Fila 1 horizontal hacia la izquierda
                else if (var13 == 0) {
                    var13 = var12;
                    var12 = 0;
                }
                
                else if (var12 == 0) {
                    var12 = var11;
                    var11 = 0;
                }
            }
        
        else if (opcion.equalsIgnoreCase("d")) {
                //Fila 1 horizontal hacia la derecha
                if (var11 == 0) {
                    var11 = var12;
                    var12 = 0;
                }
                
                else if (var12 == 0) {
                    var12 = var13;
                    var13 = 0;
                }
                //Fila 2 horizontal hacia la derecha
                else if (var21 == 0){
                    var21 = var22;
                    var22 = 0;
                }
                
                else if(var22 == 0){
                    var22 = var23;
                    var23 = 0;
                }
                //Fila 3 horizontal hacia la derecha
                else if(var31 == 0){
                    var31 = var32;
                    var32 = 0;
                }
                
                else if(var32 == 0){
                    var32 = var33;
                    var33 = 0;
                }
            }else if(opcion.equalsIgnoreCase("s")){
                //Columna 1: vertical hacia abajo
                if(var11 == 0){
                    var11 = var21;
                    var21 = 0;
                }
                
                else if(var21 == 0){
                    var21 = var31;
                    var31 = 0;
                }
                //Columna 2: vertical hacia abajo
                
                else if(var12 == 0){
                    var12 = var22;
                    var22 = 0;
                }
                
                else if(var22 == 0){
                    var22 = var32;
                    var32 = 0;
                }
                //Columna 3: vertical hacia abajo
                
                else if(var13 == 0){
                    var13 = var23;
                    var23 = 0;
                }
                
                else if(var23 == 0){
                    var23 = var33;
                    var33 = 0;
                }
            }
        }
        //Si el ciclo termina con cada pieza en su respectiva variable muestra el mensaje de victoria...
        JOptionPane.showMessageDialog(null,"¡   FELICIDADES  !\n Has Completado el Puzzle...");
        //Automaticamente finaliza el programa con un BUILD SUCCESSFUL...
    }
}