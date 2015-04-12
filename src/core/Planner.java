/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package core;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.nio.file.Files;
/**
 *
 * @author alex
 */
public class Planner {
    private BufferedReader ears;
    private String workspace;
    private String status;
    private ArrayList<Object> buffer;
    
    public void prompt(){
        if(!workspace.equals("")){
        if(!status.equals("")){
            System.out.print("|" + workspace + "|" + "(" + status + "..." + ")>> ");
        }
        else System.out.print("|" + workspace + "|>> ");
        }
        else System.out.print("|Planner|>> ");
    }
    
    public Planner(){
         this.ears = new BufferedReader(new InputStreamReader(System.in));
         System.out.println("Welcome to the Class Planner!");
         System.out.println("for help type '?' and hit enter");
         this.workspace = "";
         this.status = "";
         this.prompt();
    }
    
    public void start(){
      try{  
        boolean done = false;
        while(!done){
             if(!checkInput()){
                 done = true;
             }
         }
         System.out.println("Thanks for using the Class Planner, bye!");
      }catch(IOException e){System.out.println("Uh-oh, something went wrong with our interface...bye!");}
    }
    
    public boolean checkInput() throws IOException{
        String line = this.ears.readLine();
        String[] tokens = line.split(" ");
        switch(tokens[0]){
            case "":
                this.status = "";
                this.prompt();
                return true;
            
            case "new":
                _new(tokens);
                return true;
                
            case "add":
                add(tokens);
                return true;  
                
             case "remove":
                remove(tokens);
                return true;  
                
             case "edit":
                edit(tokens);
                return true; 
                
            default:
                return true;
        }
    }
    
    public void _new(String[] args){
        switch(args[1]){
            case "course":
                
        }
    }
    
    public void add(String[] args){
    
    }
    
    public void remove(String[] args){
    
    }
    
    public void edit(String[] args){
    
    }
    
    public static void main(String[] args){
        Planner main = new Planner();
        main.start();
    }
}
