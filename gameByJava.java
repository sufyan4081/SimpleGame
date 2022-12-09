
package Game;

import java.util.Random;
import java.util.Scanner;

public class Game {
    public static void main(String[] args) {
                //for userInput code
        
        Scanner scan = new Scanner(System.in);
        System.out.println("\t\tWelocme to Rock,Paper and Scissor game.");
        System.out.println("Select your device:\n Enter 0 for Rock\n Enter 1 for Paper\n Enter 2 for Scissor ");
        int userInput = scan.nextInt();
        
               //for computerInput code
        Random random = new Random();
        int computerInput = random.nextInt(3);
        
        
        if (userInput == computerInput) 
        {
            System.out.println("Match is draw.");
        }
        else if (userInput ==0 && computerInput ==2 ||
                userInput ==1 && computerInput ==0||
                userInput ==2 && computerInput ==1)
        {
            System.out.println("You win");
        }
        else
        {
            System.out.println("You losed!");
        }
        switch(computerInput)
        {
            case 0:
                System.out.println("Computer selected is: Rock");
            break;
            
            case 1:
                System.out.println("Computer selected is: Paper");
            break;
            
            case 2:
                System.out.println("Computer selected is: Scissor");
            break;
        
        } 
    }       
                
        
}
    

