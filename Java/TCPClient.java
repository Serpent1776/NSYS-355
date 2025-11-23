import java.net.*;
import java.io.*;
import java.util.*;
public class TCPClient {
    public static void main(String[] args) throws Exception {
        int serverPort = 13001;
        Socket clientSocket = new Socket(InetAddress.getByName("localhost"), serverPort);
        System.out.print("Give me a message please: ");
        Scanner userInput = new Scanner(System.in);
        String sentence = userInput.nextLine();
        DataOutputStream outToServer = new DataOutputStream(clientSocket.getOutputStream());
        outToServer.writeBytes(sentence + "\n");
        Scanner serverInput = new Scanner(clientSocket.getInputStream());
        sentence = serverInput.nextLine();
        System.out.println("Recieved: " + sentence);
        clientSocket.close();
        userInput.close();
        serverInput.close();
    }
    
}
