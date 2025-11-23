import java.net.*;
import java.io.*;
import java.util.*;
public class TCPServer {
    public static void main(String[] args) throws Exception {
        int serverPort = 14001;
        ServerSocket welcomeSocket = new ServerSocket(serverPort);
        System.out.println("My hame name" + InetAddress.getLocalHost());
        while(true) {
            Socket connectionSocket = welcomeSocket.accept();
            Scanner inFromClient = new Scanner(connectionSocket.getInputStream());
            String sentence = inFromClient.nextLine();
            System.out.println("Received: " + sentence);
            sentence = sentence.toUpperCase();
            DataOutputStream outtoClient = new DataOutputStream(connectionSocket.getOutputStream());
            outtoClient.writeBytes(sentence+'\n');
            inFromClient.close();
            connectionSocket.close();
            outtoClient.close();
        } 
    }
}