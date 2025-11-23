import java.net.*;
import java.io.*;
import java.util.*;
public class HangClient {

    public static void main (String[] args) throws Exception {
        //initialization
        int serverPort = 6789;
        Socket clientSocket = new Socket(InetAddress.getByName(/*"localhost"*/""), serverPort); 
        DataOutputStream outChar = new DataOutputStream(clientSocket.getOutputStream());
        Scanner in = new Scanner(clientSocket.getInputStream());
        int wordLen = Integer.parseInt(in.nextLine());
        GUI window = new GUI(wordLen);
        Scanner userInput = new Scanner(System.in);
        boolean running = true;
        while(running) { //the game
            System.out.print("Give me a letter: ");
            String hangChar = userInput.nextLine();
            boolean invalidInput = true;
            boolean first = true;
            while(invalidInput) {
                if(!first) {
                    System.out.println("Invalid input, try again.");
                    System.out.print("Give me a letter: ");
                    hangChar = userInput.nextLine();
                }
                if (hangChar.matches("[a-zA-Z]")) { // accepts a single letter
                    invalidInput = false; 
                }
                first = false;
                }
            System.out.println("Valid input, processing...");
            outChar.writeBytes(hangChar + "\n"); 
            String outFromServer = in.nextLine();
            if(!outFromServer.equals("")) { //processing the server output
                String[] locations = outFromServer.split(" ");
                for (String str : locations) {
                    window.addLetter(hangChar.charAt(0), Integer.parseInt(str));
                }
                if(!window.isNotSolved()) {
                    running = false;
                    outChar.writeBytes("won\n");
                    System.out.println("You won!");
                    break;
                }
            } else if(!window.addMiss(hangChar)) {
                running = false;
                outChar.writeBytes("lost\n");
                System.out.println("You lost!");
                System.out.println(in.nextLine());
                break;
            }
        }
        in.close();
        clientSocket.close();
        userInput.close();
        System.exit(0);
    }
}