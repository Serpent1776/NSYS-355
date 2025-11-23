import java.net.*;
import java.io.*;
import java.util.*;

public class HangServer {

    public static void main (String[] args) throws Exception {
       while(true) {
        int serverPort = 6789;
        ServerSocket welcomeSocket = new ServerSocket(serverPort);
        welcomeSocket.setSoTimeout(600000);
        try {
        int rand = (int)(Math.random()*12 + 1);
        String wordStr = "";
        switch (rand) {
            case 1:
                wordStr = "Arachnophobia";
                break;
            case 2:
                wordStr = "Imposter";
                break;
            case 3:
                wordStr = "Earth";
                break;
            case 4:
                wordStr = "Soul";
                break;
            case 5:
                wordStr = "Emotions";
                break;
            case 6:
                wordStr = "Authoritarian";
                break;
            case 7:
                wordStr = "Communism";
                break;
            case 8:
                wordStr = "Land";
                break;
            case 9:
                wordStr = "Sorcery";
                break;
            case 10:
                wordStr = "Instance";
                break;
            case 11:
                wordStr = "Stack";
                break;
            case 12:
                wordStr = "Universe";
                break;
            default:
                break;
        }
        Word theWord = new Word(wordStr);
        System.out.println("IP: " + InetAddress.getLocalHost()); //bugtesting
            Socket connectionSocket = welcomeSocket.accept();
            Scanner inFromClient = new Scanner(connectionSocket.getInputStream());
            DataOutputStream outtoClient = new DataOutputStream(connectionSocket.getOutputStream());
            boolean finished = false;
            int outInt = 0;
            outInt = theWord.getLength(); 
            outtoClient.writeBytes(outInt + "\n");
            while(!finished) {   
            String sentence = inFromClient.nextLine();
            if(sentence.equals("lost") || sentence.equals("won")) { //game end condition
            finished = true;
            if(sentence.equals("lost")) {
                outtoClient.writeBytes(theWord.getWord() + "\n");
            }
            } else {
            //System.out.println("Received: " + sentence);
            sentence = theWord.getSpots(sentence.charAt(0));
            outtoClient.writeBytes(sentence + "\n");
            }
            }
            inFromClient.close();
            connectionSocket.close();
            outtoClient.close();
            welcomeSocket.close();
    } catch(SocketTimeoutException e) {
        System.out.println("Server timed out!"); 
        break;
    }
    }
}
}